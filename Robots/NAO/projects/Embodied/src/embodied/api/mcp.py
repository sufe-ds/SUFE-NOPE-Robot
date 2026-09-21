"""MCP 工具：LLM Agent 的语义化入口，依赖服务层。"""

from __future__ import annotations

from typing import Any

from fastmcp import FastMCP
from fastmcp.utilities.types import Image

from ..domain.errors import RobotError


def _error(exc: RobotError) -> dict:
    return {"ok": False, "error": exc.code, "message": exc.message, "detail": exc.detail}


def build_mcp(container: Any) -> FastMCP:
    mcp = FastMCP(
        "NAO Embodied",
        instructions=(
            "操控 NAO 机器人的工具集。会说话、摆姿态、走路、跳舞、看摄像头、听语音、控制 LED。"
            "长动作（dance）会立即返回 job_id，用 get_job 轮询；随时可用 stop 急停。"
        ),
    )

    # -- 状态 --------------------------------------------------------------
    @mcp.tool
    def robot_status() -> dict:
        """查询机器人连接状态、是否唤醒、当前姿态、音量与正在执行的任务。"""
        data = container.gateway.status()
        data["camera"] = container.camera.info()
        current = container.jobs.current()
        data["current_job"] = current.to_dict() if current else None
        try:
            data["volume"] = container.audio.get_volume()
        except RobotError:
            data["volume"] = None
        return data

    # -- 说话 --------------------------------------------------------------
    @mcp.tool
    def say(text: str, language: str = "Chinese", animated: bool = False) -> dict:
        """让 NAO 说话。text 为要说的内容；animated=True 时带肢体语言。"""
        try:
            container.speech.say(text, language=language, animated=animated)
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def stop() -> dict:
        """急停：立刻停止所有运动与说话。任何时刻都可调用。"""
        try:
            container.gateway.stop_all()
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    # -- 姿态与运动 --------------------------------------------------------
    @mcp.tool
    def wake() -> dict:
        """唤醒机器人（运动前需要）。"""
        try:
            container.motion.wake_up()
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def rest() -> dict:
        """让机器人进入休息姿态。"""
        try:
            container.motion.rest()
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def list_postures() -> dict:
        """列出机器人支持的姿态名称。"""
        try:
            return {"postures": container.motion.list_postures()}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def go_to_posture(posture: str, speed: float = 0.5) -> dict:
        """摆到指定姿态（如 Stand / Sit）。speed 取 0-1。"""
        if container.jobs.busy():
            return {"ok": False, "error": "motion_busy", "message": "有动作正在执行"}
        try:
            return {"ok": True, "posture": container.motion.go_to_posture(posture, speed)}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def set_angles(names: list[str], angles: list[float], speed: float = 0.2) -> dict:
        """按关节名设置角度（弧度）。names 与 angles 长度需一致。"""
        if container.jobs.busy():
            return {"ok": False, "error": "motion_busy", "message": "有动作正在执行"}
        try:
            container.motion.set_angles(names, angles, speed)
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def walk(x: float, y: float, theta: float) -> dict:
        """相对移动：x 前后、y 左右、theta 转向（米与弧度）。"""
        if container.jobs.busy():
            return {"ok": False, "error": "motion_busy", "message": "有动作正在执行"}
        try:
            container.motion.move(x, y, theta)
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    # -- 动作 --------------------------------------------------------------
    @mcp.tool
    def list_dances() -> dict:
        """列出可播放的动作/舞蹈名称。"""
        try:
            return {"dances": [info.to_dict() for info in container.movement.list()]}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def dance(name: str, wait: bool = False) -> dict:
        """播放动作/舞蹈。默认立即返回 job_id，用 get_job 轮询进度。"""
        try:
            container.movement.ensure_exists(name)
            if wait:
                return {"ok": True, **container.movement.execute(name).to_dict()}
            job = container.jobs.submit_movement(name)
            return {"ok": True, "job_id": job.id, "status": job.status.value}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def get_job(job_id: str) -> dict:
        """查询动作任务状态：queued/running/done/failed/cancelled。"""
        try:
            return container.jobs.get(job_id).to_dict()
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def cancel_job(job_id: str) -> dict:
        """取消动作任务并急停。"""
        try:
            cancelled = container.jobs.cancel(job_id)
            return {"ok": cancelled, "cancelled": cancelled}
        except RobotError as exc:
            return _error(exc)

    # -- 摄像头 ------------------------------------------------------------
    @mcp.tool
    def look(resolution: int | None = None) -> Any:
        """拍一张机器人摄像头的画面。resolution: 0=160x120,1=320x240,2=640x480,3=1280x960。"""
        try:
            frame = container.camera.snapshot(resolution)
        except RobotError as exc:
            return _error(exc)
        return Image(data=frame, format="jpeg")

    # -- 语音识别 ----------------------------------------------------------
    @mcp.tool
    def listen(
        vocabulary: list[str],
        timeout_s: float = 6.0,
        word_spotting: bool = True,
        language: str = "Chinese",
    ) -> dict:
        """聆听并识别语音，返回识别到的词与置信度。vocabulary 为期望词表。"""
        try:
            return container.speech.listen(
                vocabulary,
                timeout_s=timeout_s,
                word_spotting=word_spotting,
                language=language,
            ).to_dict()
        except RobotError as exc:
            return _error(exc)

    # -- LED / 音量 --------------------------------------------------------
    @mcp.tool
    def set_leds(name: str = "FaceLeds", color: str = "#00A0FF", duration: float = 0.5) -> dict:
        """设置 LED 颜色，color 形如 #RRGGBB。"""
        try:
            container.led.set_leds(name, color, duration)
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def leds_off(name: str = "FaceLeds") -> dict:
        """关闭指定 LED 组。"""
        try:
            container.led.off(name)
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def get_volume() -> dict:
        """查询机器人扬声器音量（0-100）。"""
        try:
            return {"volume": container.audio.get_volume()}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def set_volume(volume: int) -> dict:
        """设置扬声器音量（0-100）。"""
        try:
            return {"ok": True, "volume": container.audio.set_volume(volume)}
        except RobotError as exc:
            return _error(exc)

    # -- 逃生舱 ------------------------------------------------------------
    @mcp.tool
    def call_service(service: str, method: str, args: list | None = None) -> dict:
        """低层逃生舱：调用任意白名单内的 NAOqi 服务方法（需服务端开启）。"""
        try:
            return {"ok": True, "result": container.escape.call(service, method, args)}
        except RobotError as exc:
            return _error(exc)

    return mcp
