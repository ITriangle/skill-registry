---
name: code-graph
description: >
  为目标项目构建并查询持久化代码图谱。使用 graphify（Tree-sitter + Louvain 聚类）
  进行确定性的结构提取，再由模型添加语义注释。用于用户提出构建图谱、代码图、依赖图、
  影响分析，或其他技能需要先获得结构化代码理解时。
---

# 代码图谱

构建、查询和增量更新目标项目的持久化知识图谱。它属于**基础设施**——其他技能通过查询使用它；Flow Conductor 会在会话开始时检查其新鲜度。

## 两层提取

| 层级 | 工具 | 作用 |
| --- | --- | --- |
| **结构层** | [graphify](https://github.com/safishamsi/graphify) | AST 节点、边、社区、置信度——确定性结果 |
| **语义层** | 模型 | 用途、深度、影响——依赖上下文 |

graphify 负责解析；模型负责注释。绝不使用基于 grep 的猜测替代 graphify 的结构数据。

## 前置条件

[prerequisites.md](prerequisites.md)——通过 uv/pipx/pip 安装 `graphifyy`。如果用户拒绝，不阻塞后续操作。

## 存储

| 路径 | 来源 | 用途 |
| --- | --- | --- |
| `graphify-out/graph.json` | graphify | 结构图谱 |
| `.scratch/graph/annotations.json` | 模型 | 语义层 |

不要把 `graph.json` 复制到 `.scratch/`。Schema 参见：[graph-schema.md](graph-schema.md)。

## 操作

详细步骤：[build-steps.md](build-steps.md)。

- **`/code-graph build`**——完整扫描 + 语义注释
- **`/code-graph query <subcommand>`**——只读；查询模式见 [query-patterns.md](query-patterns.md)
- **`/code-graph update`**——利用 graphify 缓存进行增量更新

## 约束

- graphify 是结构骨干——不要用基于 grep 的方式猜测依赖关系
- 模型只添加语义层；绝不覆盖 graphify 的边
- 已有图谱时优先使用 `update` 而不是 `build`
- graphify 失败不应阻塞——发出警告并继续
- 关注置信度：EXTRACTED (1.0)、INFERRED (0.5)、AMBIGUOUS (0.2)

## Flow Conductor

`aiops-graph.js` hook 会在图谱过期时建议运行 `/code-graph build`。**Architecture health** 会先运行 `graph_build` 阶段（`phases.py`）——缺失或过期时构建，仍新鲜时跳过；用户可以拒绝（此时 `/improve-codebase-architecture` 回退为有机探索）。
