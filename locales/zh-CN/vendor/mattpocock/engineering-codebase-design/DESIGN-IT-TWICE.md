# Design It Twice

当用户想探索所选 deepening candidate 的替代接口时，使用此并行 sub-agent 模式。基于「Design It Twice」（Ousterhout）——第一个想法 unlikely 是最好的。

使用 [SKILL.md](SKILL.md) 中的词汇——**module**、**interface**、**seam**、**adapter**、**leverage**。

## 流程

### 1. 框定问题空间

spawn sub-agent 之前，为所选 candidate 写面向用户的问题空间说明：

- 任何新接口需满足的约束
- 它将依赖的依赖，及各自类别（见 [DEEPENING.md](DEEPENING.md)）
- 粗略示意代码 sketch 使约束具体——不是提案，只是让约束可感的方式

展示给用户，然后立即进行步骤 2。用户在 sub-agent 并行工作时阅读思考。

### 2. Spawn sub-agent

并行 spawn 3+ sub-agent。每个必须为加深 module 产出** radically different** 的接口。

用独立技术 brief prompt 每个 sub-agent（文件路径、coupling 细节、来自 [DEEPENING.md](DEEPENING.md) 的依赖类别、seam 后有什么）。brief 独立于步骤 1 面向用户的问题空间说明。给每个 agent 不同设计约束：

- Agent 1：「最小化 interface——目标 1–3 个入口点 max。每入口点最大化 leverage。」
- Agent 2：「最大化灵活性——支持许多用例和扩展。」
- Agent 3：「优化最常见调用者——使默认情形 trivial。」
- Agent 4（若适用）：「围绕 ports & adapters 设计跨 seam 依赖。」

brief 中包含 [SKILL.md](SKILL.md) 词汇和 CONTEXT.md 词汇，使每个 sub-agent 与架构语言和项目领域语言一致命名。

每个 sub-agent 输出：

1. Interface（types、methods、params——加 invariants、ordering、error modes）
2. 展示调用者如何使用的 usage example
3. 实现藏在 seam 后什么
4. 依赖策略与 adapter（见 [DEEPENING.md](DEEPENING.md)）
5. Trade-offs——leverage 高在哪、薄在哪

### 3. 呈现并比较

顺序呈现设计，使用户能吸收每一个，然后用 prose 比较。按 **depth**（interface 处 leverage）、**locality**（变更集中处）、**seam placement** 对比。

比较后给出自己的推荐：哪个设计最强及为何。若不同设计的元素可很好组合，提议 hybrid。要有主见——用户要 strong read，不是菜单。
