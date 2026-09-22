"""CameraStreamer 回归测试：``info()`` 不能因锁重入而死锁。"""

from __future__ import annotations

import threading
import time

from embodied.service.qi_robot import CameraStreamer


class _DummyRobot:
    pass


def test_info_does_not_deadlock() -> None:
    streamer = CameraStreamer(_DummyRobot(), camera=0, resolution=1, fps=10)
    streamer._frame = b"fake-jpeg"
    streamer._frame_ts = time.time()

    result: dict = {}

    def call() -> None:
        result.update(streamer.info())

    thread = threading.Thread(target=call, daemon=True)
    thread.start()
    thread.join(timeout=2.0)

    assert not thread.is_alive(), "CameraStreamer.info() 发生死锁"
    assert result["age_s"] is not None
    assert result["fps"] == 10
