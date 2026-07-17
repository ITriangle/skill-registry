---
name: architect-design
description: >
  供 architect agent 使用的结构化设计流程。通过约束收集、module 识别、
  interface 设计、替代方案探索与风险分析，从 grill 结论推进到完整的
  NOTES.md、tech-spec.md 以及必要的领域文档更新。当 architect 需要产出
  设计决策和技术规格时使用。
---

# 架构设计

结构化设计流程：从 grill/domain-modeling 结论推进到完整的 `NOTES.md` + `tech-spec.md`，以及任何必要的领域文档更新。

## 词汇

全过程使用 [design-vocabulary.md](design-vocabulary.md)——module、interface、depth、seam、deletion test、leverage、locality。不要漂移到“component”“service”“API”或“boundary”。

## 输入

- Grill 结论（已暴露的假设、已识别的约束）
- `CONTEXT.md` 领域术语表（来自 `/aiops-setup`）
- `docs/adr/` 中现有的架构决策记录
- `.scratch/<feature>/VERDICT.md`（如果运行过 prototyper）
- `graphify-out/graph.json`（如果已运行 `/code-graph`——通过 `/code-graph query god-nodes`、`/code-graph query communities` 查询概览）

## 流程

### 第 1 步：收集约束

从所有输入中提取约束。分类为：

- **硬约束**：不可违反（现有 ADR、平台限制、团队产能、合规要求）
- **软约束**：可以权衡的偏好（性能目标、代码风格、库偏好）

在 `NOTES.md` 的 Context 一节中明确列出约束。通过编号引用 ADR——除非摩擦真实到值得重审，否则不要重新争论已落定的决策（如需重审，应清楚标记）。

### 第 1.5 步：图谱验证（如果代码图谱可用）

如果存在 `graphify-out/graph.json`，对照实际代码结构验证约束：

1. 查询 `/code-graph query modules`，获取当前 module 清单
2. 对于每项涉及现有 module 的约束，确认该 module 存在且符合约束中的假设
3. 查询 `/code-graph query deps <module>`，检查依赖关系声明
4. 标记任何与图谱矛盾的约束（例如约束称“Module A 不依赖 Module B”，但图谱显示存在依赖）

在 `NOTES.md` 中记录经过图谱验证的约束，并加上 `[graph-verified]` 标签。

### 第 2 步：识别 Module

识别满足需求所需的 module。对每个候选 module：

1. **Deletion test**：想象将其删除。复杂度是否消失（pass-through → 合并进调用方）？还是复杂度会在 N 个调用方中重新出现（发挥了应有价值 → 保留）？
2. **Depth 评估**：相对于所隐藏的行为，interface 是否足够小？Deep = 为调用方提供高 leverage。Shallow = interface 几乎与 implementation 一样复杂 → 合并或拆分。
3. **范围检查**：module 是否拥有问题中连贯的一部分，还是一个大杂烩？

将每个 module 标记为 **new**（绿地）或 **deepening**（把现有浅 module 重构为一个深 module）。

### 第 3 步：绘制依赖

为每个 module 绘制其依赖，并决定集成策略：

| 依赖类型 | 示例 | 集成方式 |
|----------------|----------|-------------|
| **进程内** | 纯计算、内存状态 | 直接合并进 module，无需 seam |
| **本地可替代** | 用 PGlite 替代 Postgres、内存 FS | 使用替代实现测试；seam 保持内部化 |
| **远程但自有** | 内部微服务、内部 API | 在 seam 定义 interface；生产 transport + 内存 test double |
| **真正外部** | Stripe、Twilio、第三方服务 | 注入到 interface 后；测试时 mock |

规则：**除非至少两个 implementation 都有充分理由，否则不要引入 seam**（通常为生产实现 + 测试实现）。只有单一 implementation 的 seam 只是间接层。

### 第 4 步：设计 Interface

为每个 module 设计 interface：

- **最小化入口点**：method 越少 = 所需测试越少 = 每个 method 的 leverage 越高
- **简化参数**：interface 能为调用方隐藏什么？
- **接收依赖，不要创建依赖**：注入 module 所需内容，不要硬编码
- **优先返回结果，而非产生副作用**：尽可能使用纯输出
- **记录调用方必须知道的一切**：invariant、顺序、错误模式、配置、性能

Interface 就是测试表面——调用方和测试穿过同一个 seam。

### 第 5 步：探索替代方案

对于**最关键**的 module（风险最高、调用方最多或影响最深），设计至少 2 个截然不同的 interface：

- **设计 A**：最小化 interface——1–3 个入口点，每个入口点提供最大 leverage
- **设计 B**：最大化灵活性——支持多种用例和扩展点
- **设计 C**（如适用）：为最常见调用方优化——让默认用例极其简单

比较：哪种设计让调用方每学习一单位 interface 就获得最多能力？变更集中在哪里？seam 在哪里？

选择最强方案，或提出混合方案。在 `NOTES.md` 中记录：
- **选定方案**
- **理由**：为什么选择它
- **拒绝的替代方案**：至少一个，并附拒绝理由
- **施加的约束**：此决策锁定了什么

### 第 6 步：领域文档检查

最终确定设计工件之前，进行一次简短的 `/domain-modeling`：

1. 从设计中提取新增或变化的领域术语。
2. 只把项目特有领域语言加入 `CONTEXT.md`；跳过通用工程术语。
3. 根据 ADR 门槛检查每项设计决策：难以逆转、缺少上下文时令人意外，并且存在真正需要权衡的替代方案。
4. 只有同时满足三项标准的决策才创建 `docs/adr/NNNN-slug.md`；否则跳过 ADR。
5. 在 `NOTES.md` 中记录结果，让下游 agent 知道领域文档是发生了变更，还是被有意保持不变。

### 第 7 步：输出规格

生成主要设计工件：

**`NOTES.md`**——设计决策、权衡分析、约束：
- 问题陈述（一句话）
- 上下文（现有系统、已知约束、相关 ADR）
- 设计决策（选定方案 + 拒绝方案 + 理由 + 施加的约束）
- 领域文档（`CONTEXT.md` 更新、创建的 ADR、跳过的 ADR 及简短理由）
- 范围（范围内 / 范围外）
- 待解决问题（planner 开始前必须解决阻塞项）

**`tech-spec.md`**——技术规格：
- 架构（module 关系说明）
- Module 清单（每个 module：interface、depth 评估、依赖、集成策略）
- 数据模型（entity、field、type）
- API contract（每个 interface 的 method + path + request/response）
- 时序（module 之间逐步交互）
- 风险（风险 + 影响 + 缓解措施）

## 约束

- 不要编写实现代码（只允许 interface signature 和 pseudocode）
- 每项设计决策都必须列出至少一个被拒绝的替代方案及理由
- 使用 `CONTEXT.md` 领域术语命名 module；如果引入新术语，将其加入 `CONTEXT.md`
- ADR 保持可选：只有满足 `/domain-modeling` ADR 门槛时才编写
- 除非摩擦值得重审，否则不要重新争论现有 ADR（如重审，需明确标记）
- 必须标记含阻塞项的待解决问题——在其解决前 planner 不得开始
- 将每个 module 标记为 **new** 或 **deepening** 现有 module
