"""运行配置：环境变量 / .env / CLI 覆盖（外部输入，属基础设施）。"""

from __future__ import annotations

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def default_movement_dir() -> Path:
    """默认动作目录：Robots/NAO/movements。

    本文件位于 ``.../projects/Embodied/src/embodied/service/config.py``，
    ``parents[5]`` 即 ``Robots/NAO``。
    """
    return Path(__file__).resolve().parents[5] / "movements"


DEFAULT_ALLOWED_SERVICES = [
    "ALTextToSpeech",
    "ALAnimatedSpeech",
    "ALRobotPosture",
    "ALMotion",
    "ALVideoDevice",
    "ALSpeechRecognition",
    "ALLeds",
    "ALAudioDevice",
    "ALMemory",
    "ALBehaviorManager",
    "ALTabletService",
]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        validate_by_name=True,
    )

    # 机器人（NAOqi）
    nao_ip: str = Field("127.0.0.1", validation_alias="NAO_IP")
    nao_port: int = Field(9559, validation_alias="NAO_PORT")

    # 服务
    host: str = Field("0.0.0.0", validation_alias="EMBODIED_HOST")
    port: int = Field(19559, validation_alias="EMBODIED_PORT")
    mcp_path: str = Field("/mcp", validation_alias="EMBODIED_MCP_PATH")
    api_token: str | None = Field(None, validation_alias="EMBODIED_API_TOKEN")

    # 行为
    dry_run: bool = Field(False, validation_alias="EMBODIED_DRY_RUN")
    movement_dir: Path = Field(
        default_factory=default_movement_dir,
        validation_alias="EMBODIED_MOVEMENTS_DIR",
    )
    action_timeout_s: float = Field(30.0, validation_alias="EMBODIED_ACTION_TIMEOUT_S")
    asr_language: str = Field("Chinese", validation_alias="EMBODIED_ASR_LANGUAGE")
    camera_fps: int = Field(10, validation_alias="EMBODIED_CAMERA_FPS")
    camera_resolution: int = Field(1, validation_alias="EMBODIED_CAMERA_RESOLUTION")

    # 逃生舱
    enable_escape_hatch: bool = Field(
        False, validation_alias="EMBODIED_ENABLE_ESCAPE_HATCH"
    )
    allowed_services: list[str] = Field(
        default_factory=lambda: list(DEFAULT_ALLOWED_SERVICES),
        validation_alias="EMBODIED_ALLOWED_SERVICES",
    )

    log_level: str = Field("INFO", validation_alias="EMBODIED_LOG_LEVEL")
