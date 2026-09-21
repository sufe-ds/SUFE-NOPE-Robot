# Embodied

NAO 机器人具身智能交互项目，基于 Python 3.12 + [qi](https://github.com/aldebaran/libqi-python)（NAOqi 的 Python 3 官方绑定）。

## 环境

- Python 3.12
- [uv](https://docs.astral.sh/uv/)
- 依赖：`qi`（`uv add qi`）

```sh
uv sync
```

## 使用

连接机器人并让 NAO 说话：

```sh
uv run embodied --ip 192.168.2.34 --say "你好，我是 Embodied"
```

也可用环境变量 `NAO_IP` / `NAO_PORT` 指定机器人地址与端口（默认 `127.0.0.1:9559`）。

## 开发笔记

- `qi.Session().connect("tcp://<ip>:9559")`，再用 `session.service("ALTextToSpeech")` 获取服务。
- `qi` 取代了 Python 2 的 `naoqi.ALProxy`，语法略有不同。
