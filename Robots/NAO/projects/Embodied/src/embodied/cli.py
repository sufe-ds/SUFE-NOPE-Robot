"""命令行入口：``uv run embodied <命令>``。

目前只有 discover：机器人发现必须在服务启动前完成，其余能力走 REST / MCP。
"""

from __future__ import annotations

import argparse

from . import __version__
from .discover import add_arguments, configure_stdio, run
from .service.discovery import DiscoveryService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="embodied", description="NAO 具身智能交互")
    parser.add_argument("--version", action="version", version=__version__)
    commands = parser.add_subparsers(dest="command", required=True)
    discover = commands.add_parser(
        "discover",
        help="扫描局域网中的 NAO 机器人",
        description="扫描局域网中的 NAO 机器人（并发探测 NAOqi 端口）。",
    )
    add_arguments(discover)
    return parser


def main(argv: list[str] | None = None, service: DiscoveryService | None = None) -> int:
    configure_stdio()
    args = build_parser().parse_args(argv)
    return run(args, service)


if __name__ == "__main__":
    raise SystemExit(main())
