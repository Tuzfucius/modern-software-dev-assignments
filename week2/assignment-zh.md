# 第二周 — 待办事项提取器

本周，我们将扩展一个最小的 FastAPI + SQLite 应用，将自由格式的笔记转换为枚举的待办事项。

***我们建议在开始之前先阅读整篇文档。***

提示：预览此 markdown 文件
- Mac 上，按 `Command (⌘) + Shift + V`
- Windows/Linux 上，按 `Ctrl + Shift + V`

## 入门

### Cursor 设置
按照以下说明设置 Cursor 并打开你的项目：
1. 兑换免费的 Cursor Pro 一年：https://cursor.com/students
2. 下载 Cursor：https://cursor.com/download
3. 要启用 Cursor 命令行工具，打开 Cursor，对于 Mac 用户按 `Command (⌘) + Shift+ P`（或非 Mac 用户按 `Ctrl + Shift + P`）打开命令面板。输入：`Shell Command: Install 'cursor' command`。选择它并按回车。
4. 打开新终端窗口，导航到项目根目录，运行：`cursor .`

### 当前应用
以下是你如何启动当前入门应用的方法：
1. 激活你的 conda 环境
```
conda activate cs146s
```
2. 从项目根目录，运行服务器：
```
poetry run uvicorn week2.app.main:app --reload
```
3. 打开网页浏览器并导航到 http://127.0.0.1:8000/。
4. 熟悉应用的当前状态。确保你能成功输入笔记并生成提取的待办事项清单。

## 练习
对于每个练习，使用 Cursor 来帮助你实现当前待办事项提取器应用的指定改进。

在完成作业时，使用 `writeup.md` 记录你的进度。请务必包含你使用的提示词，以及你或 Cursor 做的任何更改。我们将根据 write-up 的内容进行评分。请也在你的代码中包含注释来记录你的更改。

### TODO 1：搭建新功能

分析现有的 `extract_action_items()` 函数在 `week2/app/services/extract.py` 中，它目前使用预定义启发式方法提取待办事项。

你的任务是实现一个 **LLM 驱动的**替代方案 `extract_action_items_llm()`，利用 Ollama 通过大语言模型执行待办事项提取。

一些提示：
- 要产生结构化输出（即 JSON 字符串数组），请参考此文档：https://ollama.com/blog/structured-outputs
- 要浏览可用的 Ollama 模型，请参考此文档：https://ollama.com/library。请注意，更大的模型会消耗更多资源，所以从小模型开始。拉取并运行模型：`ollama run {MODEL_NAME}`

### TODO 2：添加单元测试

在 `week2/tests/test_extract.py` 中为 `extract_action_items_llm()` 编写单元测试，覆盖多个输入（例如，项目符号列表、关键字前缀行、空输入）。

### TODO 3：重构现有代码以提高清晰度

对后端代码进行重构，特别关注：明确定义的 API 契约/模式、数据库层清理、应用生命周期/配置、错误处理。

### TODO 4：使用 Agentic 模式自动化小任务

1. 将 LLM 驱动的提取集成作为一个新端点。更新前端以包含一个"提取 LLM"按钮，点击后通过新端点触发提取过程。

2. 暴露一个最终端点来检索所有笔记。更新前端以包含一个"列出笔记"按钮，点击后获取并显示它们。

### TODO 5：从代码库生成 README

***学习目标：***
*学生学习如何让 AI 检查代码库并自动生成文档，展示 Cursor 解析代码上下文并将其转换为人类可读形式的能力。*

使用 Cursor 分析当前代码库并生成结构良好的 `README.md` 文件。README 至少应包括：
- 项目简要概述
- 如何设置和运行项目
- API 端点和功能
- 如何运行测试套件的说明

## 交付物
按照说明填写 `week2/writeup.md`。确保你的所有更改都记录在代码库中。

## 评估标准（100 分满分）
- 第 1-5 部分每部分 20 分（10 分用于生成的代码，10 分用于每个提示词）
