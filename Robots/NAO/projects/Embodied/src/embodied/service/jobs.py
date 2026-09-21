"""后台任务服务：编排动作执行与取消。"""

from __future__ import annotations

from ..domain.entities import Job
from .movement import MovementService
from .ports import JobQueue, RobotPort


class JobService:
    def __init__(
        self,
        queue: JobQueue,
        movement: MovementService,
        robot: RobotPort,
    ) -> None:
        self._queue = queue
        self._movement = movement
        self._robot = robot

    def submit_movement(self, name: str) -> Job:
        self._movement.ensure_exists(name)
        return self._queue.submit(
            "movement", name, lambda: self._movement.execute(name).to_dict()
        )

    def get(self, job_id: str) -> Job:
        return self._queue.get(job_id)

    def list(self) -> list[Job]:
        return self._queue.list()

    def current(self) -> Job | None:
        return self._queue.current()

    def busy(self) -> bool:
        return self._queue.busy()

    def cancel(self, job_id: str) -> bool:
        return self._queue.cancel(job_id, on_cancel=self._robot.stop_all)
