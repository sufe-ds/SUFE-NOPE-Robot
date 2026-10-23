# AGENTS.md

上财 NOPE 机器人社仓库。多机器人、多形态混合仓库，**不是单一工程**。

## 仓库结构

- `Robots/NAO/projects/Embodied/` — 唯一的现代 Python 工程（具身智能交互，Agent 操控 NAO）。主要工作区。
- `Robots/NAO/projects/*` 其余项 — Choregraphe 行为工程，由 `manifest.xml` + `behavior_1/behavior.xar` 组成，是图形化工具产物，**不要当普通源码重构或用编辑器直接改 xar**。
- `Robots/NAO/pkg/*.pkg`、`Robots/NAO/choregraph/show.lyt`、`Robots/NAO/movements/*.py` — 装到机器人/Choregraphe 上的资源与动作脚本，非本仓库构建产物。
- `Robots/TonyPi/` — 另一款机器人（Hiwonder 人形），与本仓库 Python 工程无关。
- `Docs/`、`Shows/`、`Assets/` — 文档、外出展示资料、素材。

## Embodied 工程（`Robots/NAO/projects/Embodied/`）

Python 3.12 + `uv` + [`qi`](https://github.com/aldebaran/libqi-python)（NAOqi 的 Python 3 绑定；Windows 上是导入名同为 `qi` 的 `libqi-windows` 轮子）。详见该目录 `README.md`。

Linux / macOS / Windows 三平台都能原生运行：`pyproject.toml` 按 `sys_platform` 分别声明 `qi` 与 `libqi-windows`，不要额外引入 WSL / Docker。

命令（在 `Robots/NAO/projects/Embodied/` 下执行）：

```sh
uv sync
NAO_IP=<robot-ip> uv run uvicorn embodied.app:app --host 0.0.0.0 --port 8000
EMBODIED_DRY_RUN=1 uv run uvicorn embodied.app:app --port 8000   # 不接机器人
uv run pytest                                                    # 用 FakeRobot，无需机器人
```

Windows PowerShell 下环境变量写作 `$env:NAO_IP = "<robot-ip>"`。

- 无 CLI / console script：服务用 `uvicorn embodied.app:app` 启动，配置走环境变量或 `.env`（`Settings` 在 `service/config.py`，`app = create_app()` 在 `app.py` 模块级）。
- 连接地址：环境变量 `NAO_IP`/`NAO_PORT` > 默认 `127.0.0.1:9559`。
- 有 pytest（`tests/`，`asyncio_mode=auto`）；无 lint / typecheck 配置，不要臆造。

### 分层架构（`src/embodied/`，DDD，依赖单向）

依赖方向 `domain ← service ← api`；组装根 `container.py` / `app.py` 可依赖所有层。**不要跨层或反向依赖。**

- `domain/`：纯领域（实体 `entities.py`、值对象 `values.py`、`trajectory.py` 轨迹展平、`errors.py`）。不得导入 qi/FastAPI/pydantic/外层。
- `service/`：应用服务 + `ports.py` 抽象端口（`RobotPort` / `MovementRepository` / `JobQueue`）+ 具体实现（`qi_robot.py` 唯一接触 `qi`，`_motion_lock`/`_call_lock`，`stop_all` 绕过锁；`fake_robot.py`、`movement_files.py`、`thread_jobs.py`（单后台 worker）、`config.py`）。本项目无数据库，不单设基础设施层。
- `api/`：`rest.py`（FastAPI）、`mcp.py`（FastMCP 工具）、`schemas.py`。只依赖 `service`，不得直接调用 `qi`。
- `container.py`：组装根，把具体实现注入应用服务。
- Agent 接入：服务端 `http://localhost:8000/mcp/`；stdio-only 客户端用 `uvx fastmcp-remote http://localhost:8000/mcp/ --auth none`。

## 约定

- 文档与注释以中文为主。
- 新代码放 `src/embodied/`，保持入口 `embodied.app:app`（服务）；不要引入 CLI。
- 用 `qi` 的方式与旧的 Python 2 `naoqi.ALProxy` 不同：`qi.Session().connect("tcp://<ip>:9559")`，再 `session.service("ALTextToSpeech")`。
