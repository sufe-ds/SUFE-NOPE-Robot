"""低层逃生舱服务：白名单/黑名单策略在这里，而非基础设施。"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..domain.errors import ForbiddenCallError
from .ports import RobotPort

_DENY_METHODS = {"shutdown", "reboot", "restart", "system"}


def _is_denied(method: str) -> bool:
    lowered = str(method).lower()
    return lowered in _DENY_METHODS or "unregister" in lowered


class EscapeHatchService:
    def __init__(
        self,
        robot: RobotPort,
        enabled: bool = False,
        allowed_services: Sequence[str] = (),
    ) -> None:
        self._robot = robot
        self._enabled = enabled
        self._allowed = tuple(allowed_services)

    def call(self, service: str, method: str, args: list | None = None) -> Any:
        if not self._enabled:
            raise ForbiddenCallError(
                "逃生舱未启用（设置 EMBODIED_ENABLE_ESCAPE_HATCH=1 开启）"
            )
        if "*" not in self._allowed and service not in self._allowed:
            raise ForbiddenCallError(f"服务 {service} 不在白名单", detail=list(self._allowed))
        if _is_denied(method):
            raise ForbiddenCallError(f"方法 {method} 被禁止")
        return self._robot.call_service(service, method, args)
