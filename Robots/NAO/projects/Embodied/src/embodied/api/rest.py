"""REST 路由：依赖服务层，不直接接触基础设施。"""

from __future__ import annotations

import asyncio
from typing import Any

from fastapi import APIRouter, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import Response, StreamingResponse

from ..domain.errors import MotionBusyError, RobotError, RobotUnreachableError
from . import schemas

router = APIRouter()
_MJPEG_BOUNDARY = "frame"


def _container(request: Request) -> Any:
    container = getattr(request.app.state, "container", None)
    if container is None:
        raise RobotUnreachableError("机器人未初始化")
    return container


def _ensure_idle(request: Request) -> None:
    if _container(request).jobs.busy():
        raise MotionBusyError("有动作正在执行，请先停止或等待完成")


# -- 健康与状态 ------------------------------------------------------------
@router.get("/health")
def health(request: Request) -> dict:
    container = getattr(request.app.state, "container", None)
    if container is None:
        return {"status": "ok", "robot": {"connected": False}}
    try:
        status = container.gateway.status()
        if not container.gateway.connected():
            container.gateway.connect()
            status = container.gateway.status()
        return {"status": "ok", "robot": status}
    except RobotError as exc:
        return {"status": "degraded", "robot": {"connected": False, "error": exc.message}}


@router.get("/api/robot/status")
def robot_status(request: Request) -> dict:
    container = _container(request)
    data = container.gateway.status()
    data["camera"] = container.camera.info()
    current = container.jobs.current()
    data["current_job"] = current.to_dict() if current else None
    try:
        data["volume"] = container.audio.get_volume()
    except RobotError:
        data["volume"] = None
    return data


# -- 说话 ------------------------------------------------------------------
@router.post("/api/robot/say")
def say(request: Request, body: schemas.SayRequest) -> dict:
    _container(request).speech.say(body.text, language=body.language, animated=body.animated)
    return {"ok": True, "text": body.text}


@router.post("/api/robot/stop")
def stop(request: Request) -> dict:
    _container(request).gateway.stop_all()
    return {"ok": True}


# -- 姿态与运动 ------------------------------------------------------------
@router.post("/api/robot/wake")
def wake(request: Request) -> dict:
    _ensure_idle(request)
    _container(request).motion.wake_up()
    return {"ok": True, "awake": True}


@router.post("/api/robot/rest")
def rest(request: Request) -> dict:
    _ensure_idle(request)
    _container(request).motion.rest()
    return {"ok": True, "awake": False}


@router.get("/api/robot/postures")
def postures(request: Request) -> dict:
    return {"postures": _container(request).motion.list_postures()}


@router.post("/api/robot/posture")
def go_to_posture(request: Request, body: schemas.PostureRequest) -> dict:
    _ensure_idle(request)
    name = _container(request).motion.go_to_posture(body.name, body.speed)
    return {"ok": True, "posture": name}


@router.post("/api/robot/angles")
def set_angles(request: Request, body: schemas.AnglesRequest) -> dict:
    _ensure_idle(request)
    _container(request).motion.set_angles(body.names, body.angles, body.speed)
    return {"ok": True}


@router.post("/api/robot/move")
def move(request: Request, body: schemas.MoveRequest) -> dict:
    _ensure_idle(request)
    _container(request).motion.move(body.x, body.y, body.theta)
    return {"ok": True}


# -- 动作 ------------------------------------------------------------------
@router.get("/api/movements")
def list_movements(request: Request) -> dict:
    infos = _container(request).movement.list()
    return {"movements": [info.to_dict() for info in infos]}


@router.post("/api/movements/{name}", status_code=202)
def start_movement(request: Request, name: str, body: schemas.MovementRequest):
    container = _container(request)
    container.movement.ensure_exists(name)  # 未知动作直接 404
    if body.wait:
        return {"ok": True, **container.movement.execute(name).to_dict()}
    job = container.jobs.submit_movement(name)
    return {"job_id": job.id, "name": name, "status": job.status.value}


@router.get("/api/jobs")
def list_jobs(request: Request) -> dict:
    return {"jobs": [job.to_dict() for job in _container(request).jobs.list()]}


@router.get("/api/jobs/{job_id}")
def get_job(request: Request, job_id: str) -> dict:
    return _container(request).jobs.get(job_id).to_dict()


@router.delete("/api/jobs/{job_id}")
def cancel_job(request: Request, job_id: str) -> dict:
    cancelled = _container(request).jobs.cancel(job_id)
    return {"ok": cancelled, "cancelled": cancelled}


# -- 摄像头 ----------------------------------------------------------------
@router.get("/api/camera/info")
def camera_info(request: Request) -> dict:
    return _container(request).camera.info()


@router.get("/api/camera/snapshot")
def camera_snapshot(request: Request, resolution: int | None = None) -> Response:
    frame = _container(request).camera.snapshot(resolution)
    return Response(content=frame, media_type="image/jpeg")


@router.get("/api/camera/mjpeg")
async def camera_mjpeg(request: Request, resolution: int | None = None) -> StreamingResponse:
    container = _container(request)
    await run_in_threadpool(container.camera.start)
    interval = 1.0 / max(1, container.settings.camera_fps)

    async def generate():
        while True:
            if await request.is_disconnected():
                break
            frame = await run_in_threadpool(container.camera.frame)
            if frame:
                yield (
                    f"--{_MJPEG_BOUNDARY}\r\n"
                    f"Content-Type: image/jpeg\r\n"
                    f"Content-Length: {len(frame)}\r\n\r\n"
                ).encode() + frame + b"\r\n"
            await asyncio.sleep(interval)

    return StreamingResponse(
        generate(),
        media_type=f"multipart/x-mixed-replace; boundary={_MJPEG_BOUNDARY}",
    )


# -- 语音识别 --------------------------------------------------------------
@router.post("/api/asr/listen")
def listen(request: Request, body: schemas.ListenRequest) -> dict:
    result = _container(request).speech.listen(
        body.vocabulary,
        timeout_s=body.timeout_s,
        word_spotting=body.word_spotting,
        language=body.language,
        min_confidence=body.min_confidence,
    )
    return result.to_dict()


# -- LED / 音量 ------------------------------------------------------------
@router.post("/api/leds")
def set_leds(request: Request, body: schemas.LedRequest) -> dict:
    _container(request).led.set_leds(body.name, body.color, body.duration)
    return {"ok": True}


@router.post("/api/leds/off")
def leds_off(request: Request, body: schemas.LedOffRequest) -> dict:
    _container(request).led.off(body.name)
    return {"ok": True}


@router.post("/api/leds/intensity")
def leds_intensity(request: Request, body: schemas.LedIntensityRequest) -> dict:
    _container(request).led.set_intensity(body.name, body.intensity)
    return {"ok": True}


@router.post("/api/leds/rasta")
def leds_rasta(request: Request, body: schemas.RastaRequest) -> dict:
    _container(request).led.rasta(body.duration)
    return {"ok": True}


@router.get("/api/volume")
def get_volume(request: Request) -> dict:
    return {"volume": _container(request).audio.get_volume()}


@router.post("/api/volume")
def set_volume(request: Request, body: schemas.VolumeRequest) -> dict:
    return {"ok": True, "volume": _container(request).audio.set_volume(body.volume)}


# -- 逃生舱 ----------------------------------------------------------------
@router.post("/api/call")
def call_service(request: Request, body: schemas.CallRequest) -> dict:
    result = _container(request).escape.call(body.service, body.method, body.args)
    return {"ok": True, "result": result}
