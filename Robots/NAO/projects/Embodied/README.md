# Embodied

NAO 机器人具身智能交互项目，基于 Python 3.12 + [qi](https://github.com/aldebaran/libqi-python)（NAOqi 的 Python 3 官方绑定）。提供 **FastAPI REST 服务**与 **MCP 工具**，让 LLM Agent 直接操控机器人。

## 环境

- Python 3.12
- [uv](https://docs.astral.sh/uv/)
- 依赖：`qi` / `fastapi` / `fastmcp` / `pillow` 等

`qi` 在 Linux / macOS 上是官方轮子；Windows 上由 [`libqi-windows`](https://pypi.org/project/libqi-windows/)
提供（libqi 4.0.1 + 官方绑定 3.1.5 的 MSVC 构建，导入名同样是 `qi`，覆盖 cp311–cp314 win_amd64）。
`pyproject.toml` 已按 `sys_platform` 分别声明，三个平台都直接 `uv sync`，不需要 WSL 或容器。

```sh
uv sync
```

## 使用

启动服务（机器人地址等配置见下方「配置」，默认 `127.0.0.1:9559`）：

```sh
NAO_IP=192.168.2.34 uv run uvicorn embodied.app:app --host 0.0.0.0 --port 8000

# 不接机器人、纯本地体验：
EMBODIED_DRY_RUN=1 uv run uvicorn embodied.app:app --host 0.0.0.0 --port 8000
```

PowerShell 里把环境变量写成 `$env:NAO_IP = "192.168.2.34"`。

- REST 文档：`http://localhost:8000/docs`
- MCP 端点：`http://localhost:8000/mcp/`

### 连接 MCP（Agent 侧）

支持远程 HTTP 的客户端：

```json
{"mcpServers": {"nao": {"type": "http", "url": "http://localhost:8000/mcp/"}}}
```

只支持 stdio 的客户端，用 `uvx` 桥接（无需安装本项目依赖）：

```json
{"mcpServers": {"nao": {"command": "uvx", "args": ["fastmcp-remote", "http://localhost:8000/mcp/", "--auth", "none"]}}}
```

局域网其他机器访问本机服务时，需要在防火墙放行 `EMBODIED_PORT`。

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
uv run pytest                                                     # 全部使用 FakeRobot，无需机器人
EMBODIED_DRY_RUN=1 uv run uvicorn embodied.app:app --port 8000    # dry-run 起服务
```

### 架构

领域驱动分层，依赖方向单向：`domain ← service ← api`。

- `domain/` — 纯领域层：实体、值对象、领域函数（轨迹展平）、领域错误。不依赖任何外层。
- `service/` — 服务层：应用服务 + `ports.py` 抽象端口（`RobotPort` / `MovementRepository` / `JobQueue`）+ 具体实现（`qi_robot.py`、`fake_robot.py`、`movement_files.py`、`thread_jobs.py`、`config.py`）。本项目没有数据库，故不单设基础设施层。
- `api/` — 交付层：`rest.py`（FastAPI）、`mcp.py`（FastMCP）、`schemas.py`、错误映射。依赖服务层，不直接接触 `qi`。
- `container.py` / `app.py` — 组装根：把具体实现注入应用服务，再交给 API。

依赖倒置：应用服务依赖 `service/ports.py` 的抽象；具体实现也依赖该抽象（实现它），由 `container.py` 注入。抽象不依赖具体，具体依赖抽象；领域层不依赖任何外层。

## 开发笔记

- `qi.Session().connect("tcp://<ip>:9559")`，再用 `session.service("ALTextToSpeech")` 获取服务。
- `qi` 取代了 Python 2 的 `naoqi.ALProxy`，语法略有不同。
- 运动类服务（`ALMotion`/`ALRobotPosture`）由 `QiRobot._motion_lock` 串行化，长动作会长时间持有该锁；`stop_all` 故意绕过锁以便随时急停。
- 动作模块（`Robots/NAO/movements/*.py`）是 LabVIEW 导出的数据，`main()` 返回 `(Posture, time, movements)`，由 `domain/trajectory.py` 展平后交给 `ALMotion.angleInterpolationBezier`。
- 新增能力：领域模型放 `domain/`，抽象端口放 `service/ports.py`，具体实现放 `service/`（如 `qi_robot.py`），接口放 `api/`；不要在 `api/` 里直接调用 `qi`。
