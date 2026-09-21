"""把领域错误映射为 HTTP 响应。"""

from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from ..domain.errors import RobotError


def install_handlers(app: FastAPI) -> None:
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
