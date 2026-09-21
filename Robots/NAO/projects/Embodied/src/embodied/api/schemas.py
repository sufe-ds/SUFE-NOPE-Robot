"""REST API 的请求 / 响应模型。"""

from __future__ import annotations

from pydantic import BaseModel, Field


class SayRequest(BaseModel):
    text: str = Field(..., max_length=2000)
    language: str | None = None
    animated: bool = False


class PostureRequest(BaseModel):
    name: str
    speed: float = Field(0.5, gt=0.0, le=1.0)


class AnglesRequest(BaseModel):
    names: list[str]
    angles: list[float]
    speed: float = Field(0.2, gt=0.0, le=1.0)


class MoveRequest(BaseModel):
    x: float = 0.0
    y: float = 0.0
    theta: float = 0.0


class MovementRequest(BaseModel):
    wait: bool = False
    timeout_s: float | None = None


class ListenRequest(BaseModel):
    vocabulary: list[str] = Field(..., min_length=1)
    timeout_s: float = Field(6.0, gt=0.0, le=60.0)
    word_spotting: bool = True
    language: str | None = None
    min_confidence: float = Field(0.0, ge=0.0, le=1.0)


class LedRequest(BaseModel):
    name: str = "FaceLeds"
    color: str = "#00A0FF"
    duration: float = Field(0.5, gt=0.0)


class LedOffRequest(BaseModel):
    name: str = "FaceLeds"


class LedIntensityRequest(BaseModel):
    name: str
    intensity: float = Field(..., ge=0.0, le=1.0)


class RastaRequest(BaseModel):
    duration: float = Field(1.0, gt=0.0)


class VolumeRequest(BaseModel):
    volume: int = Field(..., ge=0, le=100)


class CallRequest(BaseModel):
    service: str
    method: str
    args: list | None = None
