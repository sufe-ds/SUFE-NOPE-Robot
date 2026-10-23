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
uv run embodied discover 192.168.2.0/24                        # 先用工具确认机器人 IP
uv run embodied serve --robot-ip <robot-ip>                    # 启动 REST + MCP
uv run embodied serve --dry-run                                # 不接机器人
uv run pytest                                                  # 用 FakeRobot，无需机器人
```

Windows PowerShell 下环境变量写作 `$env:NAO_IP = "<robot-ip>"`。

- CLI 只有 `discover` / `serve` 两个子命令（console script `embodied`，`[project.scripts]` -> `cli.py`）。服务参数优先用命令行传（`--robot-ip` / `--robot-port` / `--host` / `--port` / `--dry-run` / `--log-level`），未传的由 `Settings` 从环境变量 / `.env` 读取（`Settings` 在 `service/config.py`）。`uvicorn embodied.app:app` 仍可按环境变量启动，作为无脚本的备用入口。
- 连接地址：CLI 参数 > 环境变量 `NAO_IP`/`NAO_PORT` > 默认 `127.0.0.1:9559`。
- 有 pytest（`tests/`，`asyncio_mode=auto`）；无 lint / typecheck 配置，不要臆造。

### 分层架构（`src/embodied/`，DDD，依赖单向）

依赖方向 `domain ← service ← api`；组装根 `container.py` / `app.py` 可依赖所有层。**不要跨层或反向依赖。**

- `domain/`：纯领域（实体 `entities.py`、值对象 `values.py`、`trajectory.py` 轨迹展平、`errors.py`）。不得导入 qi/FastAPI/pydantic/外层。
- `service/`：应用服务 + `ports.py` 抽象端口（`RobotPort` / `RobotLocator` / `MovementRepository` / `JobQueue`）+ 具体实现（`qi_robot.py` 唯一接触 `qi`，`_motion_lock`/`_call_lock`，`stop_all` 绕过锁；`fake_robot.py`、`network_scan.py`、`movement_files.py`、`thread_jobs.py`（单后台 worker）、`config.py`）。本项目无数据库，不单设基础设施层。
- `api/`：`rest.py`（FastAPI）、`mcp.py`（FastMCP 工具）、`schemas.py`。只依赖 `service`，不得直接调用 `qi`。
- `container.py`：组装根，把具体实现注入应用服务。
- `cli.py` + `discover.py`：`uv run embodied` 的 `serve` / `discover` 入口。`serve` 把参数映射成 `Settings` 后交给 `app.create_app`；`discover` 直接用 `service/` 的 `DiscoveryService` + `SubnetRobotLocator`，不经过 `Container`。
- Agent 接入：服务端 `http://localhost:19559/mcp/`；stdio-only 客户端用 `uvx fastmcp-remote http://localhost:19559/mcp/ --auth none`。

## 约定

- 文档与注释以中文为主。
- 新代码放 `src/embodied/`，保持服务入口 `embodied.app:app`；CLI 只保留 `discover` / `serve`，不要扩成通用控制命令。
- 用 `qi` 的方式与旧的 Python 2 `naoqi.ALProxy` 不同：`qi.Session().connect("tcp://<ip>:9559")`，再 `session.service("ALTextToSpeech")`。
