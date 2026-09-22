"""qi / NAOqi 机器人适配器（RobotPort 的具体实现）。

线程模型：
- ``_motion_lock`` 串行化运动类服务；长动作会长时间持有它，
  因此 ``stop_all`` 故意绕过该锁，保证随时急停。
- ``_call_lock`` 串行化其余 I/O；两类锁互相独立，跳舞时仍可说话、拍照。
"""

from __future__ import annotations

import base64
import io
import threading
import time
import uuid
from contextlib import contextmanager
from typing import Any, Iterator

import qi
from PIL import Image

from ..domain.entities import Movement, MovementResult, SpeechResult
from ..domain.errors import (
    ActionTimeoutError,
    RobotCallError,
    RobotError,
    RobotUnreachableError,
    ServiceUnavailableError,
    UnknownMovementError,
    UnknownPostureError,
    UnknownServiceMethodError,
    ValidationError,
)
from ..domain.values import Color
from .config import Settings
from .ports import RobotPort

_MOTION_SERVICES = frozenset({"ALMotion", "ALRobotPosture"})
_COLOR_SPACE_RGB = 11


def connect(ip: str, port: int = 9559) -> qi.Session:
    """连接 NAOqi，返回 qi.Session（兼容旧版）。"""
    session = qi.Session()
    session.connect(f"tcp://{ip}:{port}")
    return session


def to_jsonable(value: Any) -> Any:
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, (bytes, bytearray)):
        return base64.b64encode(bytes(value)).decode("ascii")
    if isinstance(value, (list, tuple)):
        return [to_jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): to_jsonable(val) for key, val in value.items()}
    return str(value)


class CameraStreamer:
    """后台持续订阅摄像头，缓存最新一帧 JPEG。"""

    def __init__(self, robot: "QiRobot", camera: int, resolution: int, fps: int) -> None:
        self.robot = robot
        self.camera = camera
        self.resolution = resolution
        self.fps = max(1, int(fps))
        self.name = f"embodied_{uuid.uuid4().hex[:8]}"
        self.width = 0
        self.height = 0
        self._handle: str | None = None
        self._thread: threading.Thread | None = None
        self._stop = threading.Event()
        self._frame: bytes | None = None
        self._frame_ts = 0.0
        self._frame_lock = threading.RLock()
        self._error: str | None = None

    @property
    def error(self) -> str | None:
        return self._error

    def start(self) -> None:
        if self._thread is not None and self._thread.is_alive():
            return
        self._stop.clear()
        self._thread = threading.Thread(
            target=self._run, name="embodied-camera", daemon=True
        )
        self._thread.start()

    def _run(self) -> None:
        try:
            video = self.robot._resolve("ALVideoDevice")
            self._handle = video.subscribeCamera(
                self.name, self.camera, self.resolution, _COLOR_SPACE_RGB, self.fps
            )
        except Exception as exc:  # noqa: BLE001
            self._error = str(exc)
            return
        interval = 1.0 / self.fps
        try:
            while not self._stop.is_set():
                started = time.perf_counter()
                try:
                    data = video.getImageRemote(self._handle)
                    if data and len(data) >= 7:
                        width, height = int(data[0]), int(data[1])
                        raw = bytes(data[6])
                        image = Image.frombuffer(
                            "RGB", (width, height), raw, "raw", "RGB", 0, 1
                        )
                        buffer = io.BytesIO()
                        image.save(buffer, "JPEG", quality=80)
                        with self._frame_lock:
                            self._frame = buffer.getvalue()
                            self._frame_ts = time.time()
                            self.width, self.height = width, height
                        self._error = None
                except Exception as exc:  # noqa: BLE001
                    self._error = str(exc)
                elapsed = time.perf_counter() - started
                self._stop.wait(max(0.0, interval - elapsed))
        finally:
            try:
                video.unsubscribe(self._handle)
            except Exception:  # noqa: BLE001
                pass
            self._handle = None

    def snapshot(self) -> bytes | None:
        with self._frame_lock:
            return self._frame

    def wait_for_frame(self, timeout: float = 3.0) -> bytes | None:
        deadline = time.time() + timeout
        while time.time() < deadline:
            frame = self.snapshot()
            if frame is not None:
                return frame
            time.sleep(0.05)
        return self.snapshot()

    def frame_age(self) -> float | None:
        with self._frame_lock:
            if self._frame is None:
                return None
            return round(time.time() - self._frame_ts, 3)

    def info(self) -> dict:
        # 注意：_frame_lock 不可重入，这里直接在持锁状态下计算 age，
        # 不能调用 frame_age()（它会再次获取同一把锁导致死锁）。
        with self._frame_lock:
            age = None if self._frame is None else round(time.time() - self._frame_ts, 3)
            return {
                "camera": self.camera,
                "resolution": self.resolution,
                "width": self.width,
                "height": self.height,
                "fps": self.fps,
                "age_s": age,
                "error": self._error,
            }

    def stop(self) -> None:
        self._stop.set()
        if self._thread is not None:
            self._thread.join(timeout=2.0)
            self._thread = None


