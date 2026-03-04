# 仓库任务

## 1) 将前端迁移到 Vite + React（复杂）
- 在 `week5/frontend/`（或子文件夹如 `week5/frontend/ui/`）中搭建 Vite + React 应用。
- 用 FastAPI 服务的构建包替换当前的静态资源：
  - 构建到 `week5/frontend/dist/`。
  - 更新 FastAPI 静态挂载以服务 `dist` 和根路径（`/`）到 `dist` 中的 `index.html`。
- 在 React 中连接现有端点：
  - 笔记列表、创建、删除、编辑。
  - 待办事项列表、创建、完成。
- 更新 `Makefile` 添加目标：`web-install`、`web-dev`、`web-build`，并确保 `make run` 自动构建 web 包（或记录工作流程）。
- 为至少两个组件添加组件/单元测试（React Testing Library），并在 `backend/tests` 中添加 API 兼容性集成测试。

## 2) 带分页和排序的笔记搜索（中等）
- 实现 `GET /notes/search?q=...&page=1&page_size=10&sort=created_desc|title_asc`。
- 在标题/内容上使用不区分大小写的匹配。
- 返回包含 `items`、`total`、`page`、`page_size` 的载荷。
- 添加 SQLAlchemy 查询组合用于过滤、排序和分页。
- 更新 React UI，添加搜索输入、结果计数和上/下页分页控件。
- 在 `backend/tests/test_notes.py` 中添加查询边界情况和分页测试。

## 3) 完整笔记增删改查与乐观 UI 更新（中等）
- 添加 `PUT /notes/{id}` 和 `DELETE /notes/{id}`。
- 在前端中，在处理错误回滚的同时乐观地更新状态。
- 在 `schemas.py` 中验证载荷（最小长度、合理情况下的最大长度）。
- 为成功和验证错误添加测试。

## 4) 待办事项：过滤和批量完成（中等）
- 添加 `GET /action-items?completed=true|false` 按完成状态过滤。
- 添加 `POST /action-items/bulk-complete` 接受 ID 列表并在事务中将其标记为已完成。
- 更新前端添加过滤开关和批量操作 UI。
- 添加测试覆盖过滤、批量行为和错误时的事务回滚。

## 5) 标签功能与多对多关系（复杂）
- 添加 `Tag` 模型和连接表 `note_tags`（`Note` 和 `Tag` 之间的多对多）。
- 端点：
  - `GET /tags`、`POST /tags`、`DELETE /tags/{id}`
  - `POST /notes/{id}/tags` 用于附加，`DELETE /notes/{id}/tags/{tag_id}` 用于分离
- 更新提取（见下一个任务）以从 `#hashtags` 自动创建/附加标签。
- 更新 UI 以标签芯片形式显示标签并按标签过滤笔记。
- 为模型关系和端点行为添加测试。

## 6) 改进提取逻辑和端点（中等）
- 扩展 `backend/app/services/extract.py` 以解析：
  - `#hashtags` → 标签
  - `- [ ] task text` → 待办事项
- 添加 `POST /notes/{id}/extract`：
  - 返回结构化的提取结果，并在 `apply=true` 时选择性地持久化新标签/待办事项
- 为提取解析和 `apply=true` 持久化路径添加测试。

## 7) 健壮的错误处理和响应包装（简单-中等）
- 使用 Pydantic 模型添加验证（最小长度约束、非空字符串）。
- 添加全局异常处理器以返回一致的 JSON 包装：
  - `{ "ok": false, "error": { "code": "NOT_FOUND", "message": "..." } }`
  - 成功响应：`{ "ok": true, "data": ... }`
- 更新测试以断言成功和错误情况下的包装格式。

## 8) 所有集合的列表端点分页（简单）
- 在 `GET /notes` 和 `GET /action-items` 中添加 `page` 和 `page_size`。
- 为每个返回 `items` 和 `total`。
- 更新前端以分页列表；为边界情况添加测试（最后一页为空、page_size 过大）。

## 9) 查询性能和索引（简单-中等）
- 在有益的地方添加 SQLite 索引（例如，`notes.title`、标签的连接表）。
- 通过种子较大数据集的测试验证改进的查询计划并确保没有回归。

## 10) 测试覆盖改进（简单）
- 添加覆盖以下内容的测试：
  - 每个端点的 400/404 场景
  - 批量操作的并发/事务行为
  - 前端搜索、分页和乐观更新的集成测试（可以是模拟的或轻量级的）

## 11) 可部署到 Vercel（中等-复杂）
- Vite + React 前端：
  - 添加带有 `build` 和 `preview` 脚本的 `package.json`，并配置 Vite 输出到 `frontend/dist`（或 `frontend/ui/dist`）。
  - 添加 `vercel.json` 将项目根目录设置为 `week5/frontend`，将 `outputDirectory` 设置为 `dist`。
  - 在构建时注入 `VITE_API_BASE_URL` 指向 API。
- Vercel 上的 API（选项 A，无服务器 FastAPI）：
  - 创建 `week5/api/index.py`，从 `backend/app/main.py` 导入 FastAPI `app`。
  - 确保 Vercel 可用 Python 依赖（为函数使用 `pyproject.toml` 或 `requirements.txt`）。
  - 配置 CORS 以允许 Vercel 前端源。
  - 更新 `vercel.json` 将 `/api/*` 路由到 Python 函数，并为其他路由服务 React 应用。
- 其他地方的 API（选项 B）：
  - 将后端部署到 Fly.io 或 Render 等服务。
  - 配置 Vercel 前端通过 `VITE_API_BASE_URL` 使用外部 API，并设置所需的任何重写/代理。
- 在 `README.md` 中添加简短的部署指南，包括环境变量、构建命令和回滚。
