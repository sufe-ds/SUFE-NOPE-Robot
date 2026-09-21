"""动作仓储的文件系统实现：加载 ``Robots/NAO/movements/*.py``。"""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path
from typing import Any

from ..domain.entities import Movement, MovementInfo
from ..domain.errors import UnknownMovementError
from ..domain.trajectory import flatten
from .ports import MovementRepository

_SAFE_NAME = re.compile(r"^[A-Za-z0-9_]+$")


class FileMovementRepository(MovementRepository):
    def __init__(self, directory: Path | str) -> None:
        self.directory = Path(directory)
        self._modules: dict[Path, tuple[int, Any]] = {}

    # -- 发现 ---------------------------------------------------------------
    def _candidates(self) -> dict[str, Path]:
        if not self.directory.is_dir():
            return {}
        found: dict[str, Path] = {}
        for path in sorted(self.directory.glob("*.py")):
            if path.is_file():
                found[path.stem.lower()] = path
        return found

    def names(self) -> list[str]:
        return sorted(path.stem for path in self._candidates().values())

    def exists(self, name: str) -> bool:
        if not _SAFE_NAME.match(name):
            return False
        return name.lower() in self._candidates()

    def _resolve(self, name: str) -> Path:
        if not _SAFE_NAME.match(name):
            raise UnknownMovementError(f"非法动作名：{name!r}")
        path = self._candidates().get(name.lower())
        if path is None:
            raise UnknownMovementError(f"未知动作：{name}", detail=self.names())
        return path

    def list(self) -> list[MovementInfo]:
        infos: list[MovementInfo] = []
        for path in sorted(self._candidates().values()):
            try:
                infos.append(self.info(path.stem))
            except Exception:  # 单个坏文件不影响整体
                continue
        return infos

    def info(self, name: str) -> MovementInfo:
        path = self._resolve(name)
        posture, time_hint, raw = self._load(path).main()
        return MovementInfo(
            name=path.stem,
            posture=posture or "",
            time_hint=float(time_hint or 0.0),
            joint_count=len(raw),
        )

    def load(self, name: str) -> Movement:
        path = self._resolve(name)
        posture, _time_hint, raw = self._load(path).main()
        names, times, angles = flatten(raw)
        return Movement(
            name=path.stem, posture=posture or "", names=names, times=times, angles=angles
        )

    # -- 加载 ---------------------------------------------------------------
    def _load(self, path: Path):
        mtime = path.stat().st_mtime_ns
        cached = self._modules.get(path)
        if cached is not None and cached[0] == mtime:
            return cached[1]
        spec = importlib.util.spec_from_file_location(
            f"embodied_movements_{path.stem}", path
        )
        if spec is None or spec.loader is None:
            raise UnknownMovementError(f"无法加载动作：{path.name}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self._modules[path] = (mtime, module)
        return module
