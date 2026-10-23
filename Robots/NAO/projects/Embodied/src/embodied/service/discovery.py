"""机器人发现服务：整理扫描范围、标出当前配置的机器人。"""

from __future__ import annotations

import ipaddress
import time

from ..domain.entities import RobotAddress
from .ports import RobotLocator


class DiscoveryService:
    def __init__(
        self, locator: RobotLocator, configured_ip: str, configured_port: int = 9559
    ) -> None:
        self._locator = locator
        self._configured_ip = configured_ip.strip()
        self._configured_port = configured_port

    def default_targets(self) -> list[str]:
        """本机各网段 + 当前配置 IP 所在网段。

        WSL 下本机地址通常是 NAT 虚拟网段，因此再按配置 IP 猜一个 /24，
        用户换过机器人 IP 但仍在同一网段时无需再传参数。
        """
        targets = self._locator.local_subnets()
        try:
            configured = ipaddress.ip_address(self._configured_ip)
        except ValueError:
            return targets
        if (
            configured.version != 4
            or configured.is_loopback
            or configured.is_unspecified
        ):
            return targets
        subnet = str(ipaddress.ip_network(f"{configured}/24", strict=False))
        if subnet not in targets:
            targets.append(subnet)
        return targets

    def scan(
        self, targets: list[str] | None = None, timeout_s: float = 0.3
    ) -> dict:
        hosts = [
            item.strip()
            for item in (targets or self.default_targets())
            if item.strip()
        ]
        started = time.perf_counter()
        robots = self._locator.scan(hosts, timeout_s)
        return {
            "configured_ip": self._configured_ip,
            "targets": hosts,
            "elapsed_s": round(time.perf_counter() - started, 3),
            "robots": [self._view(robot) for robot in robots],
        }

    def _view(self, robot: RobotAddress) -> dict:
        data = robot.to_dict()
        data["configured"] = (
            robot.ip == self._configured_ip and robot.port == self._configured_port
        )
        return data
