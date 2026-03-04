# 仓库任务

## 1) 启用 pre-commit 并修复仓库
- 安装钩子：`pre-commit install`
- 运行：`pre-commit run --all-files`
- 修复所有格式/lint问题（black/ruff）

## 2) 添加笔记搜索端点
- 添加/扩展 `GET /notes/search?q=...`（不区分大小写），使用 SQLAlchemy 过滤器
- 更新 `frontend/app.js` 以使用搜索查询
- 在 `backend/tests/test_notes.py` 中添加测试

## 3) 完成待办事项流程
- 实现 `PUT /action-items/{id}/complete`（已搭建框架）
- 更新UI以反映完成状态（已连接）并扩展测试覆盖

## 4) 改进提取逻辑
- 扩展 `backend/app/services/extract.py` 以解析 `#tag` 这样的标签并返回它们
- 为新的解析行为添加测试
-（可选）公开 `POST /notes/{id}/extract` 将笔记转换为待办事项

## 5) 笔记增删改查增强
- 添加 `PUT /notes/{id}` 用于编辑笔记（标题/内容）
- 添加 `DELETE /notes/{id}` 用于删除笔记
- 更新 `frontend/app.js` 以支持编辑/删除；添加测试

## 6) 请求验证和错误处理
- 在 `schemas.py` 中添加简单的验证规则（例如，最小长度）
- 在适当的地方返回信息丰富的 400/404 错误；添加验证失败测试

## 7) 文档漂移检查（目前手动）
- 创建/维护一个简单的 `API.md` 描述端点和请求/响应载荷
- 每次更改后，验证文档与实际的 OpenAPI (`/openapi.json`) 匹配