class QiRobot(RobotPort):
    def __init__(self, settings: Settings, session: qi.Session | None = None) -> None:
        self.settings = settings
        self._session = session
        self._services: dict[str, Any] = {}
        self._motion_lock = threading.RLock()
        self._call_lock = threading.RLock()
        self._camera_lock = threading.Lock()
        self._camera: CameraStreamer | None = None
        self._awake = False
        self._posture: str | None = None
        self._tts_language: str | None = None

    # -- 连接 ---------------------------------------------------------------
    @property
    def connected(self) -> bool:
        return self._session is not None

    def connect(self) -> None:
        if self._session is not None:
            return
        try:
            self._session = connect(self.settings.nao_ip, self.settings.nao_port)
        except Exception as exc:  # noqa: BLE001
            raise RobotUnreachableError(
                f"无法连接 NAO {self.settings.nao_ip}:{self.settings.nao_port}",
                detail=str(exc),
            ) from exc

    def disconnect(self) -> None:
        self.stop_camera()
        self._services.clear()
        if self._session is not None:
            try:
                self._session.close()
            except Exception:  # noqa: BLE001
                pass
            self._session = None

    def _resolve(self, service: str) -> Any:
        if self._session is None:
            self.connect()
        proxy = self._services.get(service)
        if proxy is None:
            try:
                proxy = self._session.service(service)
            except Exception as exc:  # noqa: BLE001
                raise ServiceUnavailableError(
                    f"服务不可用：{service}", detail=str(exc)
                ) from exc
            self._services[service] = proxy
        return proxy

    def _invoke(self, service: str, method: str, args: tuple = ()) -> Any:
        proxy = self._resolve(service)
        try:
            func = getattr(proxy, method)
        except AttributeError as exc:
            raise UnknownServiceMethodError(f"{service} 没有方法 {method}") from exc
        try:
            return func(*args)
        except RobotError:
            raise
        except Exception as exc:  # noqa: BLE001
            raise RobotCallError(f"{service}.{method} 调用失败：{exc}") from exc

    def _acquire(self, lock: threading.RLock, timeout: float | None) -> None:
        if timeout is None:
            timeout = self.settings.action_timeout_s
        acquired = lock.acquire() if timeout < 0 else lock.acquire(timeout=timeout)
        if not acquired:
            raise ActionTimeoutError("机器人正忙，请稍后重试")

    @contextmanager
    def _motion(self, timeout: float | None = None) -> Iterator[None]:
        self._acquire(self._motion_lock, timeout)
        try:
            yield
        finally:
            self._motion_lock.release()

    def _call(self, service: str, method: str, *args: Any, timeout: float | None = None) -> Any:
        lock = self._motion_lock if service in _MOTION_SERVICES else self._call_lock
        self._acquire(lock, timeout)
        try:
            return self._invoke(service, method, tuple(args))
        finally:
            lock.release()

    def ping(self) -> bool:
        try:
            self._call("ALTextToSpeech", "getLanguage")
            return True
        except RobotError:
            return False

    def status(self) -> dict:
        return {
            "connected": self.connected,
            "ip": self.settings.nao_ip,
            "port": self.settings.nao_port,
            "awake": self._awake,
            "posture": self._posture,
            "tts_language": self._tts_language,
        }

    # -- 说话 ---------------------------------------------------------------
    def say(self, text: str, language: str | None = None, animated: bool = False) -> None:
        text = (text or "").strip()
        if not text:
            return
        if animated:
            self._call("ALAnimatedSpeech", "say", text)
            return
        lang = language or "Chinese"
        if lang != self._tts_language:
            self._call("ALTextToSpeech", "setLanguage", lang)
            self._tts_language = lang
        self._call("ALTextToSpeech", "say", text)

    def stop_speaking(self) -> None:
        self._call("ALTextToSpeech", "stopAll")

    # -- 姿态与运动 ---------------------------------------------------------
    def _wake(self) -> None:
        if not self._awake:
            self._invoke("ALMotion", "wakeUp")
            self._awake = True

    def wake_up(self) -> None:
        with self._motion():
            self._wake()

    def rest(self) -> None:
        with self._motion():
            self._invoke("ALMotion", "rest")
        self._awake = False
        self._posture = None

    def list_postures(self) -> list[str]:
        return list(self._call("ALRobotPosture", "getPostureList"))

    def go_to_posture(self, name: str, speed: float = 0.5) -> str:
        postures = self.list_postures()
        if name not in postures:
            raise UnknownPostureError(f"未知姿态：{name}", detail=postures)
        with self._motion():
            self._wake()
            self._invoke("ALRobotPosture", "goToPosture", (name, float(speed)))
        self._posture = name
        return name

    def set_angles(self, names: list[str], angles: list[float], speed: float = 0.2) -> None:
        if len(names) != len(angles):
            raise ValidationError("names 与 angles 长度不一致")
        with self._motion():
            self._wake()
            self._invoke(
                "ALMotion",
                "setAngles",
                (list(names), [float(a) for a in angles], float(speed)),
            )

    def move(self, x: float, y: float, theta: float) -> None:
        with self._motion():
            self._wake()
            self._invoke("ALMotion", "moveTo", (float(x), float(y), float(theta)))

    def stop_all(self) -> None:
        for service, method in (("ALMotion", "killAll"), ("ALTextToSpeech", "stopAll")):
            try:
                self._invoke(service, method)
            except Exception:  # noqa: BLE001 - 急停尽力而为
                pass

    def play_trajectory(self, movement: Movement) -> MovementResult:
        if not movement.names:
            raise UnknownMovementError(f"动作 {movement.name} 不含关键帧")
        started = time.perf_counter()
        with self._motion(timeout=-1):
            self._wake()
            if movement.posture:
                try:
                    self._invoke("ALRobotPosture", "goToPosture", (movement.posture, 0.5))
                except RobotError:
                    pass
            self._invoke(
                "ALMotion",
                "angleInterpolationBezier",
                (movement.names, movement.times, movement.angles),
            )
            self._posture = movement.posture or self._posture
        return MovementResult(
            name=movement.name,
            duration_s=round(time.perf_counter() - started, 3),
            joints=len(movement.names),
        )

    # -- 摄像头 -------------------------------------------------------------
    def _ensure_camera(self, resolution: int | None = None) -> CameraStreamer:
        with self._camera_lock:
            if self._camera is None:
                self._camera = CameraStreamer(
                    self,
                    camera=0,
                    resolution=(
                        resolution
                        if resolution is not None
                        else self.settings.camera_resolution
                    ),
                    fps=self.settings.camera_fps,
                )
            self._camera.start()
            return self._camera

    def start_camera(self) -> None:
        self._ensure_camera()

    def stop_camera(self) -> None:
        with self._camera_lock:
            if self._camera is not None:
                self._camera.stop()
                self._camera = None

    def camera_snapshot(self, resolution: int | None = None) -> bytes:
        streamer = self._ensure_camera(resolution)
        frame = streamer.wait_for_frame(timeout=3.0)
        if frame is None:
            raise ServiceUnavailableError("摄像头暂无可用的画面", detail=streamer.error)
        return frame

    def camera_frame(self) -> bytes | None:
        if self._camera is None:
            return None
        return self._camera.snapshot()

    def camera_info(self) -> dict:
        if self._camera is None:
            return {
                "camera": 0,
                "resolution": self.settings.camera_resolution,
                "age_s": None,
            }
        return self._camera.info()

    # -- 语音识别 -----------------------------------------------------------
    def listen(
        self,
        vocabulary: list[str],
        timeout_s: float = 6.0,
        word_spotting: bool = True,
        language: str | None = None,
        min_confidence: float = 0.0,
    ) -> SpeechResult:
        if not vocabulary:
            raise ValidationError("vocabulary 不能为空")
        token = f"embodied_asr_{uuid.uuid4().hex[:6]}"
        self._call("ALSpeechRecognition", "setLanguage", language or "Chinese")
        self._call("ALSpeechRecognition", "setVocabulary", list(vocabulary), bool(word_spotting))
        self._call("ALSpeechRecognition", "subscribe", token)
        try:
            try:
                self._call("ALMemory", "removeData", "WordRecognized")
            except RobotError:
                pass
            deadline = time.time() + float(timeout_s)
            while time.time() < deadline:
                try:
                    detected = self._call("ALMemory", "getData", "WordRecognized")
                except RobotError:
                    detected = None
                if detected and len(detected) >= 2 and detected[0]:
                    word, confidence = str(detected[0]), float(detected[1])
                    if confidence >= min_confidence:
                        return SpeechResult(True, word, confidence)
                time.sleep(0.2)
            return SpeechResult(False, None, 0.0)
        finally:
            try:
                self._call("ALSpeechRecognition", "unsubscribe", token)
            except RobotError:
                pass

    # -- LED / 音量 ---------------------------------------------------------
    def set_leds(self, name: str, color: Color, duration: float) -> None:
        self._call("ALLeds", "fadeRGB", name, color.to_int(), float(duration))

    def leds_off(self, name: str) -> None:
        self._call("ALLeds", "off", name)

    def set_led_intensity(self, name: str, intensity: float) -> None:
        self._call("ALLeds", "setIntensity", name, float(intensity))

    def rasta(self, duration: float) -> None:
        self._call("ALLeds", "rasta", float(duration))

    def get_volume(self) -> int:
        return int(self._call("ALAudioDevice", "getOutputVolume"))

    def set_volume(self, volume: int) -> int:
        value = max(0, min(100, int(volume)))
        self._call("ALAudioDevice", "setOutputVolume", value)
        return value

    # -- 逃生舱（策略在服务层，这里只做调用） --------------------------------
    def call_service(self, service: str, method: str, args: list | None = None) -> Any:
        return to_jsonable(self._call(service, method, *(args or [])))
