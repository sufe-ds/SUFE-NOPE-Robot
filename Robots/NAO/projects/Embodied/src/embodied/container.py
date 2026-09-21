"""组装根（composition root）：把具体实现注入应用服务。

只有这里同时依赖各层；``api`` 与 ``service`` 的应用服务都不知道具体实现。
"""

from __future__ import annotations

from dataclasses import dataclass

from .service import (
    AudioService,
    CameraService,
    EscapeHatchService,
    GatewayService,
    JobService,
    LedService,
    MotionService,
    MovementService,
    SpeechService,
)
from .service.config import Settings
from .service.fake_robot import FakeRobot
from .service.movement_files import FileMovementRepository
from .service.qi_robot import QiRobot
from .service.thread_jobs import ThreadJobQueue
from .service.ports import RobotPort


@dataclass
class Container:
    settings: Settings
    robot: RobotPort
    gateway: GatewayService
    speech: SpeechService
    motion: MotionService
    movement: MovementService
    camera: CameraService
    led: LedService
    audio: AudioService
    escape: EscapeHatchService
    jobs: JobService


def build_container(settings: Settings, robot: RobotPort | None = None) -> Container:
    robot = robot or (FakeRobot(settings) if settings.dry_run else QiRobot(settings))
    movements = FileMovementRepository(settings.movement_dir)
    queue = ThreadJobQueue()

    movement_service = MovementService(movements, robot)
    return Container(
        settings=settings,
        robot=robot,
        gateway=GatewayService(robot),
        speech=SpeechService(robot, default_language=settings.asr_language),
        motion=MotionService(robot),
        movement=movement_service,
        camera=CameraService(robot),
        led=LedService(robot),
        audio=AudioService(robot),
        escape=EscapeHatchService(
            robot, settings.enable_escape_hatch, settings.allowed_services
        ),
        jobs=JobService(queue, movement_service, robot),
    )
