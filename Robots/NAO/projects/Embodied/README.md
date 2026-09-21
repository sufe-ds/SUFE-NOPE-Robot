# Embodied

NAO 机器人具身智能交互项目，基于 Python 3.12 + [qi](https://github.com/aldebaran/libqi-python)（NAOqi 的 Python 3 官方绑定）。既保留命令行一次性说话，也提供 **FastAPI REST 服务**与 **MCP 工具**，让 LLM Agent 直接操控机器人。

## 环境

- Python 3.12
- [uv](https://docs.astral.sh/uv/)
- 依赖：`qi` / `fastapi` / `fastmcp` / `pillow` 等

> **关键限制**：`qi` 只发布 manylinux / macOS 轮子，没有 Windows 轮子。本项目必须在 **WSL / Linux（或 macOS）** 下运行，Windows 原生 `uv sync` 装不上 `qi`。仓库内 `.venv` 是 Linux 版。

```sh
uv sync
```

## 使用

连接机器人并让 NAO 说话（旧用法，保持不变）：

```sh
uv run embodied --ip 192.168.2.34 --say "你好，我是 Embodied"
```

也可用环境变量 `NAO_IP` / `NAO_PORT` 指定机器人地址与端口（默认 `127.0.0.1:9559`）。

### 启动服务

```sh
uv run embodied serve --ip 192.168.2.34 --host 0.0.0.0 --http-port 8000
# 不接机器人、纯本地体验：
uv run embodied serve --dry-run
```

- REST 文档：`http://localhost:8000/docs`
- MCP 端点：`http://localhost:8000/mcp/`

### 连接 MCP（Agent 侧）

支持远程 HTTP 的客户端：

```json
{"mcpServers": {"nao": {"type": "http", "url": "http://localhost:8000/mcp/"}}}
```

只支持 stdio 的客户端，在 Windows 上用 `uvx` 桥接（无需 `qi`）：

```json
{"mcpServers": {"nao": {"command": "uvx", "args": ["fastmcp-remote", "http://localhost:8000/mcp/", "--auth", "none"]}}}
```

局域网其他机器访问 WSL 服务，需配置 mirrored networking 或 `netsh portproxy`（见 `.env.example` 顶部说明与计划文档）。

## 能力

| 分类 | 能力 |
| --- | --- |
| 说话 | `say`（可 `animated`）、`stop` |
| 姿态/运动 | `wake` / `rest` / `list_postures` / `go_to_posture` / `set_angles` / `walk` |
| 动作舞蹈 | `list_dances` / `dance`（异步任务，`get_job` 轮询）/ `cancel_job` |
| 摄像头 | `snapshot` / `mjpeg` / `info` |
| 语音识别 | `listen`（给定词表，返回识别词与置信度） |
| LED/音量 | `set_leds` / `leds_off` / `set_volume` / `get_volume` |
| 逃生舱 | `call_service`（默认关闭，调用白名单内任意 NAOqi 服务） |

## 配置

环境变量或项目根目录 `.env`（模板见 `.env.example`）：

- `NAO_IP` / `NAO_PORT`：机器人地址与端口。
- `EMBODIED_HOST` / `EMBODIED_PORT` / `EMBODIED_MCP_PATH`：服务监听。
- `EMBODIED_DRY_RUN`：不连接机器人，使用假实现。
- `EMBODIED_MOVEMENTS_DIR`：动作模块目录（默认 `Robots/NAO/movements`）。
- `EMBODIED_API_TOKEN`：设置后对 `/api`、`/mcp` 强制 `Authorization: Bearer`。
- `EMBODIED_ENABLE_ESCAPE_HATCH` / `EMBODIED_ALLOWED_SERVICES`：逃生舱开关与白名单。

## 开发

```sh
uv run pytest          # 全部使用 FakeRobot，无需机器人
uv run embodied serve --dry-run
```

### 开发笔记

- `qi.Session().connect("tcp://<ip>:9559")`，再用 `session.service("ALTextToSpeech")` 获取服务。
- `qi` 取代了 Python 2 的 `naoqi.ALProxy`，语法略有不同。
- 运动类服务（`ALMotion`/`ALRobotPosture`）由 `_motion_lock` 串行化，长动作会长时间持有该锁；`stop_all` 故意绕过锁以便随时急停。
- 动作模块（`Robots/NAO/movements/*.py`）是 LabVIEW 导出的数据，`main()` 返回 `(Posture, time, movements)`，由 `movements.py` 展平后交给 `ALMotion.angleInterpolationBezier`。
