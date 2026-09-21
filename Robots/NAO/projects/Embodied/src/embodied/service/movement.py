"""动作/舞蹈服务：从仓储取轨迹，交由机器人执行。"""

from __future__ import annotations

from ..domain.entities import MovementInfo, MovementResult
from ..domain.errors import UnknownMovementError
from .ports import MovementRepository, RobotPort


class MovementService:
    def __init__(self, movements: MovementRepository, robot: RobotPort) -> None:
        self._movements = movements
        self._robot = robot

    def list(self) -> list[MovementInfo]:
        return self._movements.list()

    def names(self) -> list[str]:
        return self._movements.names()

    def info(self, name: str) -> MovementInfo:
        return self._movements.info(name)

    def ensure_exists(self, name: str) -> None:
        if not self._movements.exists(name):
            raise UnknownMovementError(f"未知动作：{name}", detail=self._movements.names())

    def execute(self, name: str) -> MovementResult:
        movement = self._movements.load(name)
        return self._robot.play_trajectory(movement)
