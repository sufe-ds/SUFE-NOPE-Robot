"""不连接机器人的假实现，用于 ``--dry-run`` 与测试。"""

from __future__ import annotations

import io
import time

from PIL import Image

from .config import Settings
from .errors import (
    ForbiddenCallError,
    ServiceUnavailableError,
    UnknownMovementError,
    UnknownPostureError,
)
from .movements import MovementLibrary
from .robot import AsrResult, MovementResult

_POSTURES = ["Stand", "StandInit", "StandZero", "Crouch", "Sit", "LyingBelly", "LyingBack"]


class FakeRobot:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or Settings(dry_run=True)
        self.movements = MovementLibrary(self.settings.movement_dir)
        self._awake = False
        self._posture: str | None = None
        self._volume = 50
        self._tts_language: str | None = None
        self._camera_started = False

    # -- 连接 / 状态 -------------------------------------------------------
    @property
    def connected(self) -> bool:
        return True

    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def ping(self) -> bool:
        return True

    def status(self) -> dict:
        return {
            "connected": True,
            "ip": self.settings.nao_ip,
            "port": self.settings.nao_port,
            "awake": self._awake,
            "posture": self._posture,
            "tts_language": self._tts_language,
        }

    # -- 说话 --------------------------------------------------------------
    def say(self, text: str, language: str | None = None, animated: bool = False) -> None:
        self._tts_language = language or "Chinese"

    def stop_speaking(self) -> None:
        pass

    # -- 姿态与运动 --------------------------------------------------------
    def wake_up(self) -> None:
        self._awake = True

    def rest(self) -> None:
        self._awake = False
        self._posture = None

    def list_postures(self) -> list[str]:
        return list(_POSTURES)

    def go_to_posture(self, name: str, speed: float = 0.5) -> str:
        if name not in _POSTURES:
            raise UnknownPostureError(f"未知姿态：{name}", detail=_POSTURES)
        self._awake = True
        self._posture = name
        return name

    def set_angles(self, names: list[str], angles: list[float], speed: float = 0.2) -> None:
        self._awake = True

    def move(self, x: float, y: float, theta: float) -> None:
        self._awake = True

    def stop_motion(self) -> None:
        pass

    def stop_all(self) -> None:
        pass

    # -- 动作 --------------------------------------------------------------
    def list_movements(self):
        return self.movements.list()

    def play_movement(self, name: str) -> MovementResult:
        _, _, times, _ = self.movements.prepare(name)
        time.sleep(0.05)
        return MovementResult(name=name, duration_s=0.05, joints=len(times))

    # -- 摄像头 ------------------------------------------------------------
    def start_camera(self) -> None:
        self._camera_started = True

    def stop_camera(self) -> None:
        self._camera_started = False

    def _jpeg(self) -> bytes:
        if not self._camera_started:
            raise ServiceUnavailableError("摄像头未启动")
        buffer = io.BytesIO()
        Image.new("RGB", (320, 240), (30, 60, 90)).save(buffer, "JPEG")
        return buffer.getvalue()

    def camera_snapshot(self, resolution: int | None = None) -> bytes:
        self._camera_started = True
        return self._jpeg()

    def camera_frame(self) -> bytes | None:
        if not self._camera_started:
            return None
        return self._jpeg()

    def camera_info(self) -> dict:
        return {
            "camera": 0,
            "resolution": self.settings.camera_resolution,
            "width": 320,
            "height": 240,
            "fps": self.settings.camera_fps,
            "age_s": 0.0,
            "error": None,
        }

    # -- 语音识别 ----------------------------------------------------------
    def listen(
        self,
        vocabulary: list[str],
        timeout_s: float = 6.0,
        word_spotting: bool = True,
        language: str | None = None,
        min_confidence: float = 0.0,
    ) -> AsrResult:
        if not vocabulary:
            raise UnknownMovementError("vocabulary 不能为空")
        return AsrResult(True, vocabulary[0], 1.0)

    # -- LED / 音量 --------------------------------------------------------
    def set_leds(self, name: str = "FaceLeds", color: str | int = "#00A0FF", duration: float = 0.5) -> None:
        pass

    def leds_off(self, name: str = "FaceLeds") -> None:
        pass

    def set_led_intensity(self, name: str, intensity: float) -> None:
        pass

    def rasta(self, duration: float = 1.0) -> None:
        pass

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, volume: int) -> int:
        self._volume = max(0, min(100, int(volume)))
        return self._volume

    # -- 逃生舱 ------------------------------------------------------------
    def call_service(self, service: str, method: str, args: list | None = None) -> dict:
        if not self.settings.enable_escape_hatch:
            raise ForbiddenCallError("逃生舱未启用（dry-run）")
        return {"fake": True, "service": service, "method": method, "args": args}
