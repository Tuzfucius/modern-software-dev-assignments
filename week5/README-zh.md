# 第五周

用于试验自主编码代理的最小全栈入门。

- FastAPI 后端与 SQLite（SQLAlchemy）
- 静态前端（无需 Node 工具链）
- 最小化测试（pytest）
- Pre-commit（black + ruff）
- 代理驱动工作流的任务

## 快速开始

1) 创建并激活虚拟环境，然后安装依赖

```bash
cd /Users/mihaileric/Documents/code/modern-software-dev-assignments
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
```

2)（可选）安装 pre-commit 钩子

```bash
pre-commit install
```

3) 运行应用（从 `week5/`）

```bash
cd week5 && make run
```

打开 `http://localhost:8000` 查看前端，`http://localhost:8000/docs` 查看 API 文档。

## 结构

```
backend/                # FastAPI 应用
frontend/               # FastAPI 服务的静态 UI
data/                   # SQLite 数据库 + 种子数据
docs/                   # 代理驱动工作流的 TASKS
```

## 测试

```bash
cd week5 && make test
```

## 格式化/代码检查

```bash
cd week5 && make format
cd week5 && make lint
```

## 配置

将 `.env.example` 复制到 `.env`（在 `week5/` 中）以覆盖默认值，如数据库路径。
