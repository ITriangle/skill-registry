---
name: code-review
description: 沿两个轴评审自固定点（commit、分支、标签或 merge-base）以来的变更——Standards（代码是否遵循本仓库 documented coding standards？）和 Spec（代码是否匹配 originating issue/spec 的要求？）。两轴在并行 sub-agent 中运行，并排报告。当用户想评审分支、PR、进行中的变更，或要求「since X 以来评审」时使用。
---

对 `HEAD` 与用户提供的固定点之间 diff 的两轴评审：

- **Standards**——代码是否符合本仓库 documented coding standards？
- **Spec**——代码是否忠实实现 originating issue / spec？

两轴作为**并行 sub-agent** 运行，避免互相污染上下文，然后本 skill 汇总发现。

issue tracker 应已提供——若缺少 `docs/agents/issue-tracker.md`，运行 `/setup-matt-pocock-skills`。

## 流程

### 1. 固定基准点

用户说的固定点——commit SHA、分支名、标签、`main`、`HEAD~5` 等。未指定则询问。

一次性捕获 diff 命令：`git diff <fixed-point>...HEAD`（三点，相对 merge-base 比较）。并用 `git log <fixed-point>..HEAD --oneline` 记下 commit 列表。

继续前，确认固定点可解析（`git rev-parse <fixed-point>`）且 diff 非空。坏 ref 或空 diff 应在此失败——不在两个并行 sub-agent 内部。

### 2. 识别 spec 来源

按此顺序寻找 originating spec：

1. commit message 中的 issue 引用（`#123`、`Closes #45`、GitLab `!67` 等）——通过 `docs/agents/issue-tracker.md` 中的 workflow 获取。
2. 用户作为参数传的路径。
3. `docs/`、`specs/` 或 `.scratch/` 下与分支名或功能匹配的 spec 文件。
4. 找不到则问用户 spec 在哪。若说没有，**Spec** sub-agent 跳过并报告「no spec available」。

### 3. 识别 standards 来源

记录代码应如何写的仓库内任何内容，如 `CODING_STANDARDS.md` 或 `CONTRIBUTING.md`。

在仓库记录之上，Standards 轴始终携带下方**气味 baseline**——Fowler code smells 固定集（_Refactoring_ ch.3），即使仓库无记录也适用。两条规则约束它：

- **仓库覆盖。**documented repo standard 始终胜出；若它 endorse baseline 会 flag 的东西，抑制该 smell。
- **始终是判断调用。**每个 smell 是带标签启发（「possible Feature Envy」），从不是硬违规——且与此处任何 standard 一样，跳过 tooling 已强制的内容。

每个 smell 读*是什么* → *如何修*；与 diff 匹配：

- **Mysterious Name**——函数、变量或类型名未揭示其做什么或持有什么。→ 重命名；若无诚实名称，设计浑浊。
- **Duplicated Code**——同一逻辑形状在变更中多处或文件出现。→ 提取共享形状，两处调用。
- **Feature Envy**——方法伸手进另一对象数据多于自己的。→ 把方法移到它 envy 的数据上。
- **Data Clumps**——相同几个字段或参数总是一起出现（待出生的类型）。→ 捆成一个类型，传它。
- **Primitive Obsession**——primitive 或 string 代替值得自有类型的领域概念。→ 给概念小类型。
- **Repeated Switches**——对同一类型的相同 `switch`/`if` 级联在变更中复发。→ 多态，或两处共享的 map。
- **Shotgun Surgery**——一个逻辑变更迫使 diff 中许多文件 scattered 编辑。→ 把一起变的 gather 到一个 module。
- **Divergent Change**——一个文件或 module 因多个无关理由被编辑。→ 拆分，使每个 module 只为一因而变。
- **Speculative Generality**——为 spec 没有的需求加的抽象、参数或 hook。→ 删掉；inline 回去直到真需求出现。
- **Message Chains**——调用者不应依赖的长 `a.b().c().d()` 导航。→ 在第一个对象上藏 walk 于一个方法后。
- **Middle Man**——大多只是继续 delegate 的类或函数。→ 砍掉，直接调真目标。
- **Refused Bequest**——子类或实现者忽略或 override 大部分继承内容。→  drop 继承，用组合。

### 4. 并行 spawn 两个 sub-agent

**Standards sub-agent prompt**——包含：

- 完整 diff 命令与 commit 列表。
- 步骤 3 找到的 standards 来源文件列表，**加上步骤 3 smell baseline 全文粘贴**——sub-agent 无其他访问。
- brief：「报告——在相关处按文件/hunk——(a) diff 违反 documented standard 的每处：cite standard（文件 + 规则）；(b) 发现的 baseline smell：命名并引用 hunk。区分硬违规与判断调用——documented-standard  breach 可硬，baseline smell 始终是判断调用，documented repo standard 覆盖 baseline。跳过 tooling 强制的。400 词以内。」

**Spec sub-agent prompt**——包含：

- diff 命令与 commit 列表。
- spec 路径或获取的内容。
- brief：「报告：(a) spec 要求但缺失或部分的；(b) diff 中未要求的（scope creep）；(c) 看起来实现了但实现看起来错的。每条 finding 引用 spec 行。400 词以内。」

若 spec 缺失，跳过 Spec sub-agent，在最终报告中注明。

### 5. 汇总

在 `## Standards` 和 `## Spec` 标题下呈现两份报告，verbatim 或轻度清理。不要合并或 rerank finding——两轴故意分离（见*为何两轴*）。

以一行摘要结束：每轴 finding 总数，及每轴内最严重 issue（若有）。不要跨轴选单一 winner——那是分离所要防止的 reranking。

## 为何两轴

变更可过一轴败另一轴：

- 遵循每条 standard 但实现错的东西 → **Standards pass, Spec fail。**
- 完全做 issue 要求但破项目惯例 → **Spec pass, Standards fail。**

分开报告防止一轴 mask 另一轴。
