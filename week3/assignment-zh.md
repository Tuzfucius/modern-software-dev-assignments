# 第三周 — 构建自定义 MCP 服务器

设计和实现一个封装真实外部 API 的模型上下文协议（MCP）服务器。你可以：
- **本地**运行（STDIO 传输）并与 MCP 客户端集成（如 Claude Desktop）。
- 或**远程**运行（HTTP 传输）并从模型代理或客户端调用它。这更难，但可以获得额外加分。

添加与 MCP Authorization 规范一致的身份验证（API 密钥或 OAuth2）可获得加分。

## 学习目标
- 了解核心 MCP 能力：工具、资源、提示。
- 实现具有类型化参数和健壮错误处理的工具定义。
- 遵循日志记录和传输最佳实践（STDIO 服务器不使用 stdout）。
- （可选）实现 HTTP 传输的授权流程。

## 要求
1. 选择一个外部 API 并记录你将使用哪些端点。示例：天气、GitHub issues、Notion 页面、电影/电视数据库、日历、任务管理器、金融/加密、旅行、体育统计。
2. 暴露至少两个 MCP 工具
3. 实现基本弹性：
   - 对 HTTP 失败、超时和空结果的优雅错误处理。
   - 遵守 API 速率限制（例如，简单退避或面向用户的警告）。
4. 打包和文档：
   - 提供清晰的设置说明、环境变量和运行命令。
   - 包含示例调用流程（要在客户端中输入/点击什么来触发工具）。
5. 选择一种部署模式：
   - 本地：STDIO 服务器，可从你的机器运行，Claude Desktop 或 AI IDE（如 Cursor）可发现。
   - 远程：可通过网络访问的 HTTP 服务器，可由 MCP 感知客户端或代理运行时调用。如果部署且可访问，可获得额外学分。
6. （可选）加分：身份验证
   - 通过环境变量和客户端配置支持 API 密钥；或
   - 用于 HTTP 传输的 OAuth2 风格 bearer 令牌，验证令牌受众，永不将令牌传递给上游 API。

## 交付物
- `week3/` 下的源代码（建议：`week3/server/`，入口点清晰，如 `main.py` 或 `app.py`）。
- 包含以下内容的 `week3/README.md`：
  - 前提条件、环境设置和运行说明（本地和/或远程）。
  - 如何配置 MCP 客户端（本地用 Claude Desktop 示例）或远程的代理运行时。
  - 工具参考：名称、参数、示例输入/输出和预期行为。

## 评估标准（90 分满分）
- 功能性（35）：实现 2+ 工具、正确的 API 集成、有意义的输出。
- 可靠性（20）：输入验证、错误处理、日志记录、速率限制感知。
- 开发者体验（20）：清晰的设置/文档、易于本地运行；合理的文件夹结构。
- 代码质量（15）：可读性代码、描述性名称、最小复杂性、适用处的类型提示。
- 额外学分（10）：
  - +5 远程 HTTP MCP 服务器，可由代理/客户端（如 OpenAI/Claude SDK）调用。
  - +5 正确实现身份验证（API 密钥或带受众验证的 OAuth2）。

## 有用的参考
- MCP 服务器快速入门：[modelcontextprotocol.io/quickstart/server](https://modelcontextprotocol.io/quickstart/server)。
*注意：你不能提交此示例。*
- MCP 授权（HTTP）：[modelcontextprotocol.io/specification/2025-06-18/basic/authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
- Cloudflare 上的远程 MCP（代理）：[developers.cloudflare.com/agents/guides/remote-mcp-server/](https://developers.cloudflare.com/agents/guides/remote-mcp-server/)。在部署前使用 modelcontextprotocol 检查器工具在本地调试你的服务器。
- https://vercel.com/docs/mcp/deploy-mcp-servers-to-vercel 如果你选择做远程 MCP 部署，Vercel 是一个不错的选择，有免费层。
