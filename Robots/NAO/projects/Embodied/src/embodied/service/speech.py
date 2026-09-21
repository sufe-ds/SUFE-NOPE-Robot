"""说话与语音识别服务。"""

from __future__ import annotations

from ..domain.entities import SpeechResult
from .ports import RobotPort


class SpeechService:
    def __init__(self, robot: RobotPort, default_language: str = "Chinese") -> None:
        self._robot = robot
        self._default_language = default_language

    def say(self, text: str, language: str | None = None, animated: bool = False) -> None:
        self._robot.say(text, language or self._default_language, animated)

    def stop(self) -> None:
        self._robot.stop_speaking()

    def listen(
        self,
        vocabulary: list[str],
        timeout_s: float = 6.0,
        word_spotting: bool = True,
        language: str | None = None,
        min_confidence: float = 0.0,
    ) -> SpeechResult:
        return self._robot.listen(
            vocabulary,
            timeout_s=timeout_s,
            word_spotting=word_spotting,
            language=language or self._default_language,
            min_confidence=min_confidence,
        )
