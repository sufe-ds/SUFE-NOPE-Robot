"""任务队列的线程实现：单后台 worker。"""

from __future__ import annotations

import queue
import threading
import time
import uuid
from typing import Any, Callable

from ..domain.entities import Job
from ..domain.errors import JobNotFoundError
from ..domain.values import JobStatus
from .ports import JobQueue


class ThreadJobQueue(JobQueue):
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
                if job.status == JobStatus.RUNNING:
                    return job
        return None

    def busy(self) -> bool:
        return self.current() is not None

    def cancel(self, job_id: str, on_cancel: Callable[[], None] | None = None) -> bool:
        job = self.get(job_id)
        if job.status not in (JobStatus.QUEUED, JobStatus.RUNNING):
            return False
        job.status = JobStatus.CANCELLED
        job.finished_at = time.time()
        if on_cancel is not None:
            try:
                on_cancel()
            except Exception:  # 取消失败不改状态
                pass
        return True

    def _run(self) -> None:
        while True:
            job, func = self._queue.get()
            try:
                if job.status != JobStatus.CANCELLED:
                    job.status = JobStatus.RUNNING
                    job.started_at = time.time()
                    try:
                        job.result = func()
                        if job.status != JobStatus.CANCELLED:
                            job.status = JobStatus.DONE
                    except Exception as exc:  # noqa: BLE001
                        job.error = str(exc)
                        if job.status != JobStatus.CANCELLED:
                            job.status = JobStatus.FAILED
            finally:
                job.finished_at = time.time()
                self._queue.task_done()
