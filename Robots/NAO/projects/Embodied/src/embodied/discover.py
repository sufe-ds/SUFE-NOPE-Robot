"""机器人发现工具：启动服务前确认机器人 IP。

    uv run embodied discover [目标...] [--timeout 0.3] [--json]

扫描不依赖服务进程，因此可以在配置 ``NAO_IP`` 之前使用。
退出码：0 找到候选，1 未找到，2 参数或网络错误。
"""

from __future__ import annotations

import argparse
import json
import sys

from .domain.errors import RobotError
from .service.config import Settings
from .service.discovery import DiscoveryService
from .service.network_scan import SubnetRobotLocator


def add_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "targets",
        nargs="*",
        metavar="目标",
        help="IP 或 CIDR 列表，省略则扫描本机网段与 NAO_IP 所在网段",
    )
    parser.add_argument(
        "--timeout", type=float, default=0.3, metavar="秒", help="单地址探测超时，默认 0.3"
    )
    parser.add_argument("--json", action="store_true", help="输出完整 JSON")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m embodied.discover",
        description="扫描局域网中的 NAO 机器人（并发探测 NAOqi 端口）。",
    )
    add_arguments(parser)
    return parser


def configure_stdio() -> None:
    """Windows 重定向时默认走 ANSI 代码页，统一成 UTF-8 便于 Agent 读取。"""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def run(args: argparse.Namespace, service: DiscoveryService | None = None) -> int:
    if service is None:
        settings = Settings()
        service = DiscoveryService(
            SubnetRobotLocator(settings.nao_port), settings.nao_ip, settings.nao_port
        )

    try:
        result = service.scan(args.targets or None, args.timeout)
    except RobotError as exc:
        print(f"扫描失败：{exc.message}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        _report(result)
    return 0 if result["robots"] else 1


def _report(result: dict) -> None:
    robots = result["robots"]
    targets = ", ".join(result["targets"]) or "无可用网段"
    print(
        f"扫描 {targets}，用时 {result['elapsed_s']}s，"
        f"发现 {len(robots)} 个候选（端口开放不等于一定是 NAO）"
    )
    for robot in robots:
        name = robot["name"] or "-"
        mark = "  (当前 NAO_IP)" if robot["configured"] else ""
        print(f"  {robot['ip']}:{robot['port']}  {name}{mark}")
    if not robots:
        print("未找到开放的 NAOqi 端口。请确认机器人已开机、与本机同网段；")
        print("若本机是容器或 WSL NAT 网段，请显式传入机器人所在网段。")


def main(argv: list[str] | None = None, service: DiscoveryService | None = None) -> int:
    configure_stdio()
    return run(build_parser().parse_args(argv), service)


if __name__ == "__main__":
    raise SystemExit(main())
