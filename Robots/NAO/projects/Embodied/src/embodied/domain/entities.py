"""领域实体。"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any

from .values import JobStatus


@dataclass(frozen=True)
class MovementInfo:
    name: str
    posture: str
    time_hint: float
    joint_count: int

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "posture": self.posture,
            "time_hint": self.time_hint,
            "joint_count": self.joint_count,
        }


@dataclass(frozen=True)
class Movement:
    """一段已展平的动作轨迹。"""

    name: str
    posture: str
    names: list[str]
    times: list[list[float]]
    angles: list[list[list[float]]]


@dataclass(frozen=True)
class MovementResult:
    name: str
    duration_s: float
    joints: int

    def to_dict(self) -> dict:
        return {"name": self.name, "duration_s": self.duration_s, "joints": self.joints}


@dataclass(frozen=True)
class SpeechResult:
    recognized: bool
    word: str | None
    confidence: float

    def to_dict(self) -> dict:
        return {
            "recognized": self.recognized,
            "word": self.word,
            "confidence": self.confidence,
        }


@dataclass(frozen=True)
class RobotAddress:
    """局域网中探测到的一个 NAOqi 端点。"""

    ip: str
    port: int = 9559
    name: str | None = None

    def to_dict(self) -> dict:
        return {"ip": self.ip, "port": self.port, "name": self.name}


@dataclass
class Job:
    id: str
    kind: str
    name: str
    status: JobStatus = JobStatus.QUEUED
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
            "status": self.status.value,
            "created_at": self.created_at,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "result": self.result,
            "error": self.error,
        }
