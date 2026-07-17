# 图谱 Schema

代码图谱使用两个位置：

1. **`graphify-out/graph.json`**——graphify 的原生输出（结构数据：节点、边、社区、置信度）。直接从 graphify 输出目录读取。
2. **`.scratch/graph/annotations.json`**——模型生成的语义层（用途、深度、标签、热点）。

## graph.json（graphify 格式）

由 `graphify`（PyPI：`graphifyy`）生成，存储在 `graphify-out/graph.json`。这是 graphify 的原生 schema。

```json
{
  "directed": true,
  "multigraph": false,
  "graph": {
    "provenance": "graphify v0.17.1",
    "community_labels": { "0": "Authentication", "1": "API Layer" },
    "built_from_commit": "abc1234"
  },
  "topology_signature": "sha256-hash-of-sorted-ids-and-edges",
  "nodes": [ ... ],
  "links": [ ... ],
  "hyperedges": [ ... ]
}
```

### nodes[]

每个节点代表从代码库中提取的文件、函数、类或概念。

```json
{
  "id": "src/auth/login.ts",
  "community": "0",
  "community_name": "Authentication",
  "file_type": "ts",
  "source_file": "src/auth/login.ts",
  "description": "User login handler with OAuth support",
  "degree": 8,
  "in_degree": 5,
  "out_degree": 3
}
```

字段：
- `id`——唯一节点标识符（通常是文件路径或符号名）
- `community`——Louvain 社区分配结果
- `community_name`——人类可读的社区标签
- `file_type`——文件扩展名
- `source_file`——源文件相对路径
- `description`——自动生成或 LLM 生成的描述
- `degree` / `in_degree` / `out_degree`——连通性指标

### links[]

每条 link 表示两个节点之间的关系。

```json
{
  "source": "src/api/routes.ts",
  "target": "src/auth/login.ts",
  "relation": "IMPORTS",
  "confidence_score": 1.0
}
```

字段：
- `source`——源节点 ID（消费方）
- `target`——目标节点 ID（依赖项）
- `relation`——边类型：`CONTAINS` | `CALLS` | `INHERITS` | `IMPORTS` | `SEMANTICALLY_SIMILAR_TO` | ...
- `confidence_score`——提取确定性：
  - `1.0` = **EXTRACTED**——直接来自 AST（import 语句、显式调用）
  - `0.5` = **INFERRED**——根据模式推断（共享数据结构、命名约定）
  - `0.2` = **AMBIGUOUS**——不确定，需要验证

### hyperedges[]

共同参与某个模式的节点组（例如“MDX Content Rendering Pipeline”）。

### 图谱元数据

- `provenance`——构建元数据（graphify 版本、构建上下文）
- `community_labels`——社区 ID 到人类可读标签的映射
- `built_from_commit`——构建时的 git 提交哈希
- `topology_signature`——排序后的节点 ID 和边的哈希，用于变更检测

## annotations.json（模型生成）

由模型在 `/code-graph build` 步骤 5 中生成。它叠加在 graph.json 上，不修改后者。

```json
{
  "build_time": "2026-06-29T10:00:00Z",
  "git_ref": "abc1234def",
  "annotations": {
    "src/auth/login.ts": {
      "purpose": "User login handler with OAuth and session management",
      "depth": "deep",
      "tags": ["auth", "security"],
      "complexity": "high",
      "is_test_file": false
    },
    "src/utils/helpers.ts": {
      "purpose": "Grab-bag of utility functions with no clear domain",
      "depth": "shallow",
      "tags": ["utils"],
      "complexity": "low",
      "is_test_file": false
    }
  },
  "hotspots": [
    {
      "node_id": "src/core/engine.ts",
      "in_degree": 18,
      "recent_commits": 12,
      "reason": "high in-degree + frequent changes = architectural friction"
    }
  ],
  "impact_map": {
    "src/auth/login.ts": {
      "direct": ["src/api/routes.ts", "tests/auth.test.ts"],
      "transitive": ["src/pages/dashboard.ts", "e2e/login.spec.ts"]
    }
  }
}
```

### annotations（逐节点）

- `purpose`——单行语义描述（模型根据 CONTEXT.md 词汇生成）
- `depth`——`deep` | `shallow` | `unknown`
  - **deep**：小接口、丰富实现（良好架构）
  - **shallow**：接口几乎与实现一样复杂（深化候选项）
  - **unknown**：信号不足，无法分类
- `tags`——使用 CONTEXT.md 词汇的领域标签
- `complexity`——`low` | `medium` | `high`
- `is_test_file`——布尔标记

### hotspots

同时具备高耦合和最近变更的模块：
- `node_id`——匹配 graph.json 节点 ID
- `in_degree`——来自 graph.json
- `recent_commits`——来自 `git log --oneline -30`
- `reason`——被标记的原因

### impact_map

针对高度数节点预先计算的传递闭包：
- Key = 节点 ID
- `direct`——通过边直接连接的节点
- `transitive`——经过多跳可以到达的节点

## 计算字段（在 `/code-graph query` 输出中）

不存储在 JSON 中，而是在生成报告时计算：

- **God nodes**——按度数排序的前 N 个节点（来自 graphify）
- **Communities**——带内聚度分数的 Louvain 集群（来自 graphify）
- **Surprising connections**——意外的边（来自 graphify）
- **Knowledge gaps**——孤立节点、稀薄集群（来自 graphify）
- **Edge confidence**——EXTRACTED/INFERRED/AMBIGUOUS 的百分比分布（来自 graphify）
- **Shallow modules**——`depth=shallow` 的节点（来自 annotations）
- **Orphans**——零入度节点（来自 graph.json links）
