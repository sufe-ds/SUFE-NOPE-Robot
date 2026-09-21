"""FastMCP 工具集：LLM Agent 的语义化入口。

工具直接调用同进程的 ``Robot``（不开第二个进程、不引入第二套锁）。
所有会阻塞的机器人调用都是同步函数，FastMCP 默认在线程池中运行它们。
"""

from __future__ import annotations

from typing import Any, Callable

from fastmcp import FastMCP
from fastmcp.utilities.types import Image

from .errors import RobotError


def _error(exc: RobotError) -> dict:
    return {
        "ok": False,
        "error": exc.code,
        "message": exc.message,
        "detail": exc.detail,
    }


def build_mcp(
    get_robot: Callable[[], Any],
    get_runner: Callable[[], Any],
    settings: Any = None,
) -> FastMCP:
    mcp = FastMCP(
        "NAO Embodied",
        instructions=(
            "操控 NAO 机器人的工具集。会说话、摆姿态、走路、跳舞、看摄像头、听语音、控制 LED。"
            "长动作（dance）会立即返回 job_id，用 get_job 轮询；随时可用 stop 急停。"
        ),
    )

    def _robot():
        return get_robot()

    def _busy() -> bool:
        return get_runner().busy()

    # -- 状态 --------------------------------------------------------------
    @mcp.tool
    def robot_status() -> dict:
        """查询机器人连接状态、是否唤醒、当前姿态、音量与正在执行的任务。"""
        robot = _robot()
        data = robot.status()
        data["camera"] = robot.camera_info()
        current = get_runner().current()
        data["current_job"] = current.to_dict() if current else None
        try:
            data["volume"] = robot.get_volume()
        except RobotError:
            data["volume"] = None
        return data

    # -- 说话 --------------------------------------------------------------
    @mcp.tool
    def say(text: str, language: str = "Chinese", animated: bool = False) -> dict:
        """让 NAO 说话。text 为要说的内容；animated=True 时带肢体语言。"""
        try:
            _robot().say(text, language=language, animated=animated)
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def stop() -> dict:
        """急停：立刻停止所有运动与说话。任何时刻都可调用。"""
        try:
            _robot().stop_all()
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    # -- 姿态与运动 --------------------------------------------------------
    @mcp.tool
    def wake() -> dict:
        """唤醒机器人（运动前需要）。"""
        try:
            _robot().wake_up()
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def rest() -> dict:
        """让机器人进入休息姿态。"""
        try:
            _robot().rest()
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def list_postures() -> dict:
        """列出机器人支持的姿态名称。"""
        try:
            return {"postures": _robot().list_postures()}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def go_to_posture(posture: str, speed: float = 0.5) -> dict:
        """摆到指定姿态（如 Stand / Sit）。speed 取 0-1。"""
        if _busy():
            return {"ok": False, "error": "motion_busy", "message": "有动作正在执行"}
        try:
            name = _robot().go_to_posture(posture, speed)
            return {"ok": True, "posture": name}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def set_angles(names: list[str], angles: list[float], speed: float = 0.2) -> dict:
        """按关节名设置角度（弧度）。names 与 angles 长度需一致。"""
        if _busy():
            return {"ok": False, "error": "motion_busy", "message": "有动作正在执行"}
        try:
            _robot().set_angles(names, angles, speed)
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def walk(x: float, y: float, theta: float) -> dict:
        """相对移动：x 前后、y 左右、theta 转向（米与弧度）。"""
        if _busy():
            return {"ok": False, "error": "motion_busy", "message": "有动作正在执行"}
        try:
            _robot().move(x, y, theta)
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    # -- 动作 --------------------------------------------------------------
    @mcp.tool
    def list_dances() -> dict:
        """列出可播放的动作/舞蹈名称。"""
        try:
            infos = _robot().list_movements()
            return {"dances": [info.__dict__ for info in infos]}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def dance(name: str, wait: bool = False) -> dict:
        """播放动作/舞蹈。默认立即返回 job_id，用 get_job 轮询进度。"""
        robot = _robot()
        try:
            robot.movements.resolve(name)
        except RobotError as exc:
            return _error(exc)
        if wait:
            try:
                return {"ok": True, **robot.play_movement(name).to_dict()}
            except RobotError as exc:
                return _error(exc)
        job = get_runner().submit(
            "movement", name, lambda: robot.play_movement(name).to_dict()
        )
        return {"ok": True, "job_id": job.id, "status": job.status}

    @mcp.tool
    def get_job(job_id: str) -> dict:
        """查询动作任务状态：queued/running/done/failed/cancelled。"""
        try:
            return get_runner().get(job_id).to_dict()
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def cancel_job(job_id: str) -> dict:
        """取消动作任务并急停。"""
        try:
            cancelled = get_runner().cancel(job_id, on_cancel=_robot().stop_all)
            return {"ok": cancelled, "cancelled": cancelled}
        except RobotError as exc:
            return _error(exc)

    # -- 摄像头 ------------------------------------------------------------
    @mcp.tool
    def look(resolution: int | None = None) -> Any:
        """拍一张机器人摄像头的画面。resolution: 0=160x120,1=320x240,2=640x480,3=1280x960。"""
        try:
            frame = _robot().camera_snapshot(resolution)
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
            result = _robot().listen(
                vocabulary,
                timeout_s=timeout_s,
                word_spotting=word_spotting,
                language=language,
            )
            return result.to_dict()
        except RobotError as exc:
            return _error(exc)

    # -- LED / 音量 --------------------------------------------------------
    @mcp.tool
    def set_leds(name: str = "FaceLeds", color: str = "#00A0FF", duration: float = 0.5) -> dict:
        """设置 LED 颜色，color 形如 #RRGGBB。"""
        try:
            _robot().set_leds(name, color, duration)
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def leds_off(name: str = "FaceLeds") -> dict:
        """关闭指定 LED 组。"""
        try:
            _robot().leds_off(name)
            return {"ok": True}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def get_volume() -> dict:
        """查询机器人扬声器音量（0-100）。"""
        try:
            return {"volume": _robot().get_volume()}
        except RobotError as exc:
            return _error(exc)

    @mcp.tool
    def set_volume(volume: int) -> dict:
        """设置扬声器音量（0-100）。"""
        try:
            return {"ok": True, "volume": _robot().set_volume(volume)}
        except RobotError as exc:
            return _error(exc)

    # -- 逃生舱 ------------------------------------------------------------
    @mcp.tool
    def call_service(service: str, method: str, args: list | None = None) -> dict:
        """低层逃生舱：调用任意白名单内的 NAOqi 服务方法（需服务端开启）。"""
        try:
            return {"ok": True, "result": _robot().call_service(service, method, args)}
        except RobotError as exc:
            return _error(exc)

    return mcp
