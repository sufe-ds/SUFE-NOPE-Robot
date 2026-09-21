# AGENTS.md

上财 NOPE 机器人社仓库。多机器人、多形态混合仓库，**不是单一工程**。

## 仓库结构

- `Robots/NAO/projects/Embodied/` — 唯一的现代 Python 工程（具身智能交互，Agent 操控 NAO）。主要工作区。
- `Robots/NAO/projects/*` 其余项 — Choregraphe 行为工程，由 `manifest.xml` + `behavior_1/behavior.xar` 组成，是图形化工具产物，**不要当普通源码重构或用编辑器直接改 xar**。
- `Robots/NAO/pkg/*.pkg`、`Robots/NAO/choregraph/show.lyt`、`Robots/NAO/movements/*.py` — 装到机器人/Choregraphe 上的资源与动作脚本，非本仓库构建产物。
- `Robots/TonyPi/` — 另一款机器人（Hiwonder 人形），与本仓库 Python 工程无关。
- `Docs/`、`Shows/`、`Assets/` — 文档、外出展示资料、素材。

## Embodied 工程（`Robots/NAO/projects/Embodied/`）

Python 3.12 + `uv` + [`qi`](https://github.com/aldebaran/libqi-python)（NAOqi 的 Python 3 绑定）。详见该目录 `README.md`。

**关键限制：`qi` 只发布 manylinux / macOS 轮子，没有 Windows 轮子。**
必须在 WSL/Linux（或 macOS）下运行。仓库内 `.venv` 是 Linux 版（`home = /usr/bin`，含 `bin/` 与 `.so`）；Windows 原生 `uv sync` 无法安装 `qi`，不要试图在 Windows 上直接跑。

命令（在 `Robots/NAO/projects/Embodied/` 下执行，且必须在 WSL/Linux）：

```sh
uv sync
uv run embodied --ip <robot-ip> --say "文本"          # 旧用法保留
uv run embodied serve --ip <robot-ip> --host 0.0.0.0 --http-port 8000
uv run embodied serve --dry-run                        # 不接机器人
uv run pytest                                          # 用 FakeRobot，无需机器人
```

- 入口改到 `src/embodied/cli.py:main`（`pyproject.toml` 脚本 `embodied`）；`main()` 里 `serve` 走服务、否则保留旧的一次性 `--say`。
- 连接地址优先级：CLI `--ip/--port` > 环境变量 `NAO_IP`/`NAO_PORT` > 默认 `127.0.0.1:9559`。
- 有 pytest（`tests/`，`asyncio_mode=auto`）；无 lint / typecheck 配置，不要臆造。

### 服务架构（`src/embodied/`）

- `robot.py`：唯一接触 `qi` 的层。`_motion_lock` 串行化运动，`_call_lock` 管其余 I/O，二者独立；`stop_all` 绕过锁以便急停。
- `movements.py`：用 `importlib` 加载 `Robots/NAO/movements/*.py` 并展平。
- `jobs.py`：单后台 worker，长动作返回 `job_id` 轮询。
- `api.py`（REST，含 `/health`、`/api/*`）、`mcp_server.py`（FastMCP 工具）、`app.py`（`create_app` + `combine_lifespans` 挂载 `/mcp`）。
- `fake.py`：`--dry-run` 与测试用的假机器人；`config.py`：`pydantic-settings`。
- Agent 在 Windows 时：用 `http://localhost:8000/mcp/`（WSL localhost 转发），stdio-only 客户端用 `uvx fastmcp-remote http://localhost:8000/mcp/ --auth none`。

## 约定

- 文档与注释以中文为主。
- 新代码放 `src/embodied/`，保持 CLI 入口 `embodied`（`embodied.cli:main`）。
- 用 `qi` 的方式与旧的 Python 2 `naoqi.ALProxy` 不同：`qi.Session().connect("tcp://<ip>:9559")`，再 `session.service("ALTextToSpeech")`。
