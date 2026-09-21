"""机器人生命周期与急停服务。"""

from __future__ import annotations

from .ports import RobotPort


class GatewayService:
    def __init__(self, robot: RobotPort) -> None:
        self._robot = robot

    def connect(self) -> None:
        self._robot.connect()

    def disconnect(self) -> None:
        self._robot.disconnect()

    def connected(self) -> bool:
        return self._robot.connected

    def status(self) -> dict:
        return self._robot.status()

    def ping(self) -> bool:
        return self._robot.ping()

    def stop_all(self) -> None:
        self._robot.stop_all()
