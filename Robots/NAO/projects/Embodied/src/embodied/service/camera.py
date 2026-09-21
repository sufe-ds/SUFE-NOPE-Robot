"""摄像头服务。"""

from __future__ import annotations

from .ports import RobotPort


class CameraService:
    def __init__(self, robot: RobotPort) -> None:
        self._robot = robot

    def start(self) -> None:
        self._robot.start_camera()

    def stop(self) -> None:
        self._robot.stop_camera()

    def snapshot(self, resolution: int | None = None) -> bytes:
        return self._robot.camera_snapshot(resolution)

    def frame(self) -> bytes | None:
        return self._robot.camera_frame()

    def info(self) -> dict:
        return self._robot.camera_info()
