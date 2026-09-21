"""Embodied：分层架构（domain ← service ← api）。"""

from __future__ import annotations

from .service.config import Settings
from .service.qi_robot import connect

__version__ = "0.1.0"

__all__ = ["Settings", "connect", "__version__"]
