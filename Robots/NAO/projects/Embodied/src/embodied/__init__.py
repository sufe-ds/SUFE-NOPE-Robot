"""Embodied —— Agent 可操控的 NAO 具身智能服务。"""

from __future__ import annotations

from .config import Settings
from .robot import Robot, connect

__version__ = "0.1.0"

__all__ = ["Settings", "Robot", "connect", "main", "__version__"]


def main() -> int:
    from .cli import main as _main

    return _main()
