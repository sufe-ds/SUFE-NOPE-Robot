"""REST API 测试（dry-run 使用 FakeRobot，无需机器人）。"""

from __future__ import annotations

import asyncio

import httpx
import pytest

from embodied.app import create_app
from embodied.service.config import Settings


@pytest.fixture
def app():
    return create_app(Settings(dry_run=True))


@pytest.fixture
async def client(app):
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as c:
        yield c


async def test_health(client) -> None:
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


async def test_say(client) -> None:
    response = await client.post("/api/robot/say", json={"text": "你好"})
    assert response.status_code == 200
    assert response.json()["ok"] is True


async def test_posture(client) -> None:
    response = await client.post("/api/robot/posture", json={"name": "Stand"})
    assert response.status_code == 200
    assert response.json()["posture"] == "Stand"


async def test_posture_unknown(client) -> None:
    response = await client.post("/api/robot/posture", json={"name": "Fly"})
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "unknown_posture"


async def test_validation_error_shape(client) -> None:
    response = await client.post("/api/robot/angles", json={"names": ["HeadYaw"]})
    assert response.status_code == 422
    assert response.json()["error"]["code"] == "validation_error"


async def test_movement_job_flow(client) -> None:
    response = await client.post("/api/movements/move1", json={"wait": False})
    assert response.status_code == 202
    job_id = response.json()["job_id"]

    for _ in range(50):
        job = (await client.get(f"/api/jobs/{job_id}")).json()
        if job["status"] in ("done", "failed"):
            break
        await asyncio.sleep(0.05)
    assert job["status"] == "done"
    assert job["result"]["name"] == "move1"


async def test_movement_unknown(client) -> None:
    response = await client.post("/api/movements/nope", json={})
    assert response.status_code == 404


async def test_movements_list(client) -> None:
    response = await client.get("/api/movements")
    assert response.status_code == 200
    names = {item["name"] for item in response.json()["movements"]}
    assert "move1" in names


async def test_camera_snapshot(client) -> None:
    response = await client.get("/api/camera/snapshot")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"
    assert response.content[:2] == b"\xff\xd8"


async def test_escape_hatch_disabled(client) -> None:
    response = await client.post(
        "/api/call", json={"service": "ALMotion", "method": "wakeUp", "args": []}
    )
    assert response.status_code == 403
    assert response.json()["error"]["code"] == "forbidden_service"


async def test_escape_hatch_enabled() -> None:
    app = create_app(Settings(dry_run=True, enable_escape_hatch=True))
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as c:
        response = await c.post(
            "/api/call", json={"service": "ALMemory", "method": "getData", "args": ["x"]}
        )
    assert response.status_code == 200
    assert response.json()["result"]["fake"] is True


async def test_volume_roundtrip(client) -> None:
    response = await client.post("/api/volume", json={"volume": 42})
    assert response.status_code == 200
    assert (await client.get("/api/volume")).json()["volume"] == 42
