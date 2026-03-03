# 第六周 — 使用 Semgrep 扫描和修复漏洞

## 作业概述
使用 **Semgrep** 对 `week6/` 中的应用运行静态分析。分类发现并修复至少 3 个安全问题。在你的 write-up 中，解释 Semgrep 发现了什么问题以及你如何修复它们。

## 了解 Semgrep
Semgrep 是一个开源静态分析工具，用于搜索代码、发现错误并实施安全护栏和编码标准。

1. 点击[这里](https://github.com/semgrep/semgrep/blob/develop/README.md)了解 Semgrep。

2. 按照上面的链接中的安装说明进行操作。你可以选择使用 **Semgrep Appsec Platform** 或 **CLI 工具**。

## 扫描任务

### 你将扫描的内容
- 后端 Python（FastAPI）：`week6/backend/`
- 前端 JavaScript：`week6/frontend/`
- 依赖：`week6/requirements.txt`
- 配置/环境（用于密钥）：`week6/` 中的文件

### 运行一般安全扫描以及针对密钥和依赖的专注扫描。

从**作业仓库根目录**运行以下命令，应用包含代码和密钥规则的精选 CI 风格包：
```bash
semgrep ci --subdir week6
```

## 任务
1. 选择 Semgrep 发现的任何 3 个问题，并使用你选择的 AI 编码工具进行修复。

2. 展示精确的编辑并解释缓解方法（例如，参数化 SQL、更安全的 API、更强的加密、清理的 DOM 写入、限制 CORS、依赖升级）。

3. 重要：确保修复后应用仍能运行且测试仍能通过。

## 交付物
### 1. 简要发现概述
- 总结 Semgrep 报告的类别（SAST/Secrets/SCA）。
- 记下你选择忽略的任何误报或嘈杂规则及其原因。

### 2. 三个修复（修复前 → 修复后）
对于每个修复的问题：
- 文件和行号
- Semgrep 标记的规则/类别
- 简要风险描述
- 你的更改（简短代码差异或解释，AI 编码工具使用）
- 为什么这能缓解问题

## 提示
- 首选针对根本原因的最小、针对性更改。
- 每次修复后重新运行 Semgrep 以确认发现已解决且没有引入新问题。
- 对于依赖，记录升级版本，如果使用供应链扫描则链接到公告。

## 提交说明
1. 确保你已将所有更改推送到远程仓库以进行评分。
2. 确保你已添加 brentju 和 febielin 作为作业仓库的合作者。
2. 通过 Gradescope 提交。
