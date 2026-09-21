"""FastAPI REST 路由。"""

from __future__ import annotations

import asyncio

from fastapi import APIRouter, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import Response, StreamingResponse

from . import models
from .errors import MotionBusyError, RobotError, RobotUnreachableError
from .robot import Robot

router = APIRouter()

_MJPEG_BOUNDARY = "frame"


def get_robot(request: Request) -> Robot:
    robot = getattr(request.app.state, "robot", None)
    if robot is None:
        raise RobotUnreachableError("机器人未初始化")
    return robot


def _ensure_idle(request: Request) -> None:
    if request.app.state.runner.busy():
        raise MotionBusyError("有动作正在执行，请先停止或等待完成")


# -- 健康与状态 ------------------------------------------------------------
@router.get("/health")
def health(request: Request) -> dict:
    robot = getattr(request.app.state, "robot", None)
    info = {"status": "ok", "robot": {"connected": False}}
    if robot is not None:
        try:
            info["robot"] = {
                "connected": robot.connected,
                "ip": robot.settings.nao_ip,
                "port": robot.settings.nao_port,
            }
            if not robot.connected:
                robot.connect()
                info["robot"]["connected"] = True
        except RobotError as exc:
            info["status"] = "degraded"
            info["robot"] = {"connected": False, "error": exc.message}
    return info


@router.get("/api/robot/status")
def robot_status(request: Request) -> dict:
    robot = get_robot(request)
    data = robot.status()
    data["camera"] = robot.camera_info()
    current = request.app.state.runner.current()
    data["current_job"] = current.to_dict() if current else None
    try:
        data["volume"] = robot.get_volume()
    except RobotError:
        data["volume"] = None
    return data


# -- 说话 ------------------------------------------------------------------
@router.post("/api/robot/say")
def say(request: Request, body: models.SayRequest) -> dict:
    robot = get_robot(request)
    robot.say(body.text, language=body.language, animated=body.animated)
    return {"ok": True, "text": body.text}


@router.post("/api/robot/stop")
def stop(request: Request) -> dict:
    robot = get_robot(request)
    robot.stop_all()
    return {"ok": True}


# -- 姿态与运动 ------------------------------------------------------------
@router.post("/api/robot/wake")
def wake(request: Request) -> dict:
    _ensure_idle(request)
    get_robot(request).wake_up()
    return {"ok": True, "awake": True}


@router.post("/api/robot/rest")
def rest(request: Request) -> dict:
    _ensure_idle(request)
    get_robot(request).rest()
    return {"ok": True, "awake": False}


@router.get("/api/robot/postures")
def postures(request: Request) -> dict:
    return {"postures": get_robot(request).list_postures()}


@router.post("/api/robot/posture")
def go_to_posture(request: Request, body: models.PostureRequest) -> dict:
    _ensure_idle(request)
    name = get_robot(request).go_to_posture(body.name, body.speed)
    return {"ok": True, "posture": name}


@router.post("/api/robot/angles")
def set_angles(request: Request, body: models.AnglesRequest) -> dict:
    _ensure_idle(request)
    get_robot(request).set_angles(body.names, body.angles, body.speed)
    return {"ok": True}


@router.post("/api/robot/move")
def move(request: Request, body: models.MoveRequest) -> dict:
    _ensure_idle(request)
    get_robot(request).move(body.x, body.y, body.theta)
    return {"ok": True}


# -- 动作 ------------------------------------------------------------------
@router.get("/api/movements")
def list_movements(request: Request) -> dict:
    infos = get_robot(request).list_movements()
    return {"movements": [info.__dict__ for info in infos]}


@router.post("/api/movements/{name}", status_code=202)
def start_movement(request: Request, name: str, body: models.MovementRequest):
    robot = get_robot(request)
    robot.movements.resolve(name)  # 提前校验，未知动作直接 404
    if body.wait:
        result = robot.play_movement(name)
        return {"ok": True, **result.to_dict()}
    job = request.app.state.runner.submit(
        "movement", name, lambda: robot.play_movement(name).to_dict()
    )
    return {"job_id": job.id, "name": name, "status": job.status}


@router.get("/api/jobs")
def list_jobs(request: Request) -> dict:
    return {"jobs": [job.to_dict() for job in request.app.state.runner.list()]}


@router.get("/api/jobs/{job_id}")
def get_job(request: Request, job_id: str) -> dict:
    return request.app.state.runner.get(job_id).to_dict()


@router.delete("/api/jobs/{job_id}")
def cancel_job(request: Request, job_id: str) -> dict:
    robot = get_robot(request)
    cancelled = request.app.state.runner.cancel(job_id, on_cancel=robot.stop_all)
    return {"ok": cancelled, "cancelled": cancelled}


# -- 摄像头 ----------------------------------------------------------------
@router.get("/api/camera/info")
def camera_info(request: Request) -> dict:
    return get_robot(request).camera_info()


@router.get("/api/camera/snapshot")
def camera_snapshot(request: Request, resolution: int | None = None) -> Response:
    frame = get_robot(request).camera_snapshot(resolution)
    return Response(content=frame, media_type="image/jpeg")


@router.get("/api/camera/mjpeg")
async def camera_mjpeg(request: Request, resolution: int | None = None) -> StreamingResponse:
    robot = get_robot(request)
    await run_in_threadpool(robot.start_camera)

    async def generate():
        interval = 1.0 / max(1, robot.settings.camera_fps)
        while True:
            if await request.is_disconnected():
                break
            frame = await run_in_threadpool(robot.camera_frame)
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
def listen(request: Request, body: models.ListenRequest) -> dict:
    result = get_robot(request).listen(
        body.vocabulary,
        timeout_s=body.timeout_s,
        word_spotting=body.word_spotting,
        language=body.language,
        min_confidence=body.min_confidence,
    )
    return result.to_dict()


# -- LED / 音量 ------------------------------------------------------------
@router.post("/api/leds")
def set_leds(request: Request, body: models.LedRequest) -> dict:
    get_robot(request).set_leds(body.name, body.color, body.duration)
    return {"ok": True}


@router.post("/api/leds/off")
def leds_off(request: Request, body: models.LedOffRequest) -> dict:
    get_robot(request).leds_off(body.name)
    return {"ok": True}


@router.post("/api/leds/intensity")
def leds_intensity(request: Request, body: models.LedIntensityRequest) -> dict:
    get_robot(request).set_led_intensity(body.name, body.intensity)
    return {"ok": True}


@router.post("/api/leds/rasta")
def leds_rasta(request: Request, body: models.RastaRequest) -> dict:
    get_robot(request).rasta(body.duration)
    return {"ok": True}


@router.get("/api/volume")
def get_volume(request: Request) -> dict:
    return {"volume": get_robot(request).get_volume()}


@router.post("/api/volume")
def set_volume(request: Request, body: models.VolumeRequest) -> dict:
    value = get_robot(request).set_volume(body.volume)
    return {"ok": True, "volume": value}


# -- 逃生舱 ----------------------------------------------------------------
@router.post("/api/call")
def call_service(request: Request, body: models.CallRequest) -> dict:
    result = get_robot(request).call_service(body.service, body.method, body.args)
    return {"ok": True, "result": result}
