"""应用装配：FastAPI + MCP（组装根，可依赖所有层）。"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastmcp.utilities.lifespan import combine_lifespans

from . import __version__
from .api import build_mcp, install_handlers, router
from .container import Container, build_container
from .domain.errors import RobotError
from .service.config import Settings


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


def create_app(
    settings: Settings | None = None, container: Container | None = None
) -> FastAPI:
    settings = settings or Settings()
    container = container or build_container(settings)

    @asynccontextmanager
    async def app_lifespan(app: FastAPI):
        if not settings.dry_run:
            try:
                container.gateway.connect()
            except RobotError:
                pass  # 允许先起服务，连不上时端点返回 503
        app.state.container = container
        app.state.settings = settings
        try:
            yield
        finally:
            container.gateway.disconnect()

    mcp = build_mcp(container)
    mcp_app = mcp.http_app(path="/")

    app = FastAPI(
        title="NAO Embodied",
        version=__version__,
        lifespan=combine_lifespans(app_lifespan, mcp_app.lifespan),
    )
    _install_auth(app, settings)
    install_handlers(app)
    app.include_router(router)
    app.mount(settings.mcp_path, mcp_app)

    app.state.container = container
    app.state.settings = settings
    return app


app = create_app()
