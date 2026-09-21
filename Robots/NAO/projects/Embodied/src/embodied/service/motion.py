"""姿态与基础运动服务。"""

from __future__ import annotations

from ..domain.errors import ValidationError
from .ports import RobotPort


class MotionService:
    def __init__(self, robot: RobotPort) -> None:
        self._robot = robot

    def wake_up(self) -> None:
        self._robot.wake_up()

    def rest(self) -> None:
        self._robot.rest()

    def list_postures(self) -> list[str]:
        return self._robot.list_postures()

    def go_to_posture(self, name: str, speed: float = 0.5) -> str:
        return self._robot.go_to_posture(name, speed)

    def set_angles(self, names: list[str], angles: list[float], speed: float = 0.2) -> None:
        if len(names) != len(angles):
            raise ValidationError("names 与 angles 长度不一致")
        self._robot.set_angles(names, angles, speed)

    def move(self, x: float, y: float, theta: float) -> None:
        self._robot.move(x, y, theta)
