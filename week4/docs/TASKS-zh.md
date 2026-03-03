# 仓库任务

## 1) 启用 pre-commit 并修复仓库
- 安装钩子：`pre-commit install`
- 运行：`pre-commit run --all-files`
- 修复任何格式化/lint 问题（black/ruff）

## 2) 添加笔记搜索端点
- 添加/扩展 `GET /notes/search?q=...`（不区分大小写）使用 SQLAlchemy 过滤器
- 更新 `frontend/app.js` 使用搜索查询
- 在 `backend/tests/test_notes.py` 中添加测试

## 3) 完成待办事项流程
- 实现 `PUT /action-items/{id}/complete`（已经搭建好）
- 更新 UI 以反映完成状态（已连接）并扩展测试覆盖

## 4) 改进提取逻辑
- 扩展 `backend/app/services/extract.py` 解析如 `#tag` 的标签并返回它们
- 为新的解析行为添加测试
- （可选）暴露 `POST /notes/{id}/extract` 将笔记转换为待办事项

## 5) 笔记 CRUD 增强
- 添加 `PUT /notes/{id}` 编辑笔记（标题/内容）
- 添加 `DELETE /notes/{id}` 删除笔记
- 更新 `frontend/app.js` 支持编辑/删除；添加测试

## 6) 请求验证和错误处理
- 在 `schemas.py` 中添加简单验证规则（例如，最小长度）
- 在适当的地方返回信息丰富的 400/404 错误；为验证失败添加测试

## 7) 文档差异检查（暂时手动）
- 创建/维护描述端点和负载的简单 `API.md`
- 每次更改后，验证文档与实际 OpenAPI (`/openapi.json`) 匹配
