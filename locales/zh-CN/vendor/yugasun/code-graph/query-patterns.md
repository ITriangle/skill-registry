# 查询模式

说明如何查询代码图谱，以及每个子命令返回什么。查询读取 `graphify-out/graph.json`（graphify 结构数据）和 `.scratch/graph/annotations.json`（模型语义层）。查询绝不修改图谱。

## `modules`——列出所有节点

**何时使用**：任何需要项目概览的技能的第一步。

**输出格式**：

```
## 模块（42 个节点 · 5 个社区）

| 模块 | 社区 | 深度 | 用途 | 入 | 出 | 置信度 |
|--------|-----------|-------|---------|----|----|------------|
| src/auth/login.ts | Authentication | deep | 用户登录处理器 | 5 | 3 | 100% EXTRACTED |
| src/api/routes.ts | API Layer | shallow | HTTP 路由定义 | 2 | 8 | 100% EXTRACTED |
| lib/parser.ts | Config | deep | 配置解析器 | 5 | 1 | 80% EXTRACTED, 20% INFERRED |
```

按入度降序排列（最常被依赖的在前）。Depth 和 Purpose 来自 annotations.json；In/Out 来自 graph.json links。

## `deps <node>`——出向依赖

**何时使用**：修改模块前了解它依赖什么。

**输出格式**：

```
## src/api/routes.ts 的依赖

| 依赖项 | 关系 | 置信度 |
|------------|----------|------------|
| src/auth/login.ts | IMPORTS | 1.0 EXTRACTED |
| src/auth/middleware.ts | IMPORTS | 1.0 EXTRACTED |
| src/utils/format.ts | IMPORTS | 0.5 INFERRED |
```

数据源：按 `source === node_id` 筛选的 graph.json links，加上每个目标节点的 annotations。

## `rdeps <node>`——入向依赖（反向）

**何时使用**：了解模块的影响范围——更改它会破坏谁。

**输出格式**：

```
## src/auth/login.ts 的依赖方

| 依赖方 | 关系 | 置信度 |
|-----------|----------|------------|
| src/api/routes.ts | IMPORTS | 1.0 EXTRACTED |
| src/api/webhooks.ts | CALLS | 1.0 EXTRACTED |
| tests/auth.test.ts | IMPORTS | 1.0 EXTRACTED |
```

数据源：按 `target === node_id` 筛选的 graph.json links。

## `impact <file>`——变更影响分析

**何时使用**：修改文件前确定还有什么需要更新。

使用 annotations.json 的 impact_map 预计算数据。如果尚未预计算，则回退到 graph.json links 上的传递闭包。

**输出格式**：

```
## 更改 src/auth/login.ts 的影响

### 直接影响（置信度：EXTRACTED）
- src/api/routes.ts — IMPORTS login()
- tests/auth.test.ts — IMPORTS login()

### 传递影响
- src/api/middleware.ts — 使用调用 login 的 routes
- src/pages/dashboard.ts — 在 auth middleware 之后加载

### 社区上下文
- 属于“Authentication”社区（内聚度：0.67）
- 另有 3 个社区成员可能受影响

### 风险评估
- 2 个模块直接受影响（EXTRACTED 置信度）
- 2 个模块间接受影响（INFERRED）
- 测试覆盖：4 个受影响模块中有 1 个带测试
```

## `hotspot`——高耦合 + 最近有变更

**何时使用**：识别架构摩擦——既复杂又处于活跃变更中的节点。

**输出格式**：

```
## 热点

| 模块 | 入度 | 社区 | 最近变更 | 风险 |
|--------|-----------|-----------|----------------|------|
| src/core/engine.ts | 18 | Core | 12 次提交（30 天） | 🔴 高 |
| src/api/routes.ts | 2 | API Layer | 8 次提交（30 天） | 🟡 中 |
```

数据源：annotations.json hotspots + graph.json in_degree + `git log --oneline -30`。

## `god-nodes`——按度数排序的顶级节点

**何时使用**：了解架构关键路径——哪些节点被所有内容依赖。

**输出格式**：

```
## God Node（前 10 个）

1. **src/types/** — 度数：24 — 类型定义（社区：Shared）
2. **lib/logger.ts** — 度数：18 — 日志工具（社区：Infrastructure）
3. **src/config/** — 度数：15 — 配置（社区：Config）
```

数据源：按度数排序的 graph.json nodes（来自 graphify 文本报告）。

## `shallow`——浅节点

**何时使用**：为 `/improve-codebase-architecture` 寻找深化候选项。

**输出格式**：

```
## 浅节点

| 模块 | 深度 | 用途 | 社区 | 建议 |
|--------|-------|---------|-----------|------------|
| src/utils/helpers.ts | shallow | 混杂工具 | Utils | 按领域拆分 |
| src/api/routes.ts | shallow | 路由定义 + 处理器 | API Layer | 提取处理器逻辑 |
```

数据源：annotations.json 中 `depth === "shallow"` 的条目。

## `orphans`——零入度节点

**何时使用**：查找潜在死代码或独立工具。

**输出格式**：

```
## 孤立节点（没有任何对象依赖它们）

- scripts/migrate.ts — 可能是 CLI 脚本（符合预期）
- src/legacy/old-api.ts — 潜在死代码
- docs/examples/ — 文档（符合预期）
```

数据源：没有入向 link 的 graph.json nodes。

## `communities`——检测到的社区集群

**何时使用**：了解代码库天然的模块分组。

**输出格式**：

```
## 社区（Louvain 聚类）

### Authentication（内聚度：0.67）
- src/auth/login.ts
- src/auth/middleware.ts
- src/auth/session.ts
- src/models/user.ts

### API Layer（内聚度：0.42）
- src/api/routes.ts
- src/api/handlers/
- src/api/middleware.ts

### Infrastructure（内聚度：0.31）
- lib/logger.ts
- lib/config.ts
- lib/cache.ts
```

数据源：graph.json 社区分配结果 + graphify community_labels + 内聚度分数。
