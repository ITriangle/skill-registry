# 构建与更新步骤

## `/code-graph build`

完整扫描。不存在图谱或用户要求完整重建时使用。

### 步骤 1——验证前置条件

参见 [prerequisites.md](prerequisites.md)。快速检查：

```bash
which graphify || uv tool install graphifyy
```

### 步骤 2——运行 graphify

```bash
graphify .
```

关键选项：
- `--wiki`——为社区和 god node 生成 wiki 文章（建议 aiops 使用）
- `--mode deep`——使用激进提取，实现全面覆盖
- `--exclude 'node_modules' --exclude 'dist' --exclude '.scratch'`——跳过构建输出

graphify 产出：
- `graphify-out/graph.json`——结构化图谱
- `graphify-out/`——studio 可视化、SVG、wiki 文章、文本报告

### 步骤 3——语义注释（模型）

读取 `graphify-out/graph.json`，并把模型生成的注释添加到 `.scratch/graph/annotations.json`。Schema 参见：[graph-schema.md](graph-schema.md#annotationsschema)。

为每个节点注释：`purpose`、`depth`（`deep` | `shallow` | `unknown`）、`tags`、`complexity`、`is_test_file`。

对于热点，将 graphify 的 god node 与 `git log --oneline -30` 交叉核对。

### 步骤 4——需要时更新 .gitignore

如果 `.gitignore` 中没有 `graphify-out/` 和 `.scratch/graph/`，建议添加。

## `/code-graph query <subcommand>`

要求存在 `graphify-out/graph.json`。输出格式见 [query-patterns.md](query-patterns.md)。

维护者命令：`python3 <aiops-root>/skills/aiops/scripts/code_graph_query.py <subcommand>`

| 子命令 | 用途 |
| --- | --- |
| `modules` | 列出所有节点及其用途、深度、边数量 |
| `deps <node>` | 出边 |
| `rdeps <node>` | 入边 |
| `impact <file>` | 传递性影响范围 |
| `hotspot` | 高耦合 + 最近有变更 |
| `god-nodes` | 按边数量排序的前 N 个节点 |
| `shallow` | depth=shallow 的节点 |
| `orphans` | 零入边节点 |
| `communities` | Louvain 集群 |

## `/code-graph update`

```bash
graphify --update .
```

graphify 使用 `.graphify/cache/` 中的 SHA256 缓存。只为发生变化的节点重新运行语义注释。如果超过 30% 的节点发生变化，则回退到完整 `build`。
