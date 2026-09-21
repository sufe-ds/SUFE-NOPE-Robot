"""命令行入口：一次性说话（兼容旧版）或启动服务。"""

from __future__ import annotations

import argparse
import os
import sys

from .config import Settings
from .robot import connect


def _one_shot(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="embodied", description="NAO 具身智能交互")
    parser.add_argument("--ip", default=os.environ.get("NAO_IP", "127.0.0.1"))
    parser.add_argument(
        "--port", type=int, default=int(os.environ.get("NAO_PORT", "9559"))
    )
    parser.add_argument("--say", default="你好，我是 Embodied")
    args = parser.parse_args(argv)

    session = connect(args.ip, args.port)
    tts = session.service("ALTextToSpeech")
    tts.setLanguage("Chinese")
    tts.say(args.say)
    return 0


def _serve(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="embodied serve", description="启动 FastAPI + MCP 服务"
    )
    parser.add_argument("serve", nargs="?", help=argparse.SUPPRESS)
    parser.add_argument("--ip", default=None, help="机器人 IP")
    parser.add_argument("--port", type=int, default=None, help="机器人 NAOqi 端口")
    parser.add_argument("--host", default=None, help="服务监听地址")
    parser.add_argument("--http-port", type=int, default=None, help="服务监听端口")
    parser.add_argument("--dry-run", action="store_true", help="不连接机器人，使用假实现")
    args = parser.parse_args(argv)

    overrides: dict = {}
    if args.ip:
        overrides["nao_ip"] = args.ip
    if args.port:
        overrides["nao_port"] = args.port
    if args.host:
        overrides["host"] = args.host
    if args.http_port:
        overrides["port"] = args.http_port
    if args.dry_run:
        overrides["dry_run"] = True
    settings = Settings(**overrides)

    import logging

    import uvicorn

    from .app import create_app

    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO)
    )

    robot = None
    if settings.dry_run:
        from .fake import FakeRobot

        robot = FakeRobot(settings)

    app = create_app(settings, robot=robot)
    uvicorn.run(app, host=settings.host, port=settings.port, log_level=settings.log_level.lower())
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args and args[0] == "serve":
        return _serve(args)
    return _one_shot(args)
