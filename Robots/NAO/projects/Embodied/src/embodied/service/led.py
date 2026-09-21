"""LED 服务。"""

from __future__ import annotations

from ..domain.values import Color
from .ports import RobotPort


class LedService:
    def __init__(self, robot: RobotPort) -> None:
        self._robot = robot

    def set_leds(self, name: str = "FaceLeds", color: str | int = "#00A0FF", duration: float = 0.5) -> None:
        self._robot.set_leds(name, Color.parse(color), duration)

    def off(self, name: str = "FaceLeds") -> None:
        self._robot.leds_off(name)

    def set_intensity(self, name: str, intensity: float) -> None:
        self._robot.set_led_intensity(name, intensity)

    def rasta(self, duration: float = 1.0) -> None:
        self._robot.rasta(duration)
