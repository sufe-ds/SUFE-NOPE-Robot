"""API 层：REST 与 MCP 两种交付方式，均依赖服务层。

本层不包含业务逻辑，只做参数校验、调用服务、组织响应。
"""

from .mcp import build_mcp
from .rest import router
from .errors import install_handlers

__all__ = ["build_mcp", "router", "install_handlers"]
