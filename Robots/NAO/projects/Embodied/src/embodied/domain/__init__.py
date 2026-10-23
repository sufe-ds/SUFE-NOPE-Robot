"""领域层：纯业务模型，不依赖任何外层。

本层只包含实体、值对象、领域函数与领域错误，
不导入 ``qi``、FastAPI、pydantic 或任何基础设施。
"""

from .entities import (
    Job,
    Movement,
    MovementInfo,
    MovementResult,
    RobotAddress,
    SpeechResult,
)
from .values import Color, JobStatus
from .errors import (
    ActionTimeoutError,
    ForbiddenCallError,
    JobNotFoundError,
    MotionBusyError,
    RobotCallError,
    RobotError,
    RobotUnreachableError,
    ServiceUnavailableError,
    UnknownMovementError,
    UnknownPostureError,
    UnknownServiceMethodError,
    ValidationError,
)

__all__ = [
    "Job",
    "Movement",
    "MovementInfo",
    "MovementResult",
    "RobotAddress",
    "SpeechResult",
    "Color",
    "JobStatus",
    "RobotError",
    "RobotUnreachableError",
    "ServiceUnavailableError",
    "RobotCallError",
    "UnknownServiceMethodError",
    "UnknownMovementError",
    "UnknownPostureError",
    "MotionBusyError",
    "ForbiddenCallError",
    "ActionTimeoutError",
    "JobNotFoundError",
    "ValidationError",
]
