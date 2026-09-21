"""动作模块加载与展平。

``Robots/NAO/movements/*.py`` 是 LabVIEW 导出的纯数据模块：
每个文件定义 ``main() -> (Posture, time, movements)``，无副作用。
本模块负责安全地按名字加载、缓存，并展平成
``ALMotion.angleInterpolationBezier(names, times, angles)`` 所需的参数。
"""

from __future__ import annotations

import importlib.util
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import UnknownMovementError

_SAFE_NAME = re.compile(r"^[A-Za-z0-9_]+$")


@dataclass(frozen=True)
class MovementInfo:
    name: str
    posture: str
    time_hint: float
    joint_count: int


def flatten(
    movements: list,
) -> tuple[list[str], list[list[float]], list[list[list[float]]]]:
    """把 ``[joint, [[t, angle, h_in, h_out], ...]]`` 展平为三个平行列表。

    与 ``projects/jinan_cstp/touch_stop_move1.py:59-71`` 的逻辑一致。
    """
    names: list[str] = []
    times: list[list[float]] = []
    angles: list[list[list[float]]] = []
    for joint in movements:
        names.append(joint[0])
        keyframes = joint[1]
        times.append([float(kf[0]) for kf in keyframes])
        angles.append([[float(kf[1]), kf[2], kf[3]] for kf in keyframes])
    return names, times, angles


class MovementLibrary:
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

    def resolve(self, name: str) -> Path:
        if not _SAFE_NAME.match(name):
            raise UnknownMovementError(f"非法动作名：{name!r}")
        path = self._candidates().get(name.lower())
        if path is None:
            raise UnknownMovementError(f"未知动作：{name}", detail=self.names())
        return path

    def info(self, name: str) -> MovementInfo:
        path = self.resolve(name)
        posture, time_hint, movements = self._load(path).main()
        return MovementInfo(
            name=path.stem,
            posture=posture or "",
            time_hint=float(time_hint or 0.0),
            joint_count=len(movements),
        )

    def list(self) -> list[MovementInfo]:
        infos: list[MovementInfo] = []
        for path in sorted(self._candidates().values()):
            try:
                infos.append(self.info(path.stem))
            except Exception:  # 单个坏文件不应影响整个列表
                continue
        return infos

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

    def prepare(
        self, name: str
    ) -> tuple[str, list[str], list[list[float]], list[list[list[float]]]]:
        result = self._load(self.resolve(name)).main()
        posture, movements = result[0], result[2]
        names, times, angles = flatten(movements)
        return posture or "", names, times, angles
