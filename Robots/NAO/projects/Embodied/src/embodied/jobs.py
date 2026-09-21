"""后台动作队列：长动作（如舞蹈）异步执行，用 job_id 轮询。"""

from __future__ import annotations

import queue
import threading
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Callable

from .errors import JobNotFoundError


@dataclass
class Job:
    id: str
    kind: str
    name: str
    status: str = "queued"  # queued | running | done | failed | cancelled
    created_at: float = field(default_factory=time.time)
    started_at: float | None = None
    finished_at: float | None = None
    result: Any = None
    error: str | None = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "kind": self.kind,
            "name": self.name,
            "status": self.status,
            "created_at": self.created_at,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "result": self.result,
            "error": self.error,
        }


class ActionRunner:
    """单后台 worker，保证同一时刻只有一个长动作在跑。"""

    def __init__(self) -> None:
        self._queue: queue.Queue = queue.Queue()
        self._jobs: dict[str, Job] = {}
        self._lock = threading.Lock()
        self._worker = threading.Thread(
            target=self._run, name="embodied-actions", daemon=True
        )
        self._worker.start()

    def submit(self, kind: str, name: str, func: Callable[[], Any]) -> Job:
        job = Job(id=uuid.uuid4().hex[:12], kind=kind, name=name)
        with self._lock:
            self._jobs[job.id] = job
        self._queue.put((job, func))
        return job

    def get(self, job_id: str) -> Job:
        with self._lock:
            job = self._jobs.get(job_id)
        if job is None:
            raise JobNotFoundError(f"未知任务：{job_id}")
        return job

    def list(self) -> list[Job]:
        with self._lock:
            jobs = list(self._jobs.values())
        return sorted(jobs, key=lambda job: job.created_at, reverse=True)

    def current(self) -> Job | None:
        with self._lock:
            for job in self._jobs.values():
                if job.status == "running":
                    return job
        return None

    def busy(self) -> bool:
        return self.current() is not None

    def cancel(self, job_id: str, on_cancel: Callable[[], None] | None = None) -> bool:
        job = self.get(job_id)
        if job.status not in ("queued", "running"):
            return False
        job.status = "cancelled"
        job.finished_at = time.time()
        if on_cancel is not None:
            try:
                on_cancel()
            except Exception:  # noqa: BLE001 - 取消失败不改状态
                pass
        return True

    def _run(self) -> None:
        while True:
            job, func = self._queue.get()
            try:
                if job.status != "cancelled":
                    job.status = "running"
                    job.started_at = time.time()
                    try:
                        job.result = func()
                        if job.status != "cancelled":
                            job.status = "done"
                    except Exception as exc:  # noqa: BLE001
                        job.error = str(exc)
                        if job.status != "cancelled":
                            job.status = "failed"
            finally:
                job.finished_at = time.time()
                self._queue.task_done()
