"""领域错误：业务语义的统一异常，供 API / MCP 映射为响应。"""

from __future__ import annotations

from typing import Any


class RobotError(Exception):
    """所有机器人相关错误的基类。"""

    code = "robot_error"
    status = 500

    def __init__(self, message: str, detail: Any = None) -> None:
        super().__init__(message)
        self.message = message
        self.detail = detail

    def to_dict(self) -> dict:
        return {"error": {"code": self.code, "message": self.message, "detail": self.detail}}


class RobotUnreachableError(RobotError):
    code = "robot_unreachable"
    status = 503


class ServiceUnavailableError(RobotError):
    code = "service_unavailable"
    status = 503


class RobotCallError(RobotError):
    code = "robot_call_failed"
    status = 502


class UnknownServiceMethodError(RobotError):
    code = "unknown_method"
    status = 400


class UnknownMovementError(RobotError):
    code = "unknown_movement"
    status = 404


class UnknownPostureError(RobotError):
    code = "unknown_posture"
    status = 404


class MotionBusyError(RobotError):
    code = "motion_busy"
    status = 409


class ForbiddenCallError(RobotError):
    code = "forbidden_service"
    status = 403


class ActionTimeoutError(RobotError):
    code = "action_timeout"
    status = 504


class JobNotFoundError(RobotError):
    code = "job_not_found"
    status = 404


class ValidationError(RobotError):
    code = "validation_error"
    status = 422
