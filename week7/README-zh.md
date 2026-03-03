# 第七周

稍微增强的全栈入门（从第五周复制），带有一些后端改进。

- FastAPI 后端与 SQLite（SQLAlchemy）
- 静态前端（无需 Node 工具链）
- 最小化测试（pytest）
- Pre-commit（black + ruff）
- 第五周改进：
  - 模型上的时间戳（`created_at`、`updated_at`）
  - 列表端点的分页和排序
  - 可选过滤（例如按完成状态过滤待办事项）
  - 用于部分更新的 PATCH 端点

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

3) 运行应用（从 `week6/`）

```bash
cd week7 && make run
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
cd week7 && make test
```

## 格式化/代码检查

```bash
cd week7 && make format
cd week7 && make lint
```

## 配置

将 `.env.example` 复制到 `.env`（在 `week7/` 中）以覆盖默认值，如数据库路径。
