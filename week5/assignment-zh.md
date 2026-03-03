# 第五周 — 使用 Warp 的代理开发

使用 `week5/` 中的应用作为你的试验场。本周与之前的作业类似，但强调 Warp 代理开发环境和多代理工作流。

## 了解 Warp
- Warp 代理开发环境：[warp.dev](https://www.warp.dev/)
- [Warp University](https://www.warp.dev/university?slug=university)

## 探索入门应用
最小全栈入门应用。
- FastAPI 后端与 SQLite（SQLAlchemy）
- 静态前端（无需 Node 工具链）
- 最小化测试（pytest）
- Pre-commit（black + ruff）
- 代理驱动工作流的任务

使用此应用作为你的试验场来尝试你构建的 Warp 自动化。

### 结构

```
backend/                # FastAPI 应用
frontend/               # FastAPI 服务的静态 UI
data/                   # SQLite 数据库 + 种子数据
docs/                   # 代理驱动工作流的 TASKS
```

### 快速开始

1) 激活你的 conda 环境。

```bash
conda activate cs146s
```

2)（可选）安装 pre-commit 钩子

```bash
pre-commit install
```

3) 运行应用（从 `week5/` 目录）

```bash
make run
```

4) 打开 `http://localhost:8000` 查看前端，`http://localhost:8000/docs` 查看 API 文档。

5) 稍微摆弄一下入门应用，了解其当前特性和功能。

### 测试
运行测试（从 `week5/` 目录）
```bash
make test
```

### 格式化/代码检查
```bash
make format
make lint
```

## 第一部分：构建你的自动化（选择 2 个或更多）
从 `week5/docs/TASKS.md` 中选择任务来实现。你的实现必须以以下方式利用 Warp（详见下文）：

- A) 使用 Warp Drive 特性——如保存的提示、规则或 MCP 服务器。
- (B) 在 Warp 中结合多代理工作流。

将你的更改集中在 `week5/` 内的后端、前端、逻辑或测试。对于每个选定的任务，记录其难度级别。

### A) Warp Drive 保存的提示、规则、MCP 服务器（必选：至少一个）
为此仓库创建一个或多个可共享的 Warp Drive 提示、规则或 MCP 服务器集成。示例：
- 带覆盖率和不稳定测试重跑的测试运行器
- 文档同步：从 `/openapi.json` 生成/更新 `docs/API.md`，列出路由差异
- 重构工具：重命名模块，更新导入，运行 lint/测试
- 发布助手：版本提升，运行检查，准备 changelog 片段
- 集成 Git MCP 服务器，让 Warp 能够自主与 Git 交互（创建分支、提交、PR 笔记等）

>*提示：保持工作流专注，传递参数，使它们具有幂等性，在可能的情况下首选无头/非交互步骤。*

### B) Warp 中的多代理工作流（必选：至少一个）
运行多代理会话，让不同 Warp 标签页中的独立代理同时处理独立任务。
- 使用并发代理在单独的 Warp 标签页中执行 `TASKS.md` 中的多个独立任务。挑战：你能让多少代理同时工作？

>*提示：[git worktree](https://git-scm.com/docs/git-worktree) 可能有助于防止代理相互覆盖。*

## 第二部分：让你的自动化工作
既然你已构建了 2+ 个自动化，让我们让它工作！在 `writeup.md` 的 *"How you used the automation (what pain point it resolves or accelerates)"* 部分，描述你如何利用每个自动化来改进某些工作流。

## 约束和范围
严格在 `week5/` 中工作（后端、前端、逻辑、测试）。除非自动化明确要求且你记录了原因，否则不要更改其他周的内容。

## 交付物
1) 两个或更多 Warp 自动化，包括：
   - Warp Drive 工作流/规则（分享链接和/或导出的定义）和任何辅助脚本
   - 用于协调多个代理的任何补充提示/手册

2) `week5/` 下的 write-up `writeup.md`，包括：
   - 每个自动化的设计，包括目标、输入/输出、步骤
   - 之前与之后（即手动工作流 vs 自动化工作流）
   - 每个完成任务使用的自主级别（哪些代码权限，为什么，以及你如何监督）
   - （如果适用）多代理笔记：角色、协调策略和并发收益/风险/失败
   - 你如何使用自动化（它解决或加速了什么痛点）

## 提交说明
1. 确保你已将所有更改推送到远程仓库以进行评分。
2. **确保你已添加 brentju 和 febielin 作为作业仓库的合作者。**
2. 通过 Gradescope 提交。
