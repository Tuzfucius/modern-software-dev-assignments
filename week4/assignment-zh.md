# 第四周 — 现实中的自主编码代理

> ***我们建议在开始之前先阅读整篇文档。***

本周，你的任务是在本仓库的上下文中构建至少 **2 个自动化**，使用以下任意 **Claude Code** 特性：

- 自定义斜杠命令（提交到 `.claude/commands/*.md`）
- 用于仓库或上下文指导的 `CLAUDE.md` 文件
- Claude 子代理（协同工作的专业角色代理）
- 集成到 Claude Code 的 MCP 服务器

你的自动化应该显著改善开发者工作流程——例如，简化测试、文档、重构或数据相关任务。然后，你将使用你创建的自动化来扩展 `week4/` 中的入门应用。

## 了解 Claude Code
要深入了解 Claude Code 并探索你的自动化选项，请阅读以下两个资源：

1. **Claude Code 最佳实践：** [anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)

2. **子代理概述：** [docs.anthropic.com/en/docs/claude-code/sub-agents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)

## 探索入门应用
一个最小的全栈入门应用，设计为 **"开发者命令中心"**。
- FastAPI 后端与 SQLite（SQLAlchemy）
- 静态前端（无需 Node 工具链）
- 最小化测试（pytest）
- Pre-commit（black + ruff）
- 代理驱动工作流的任务

使用此应用作为你的试验场来尝试你构建的 Claude 自动化。

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

3) 运行应用（从 `week4/` 目录）

```bash
make run
```

4) 打开 `http://localhost:8000` 查看前端，`http://localhost:8000/docs` 查看 API 文档。

5) 稍微摆弄一下入门应用，了解其当前特性和功能。

### 测试
运行测试（从 `week4/` 目录）
```bash
make test
```

### 格式化/代码检查
```bash
make format
make lint
```

## 第一部分：构建你的自动化（选择 2 个或更多）
既然你已熟悉入门应用，下一步就是构建自动化来增强或扩展它。以下是 several automation options you can choose from你可以从中选择的几种自动化选项。你可以跨类别混合搭配。

在构建自动化时，将你的更改记录在 `writeup.md` 文件中。先将 *"How you used the automation to enhance the starter application"* 部分留空——你将在作业第二部分回到这里。

### A) Claude 自定义斜杠命令
斜杠命令是一种用于重复工作流的功能，让你在 `.claude/commands/` 内的 Markdown 文件中创建可重用的工作流。Claude 通过 `/` 暴露这些。

- 示例 1：带覆盖率的测试运行器
  - 名称：`tests.md`
  - 意图：运行 `pytest -q backend/tests --maxfail=1 -x`，如果是绿色的，运行覆盖率。
  - 输入：可选的标记或路径。
  - 输出：总结失败并建议下一步。
- 示例 2：文档同步
  - 名称：`docs-sync.md`
  - 意图：读取 `/openapi.json`，更新 `docs/API.md`，并列出路由差异。
  - 输出：类似 diff 的总结和 TODO。
- 示例 3：重构工具
  - 名称：`refactor-module.md`
  - 意图：重命名模块（例如 `services/extract.py` → `services/parser.py`），更新导入，运行 lint/测试。
  - 输出：修改文件的检查表和验证步骤。

>*提示：保持命令专注，使用 `$ARGUMENTS`，prefer idempotent steps. Consider allowlisting safe tools and using headless mode for repeatability.*

### B) `CLAUDE.md` 指导文件
`CLAUDE.md` 文件在开始对话时自动读取，允许你提供影响 Claude 行为的仓库特定说明、上下文或指导。在仓库根目录（也可以选择在 `week4/` 子文件夹中）创建 `CLAUDE.md` 来指导 Claude 的行为。

- 示例 1：代码导航和入口点
  - 包括：如何运行应用、路由在哪里（`backend/app/routers`）、测试在哪里、如何填充数据库。
- 示例 2：风格和安全护栏
  - 包括：工具期望（black/ruff）、安全命令、避免的命令、lint/测试门禁。
- 示例 3：工作流代码片段
  - 包括："当被要求添加端点时，先写一个失败的测试，然后实现，然后运行 pre-commit。"

> *提示：像提示词一样迭代 `CLAUDE.md`，保持简洁和可操作，记录你希望 Claude 使用的自定义工具/脚本。*

### C) 子代理（专业角色）

子代理是配置为处理具有自己系统提示、工具和上下文的特定任务的专业 AI 助手。设计两个或更多协作代理，每个负责单个工作流中的不同步骤。

- 示例 1：TestAgent + CodeAgent
  - 流程：TestAgent 为更改编写/更新测试 → CodeAgent 实现代码以通过测试 → TestAgent 验证。
- 示例 2：DocsAgent + CodeAgent
  - 流程：CodeAgent 添加新 API 路由 → DocsAgent 更新 `API.md` 和 `TASKS.md` 并检查与 `/openapi.json` 的差异。
- 示例 3：DBAgent + RefactorAgent
  - 流程：DBAgent 提出模式更改（调整 `data/seed.sql`）→ RefactorAgent 更新模型/模式/路由并修复 lint。

>*提示：使用检查表/草稿本，在角色之间重置上下文（`/clear`），对于独立任务并行运行代理。*

## 第二部分：让你的自动化工作
既然你已构建了 2+ 个自动化，让我们让它工作！在 `writeup.md` 的 *"How you used the automation to enhance the starter application"* 部分，描述你如何利用每个自动化来改进或扩展应用的功能。

例如：如果你实现了自定义斜杠命令 `/generate-test-cases`，解释你如何使用它来与入门应用交互和测试。

## 交付物
1) 两个或更多自动化，包括：
   - `.claude/commands/*.md` 中的斜杠命令
   - `CLAUDE.md` 文件
   - 子代理提示/配置（文件/scripts 如果有的话要清楚记录）

2) `week4/` 下的 write-up `writeup.md`，包括：
   - 设计灵感（例如引用最佳实践和/或子代理文档）
   - 每个自动化的设计，包括目标、输入/输出、步骤
   - 如何运行它（精确命令）、预期输出和回滚/安全说明
   - 之前与之后（即手动工作流 vs 自动化工作流）
   - 你如何使用自动化来增强入门应用

## 提交说明
1. 确保你已将所有更改推送到远程仓库以进行评分。
2. **确保你已添加 brentju 和 febielin 作为作业仓库的合作者。**
2. 通过 Gradescope 提交。
