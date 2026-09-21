"""组装 FastAPI + MCP 应用。"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastmcp.utilities.lifespan import combine_lifespans

from . import __version__
from .api import router
from .config import Settings
from .errors import RobotError
from .jobs import ActionRunner
from .mcp_server import build_mcp
from .robot import Robot


def _install_auth(app: FastAPI, settings: Settings) -> None:
    token = settings.api_token
    if not token:
        return

    @app.middleware("http")
    async def auth(request: Request, call_next):
        if request.url.path == "/health" or request.method == "OPTIONS":
            return await call_next(request)
        if request.headers.get("authorization") != f"Bearer {token}":
            return JSONResponse(
                {
                    "error": {
                        "code": "unauthorized",
                        "message": "缺少或错误的访问令牌",
                        "detail": None,
                    }
                },
                status_code=401,
            )
        return await call_next(request)


def _install_handlers(app: FastAPI) -> None:
    @app.exception_handler(RobotError)
    async def robot_error_handler(request: Request, exc: RobotError) -> JSONResponse:
        return JSONResponse(exc.to_dict(), status_code=exc.status)

    @app.exception_handler(RequestValidationError)
    async def validation_handler(
        request: Request, exc: RequestValidationError
    ) -> JSONResponse:
        return JSONResponse(
            {
                "error": {
                    "code": "validation_error",
                    "message": "请求参数不合法",
                    "detail": jsonable_encoder(exc.errors()),
                }
            },
            status_code=422,
        )


def create_app(settings: Settings | None = None, robot: Robot | None = None) -> FastAPI:
    settings = settings or Settings()
    runner = ActionRunner()
    holder: dict = {"robot": robot}

    @asynccontextmanager
    async def app_lifespan(app: FastAPI):
        instance = holder.get("robot")
        if instance is None:
            instance = Robot(settings)
            if not settings.dry_run:
                try:
                    instance.connect()
                except RobotError:
                    pass  # 允许先起服务，连不上时端点返回 503
            holder["robot"] = instance
        app.state.robot = instance
        app.state.runner = runner
        app.state.settings = settings
        try:
            yield
        finally:
            instance.disconnect()

    mcp = build_mcp(lambda: holder["robot"], lambda: runner, settings)
    mcp_app = mcp.http_app(path="/")

    app = FastAPI(
        title="NAO Embodied",
        version=__version__,
        lifespan=combine_lifespans(app_lifespan, mcp_app.lifespan),
    )
    _install_auth(app, settings)
    _install_handlers(app)
    app.include_router(router)
    app.mount(settings.mcp_path, mcp_app)

    app.state.settings = settings
    app.state.runner = runner
    if robot is not None:
        app.state.robot = robot
    return app


app = create_app()
