"""抽象端口：由基础设施层实现，服务层依赖这些抽象。"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable

from ..domain.entities import (
    Job,
    Movement,
    MovementInfo,
    MovementResult,
    RobotAddress,
    SpeechResult,
)
from ..domain.values import Color


class RobotPort(ABC):
    """对机器人外部系统的抽象网关。"""

    # -- 生命周期 -----------------------------------------------------------
    @property
    @abstractmethod
    def connected(self) -> bool: ...

    @abstractmethod
    def connect(self) -> None: ...

    @abstractmethod
    def disconnect(self) -> None: ...

    @abstractmethod
    def status(self) -> dict: ...

    @abstractmethod
    def ping(self) -> bool: ...

    # -- 说话 ---------------------------------------------------------------
    @abstractmethod
    def say(self, text: str, language: str | None = None, animated: bool = False) -> None: ...

    @abstractmethod
    def stop_speaking(self) -> None: ...

    # -- 运动 ---------------------------------------------------------------
    @abstractmethod
    def wake_up(self) -> None: ...

    @abstractmethod
    def rest(self) -> None: ...

    @abstractmethod
    def list_postures(self) -> list[str]: ...

    @abstractmethod
    def go_to_posture(self, name: str, speed: float = 0.5) -> str: ...

    @abstractmethod
    def set_angles(self, names: list[str], angles: list[float], speed: float = 0.2) -> None: ...

    @abstractmethod
    def move(self, x: float, y: float, theta: float) -> None: ...

    @abstractmethod
    def stop_all(self) -> None: ...

    @abstractmethod
    def play_trajectory(self, movement: Movement) -> MovementResult: ...

    # -- 摄像头 -------------------------------------------------------------
    @abstractmethod
    def start_camera(self) -> None: ...

    @abstractmethod
    def stop_camera(self) -> None: ...

    @abstractmethod
    def camera_frame(self) -> bytes | None: ...

    @abstractmethod
    def camera_snapshot(self, resolution: int | None = None) -> bytes: ...

    @abstractmethod
    def camera_info(self) -> dict: ...

    # -- 语音识别 -----------------------------------------------------------
    @abstractmethod
    def listen(
        self,
        vocabulary: list[str],
        timeout_s: float = 6.0,
        word_spotting: bool = True,
        language: str | None = None,
        min_confidence: float = 0.0,
    ) -> SpeechResult: ...

    # -- LED / 音量 ---------------------------------------------------------
    @abstractmethod
    def set_leds(self, name: str, color: Color, duration: float) -> None: ...

    @abstractmethod
    def leds_off(self, name: str) -> None: ...

    @abstractmethod
    def set_led_intensity(self, name: str, intensity: float) -> None: ...

    @abstractmethod
    def rasta(self, duration: float) -> None: ...

    @abstractmethod
    def get_volume(self) -> int: ...

    @abstractmethod
    def set_volume(self, volume: int) -> int: ...

    # -- 逃生舱 -------------------------------------------------------------
    @abstractmethod
    def call_service(self, service: str, method: str, args: list | None = None) -> Any: ...


class MovementRepository(ABC):
    """动作数据来源（文件、数据库或内存）。"""

    @abstractmethod
    def list(self) -> list[MovementInfo]: ...

    @abstractmethod
    def names(self) -> list[str]: ...

    @abstractmethod
    def exists(self, name: str) -> bool: ...

    @abstractmethod
    def info(self, name: str) -> MovementInfo: ...

    @abstractmethod
    def load(self, name: str) -> Movement: ...


class RobotLocator(ABC):
    """在局域网中探测 NAOqi 端点。"""

    @abstractmethod
    def local_subnets(self) -> list[str]: ...

    @abstractmethod
    def scan(
        self, targets: list[str] | None = None, timeout_s: float = 0.3
    ) -> list[RobotAddress]: ...


class JobQueue(ABC):
    """后台长任务队列。"""

    @abstractmethod
    def submit(self, kind: str, name: str, func: Callable[[], Any]) -> Job: ...

    @abstractmethod
    def get(self, job_id: str) -> Job: ...

    @abstractmethod
    def list(self) -> list[Job]: ...

    @abstractmethod
    def current(self) -> Job | None: ...

    @abstractmethod
    def busy(self) -> bool: ...

    @abstractmethod
    def cancel(self, job_id: str, on_cancel: Callable[[], None] | None = None) -> bool: ...
