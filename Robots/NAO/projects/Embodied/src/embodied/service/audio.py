"""音量服务。"""

from __future__ import annotations

from .ports import RobotPort


class AudioService:
    def __init__(self, robot: RobotPort) -> None:
        self._robot = robot

    def get_volume(self) -> int:
        return self._robot.get_volume()

    def set_volume(self, volume: int) -> int:
        return self._robot.set_volume(volume)
