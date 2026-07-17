# CONSTITUTION.md 模板

项目级不可妥协原则。每个阶段的每个代理都会引用。

由 `/aiops-setup` 生成。可自由编辑——这是项目的锚点。

---

```markdown
# 宪法：<project-name>

## 测试

- 最低测试覆盖率：<例如 80%>
- 所有公共接口都必须有测试
- <例如 API 端点的集成测试>

## 代码质量

- <例如禁止原始 SQL——使用 ORM query builder>
- <例如所有函数不超过 50 行>
- <例如启用 TypeScript strict mode>

## 架构

- <例如模块之间不得存在循环依赖>
- <例如数据库迁移必须可逆>
- <例如外部 API 调用必须经过 service layer>

## 性能

- <例如 P95 响应时间 < 200ms>
- <例如不得出现 N+1 查询>
- <例如 gzip 后 bundle 大小 < 100KB>

## 安全

- <例如代码中不得包含 secret——使用环境变量>
- <例如所有用户输入都要在边界处验证>
- <例如所有非公开端点都必须认证>

## 流程

- <例如 Conventional Commits>
- <例如合并前必须经过 PR 审查>
- <例如每次发布都更新 CHANGELOG.md>
```
