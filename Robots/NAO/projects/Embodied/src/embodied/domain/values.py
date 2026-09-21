"""领域值对象。"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .errors import ValidationError


class JobStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass(frozen=True)
class Color:
    """RGB 颜色值对象，内部以 0xRRGGBB 整数保存。"""

    value: int

    @classmethod
    def parse(cls, raw: str | int) -> "Color":
        if isinstance(raw, bool):
            raise ValidationError(f"非法颜色：{raw!r}")
        if isinstance(raw, int):
            return cls(raw & 0xFFFFFF)
        text = str(raw).strip().lstrip("#")
        if text.lower().startswith("0x"):
            text = text[2:]
        if len(text) == 3:
            text = "".join(ch * 2 for ch in text)
        if len(text) != 6:
            raise ValidationError(f"非法颜色：{raw!r}")
        try:
            return cls(int(text, 16))
        except ValueError as exc:
            raise ValidationError(f"非法颜色：{raw!r}") from exc

    def to_int(self) -> int:
        return self.value
