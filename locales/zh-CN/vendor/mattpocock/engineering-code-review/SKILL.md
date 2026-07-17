---
name: code-review
description: 从一个固定点（commit、branch、tag 或 merge-base）开始，沿两个维度评审变更——标准（代码是否遵循仓库记录的编码标准？）与 Spec（代码是否符合原始 issue/PRD 的要求？）。并行运行两个 sub-agent，并排报告结果。当用户希望评审 branch、PR、进行中的变更，或要求“评审自 X 以来的改动”时使用。
---

对用户提供的固定点与 `HEAD` 之间的 diff 进行双轴评审：

- **标准**——代码是否符合此仓库记录的编码标准？
- **Spec**——代码是否忠实实现了原始 issue / PRD / spec？

两个维度由**并行 sub-agent** 执行，避免彼此污染上下文，然后由本技能汇总发现。

issue tracker 配置应已提供；如果缺少 `docs/agents/issue-tracker.md`，运行 `/setup-matt-pocock-skills`。

## 流程

### 1. 固定比较点

用户指定的内容就是固定点——commit SHA、branch name、tag、`main`、`HEAD~5` 等。如果用户没有指定，就询问。

只记录一次 diff 命令：`git diff <fixed-point>...HEAD`（三点形式，因此与 merge-base 比较）。同时通过 `git log <fixed-point>..HEAD --oneline` 记录 commit 列表。

继续之前，确认固定点能够解析（`git rev-parse <fixed-point>`）且 diff 非空。错误 ref 或空 diff 应在这里失败，而不是在两个并行 sub-agent 内失败。

### 2. 确定 Spec 来源

按以下顺序查找原始 spec：

1. commit message 中的 issue 引用（`#123`、`Closes #45`、GitLab `!67` 等）——使用 `docs/agents/issue-tracker.md` 中的流程获取。
2. 用户通过参数传入的路径。
3. `docs/`、`specs/` 或 `.scratch/` 下与 branch name 或功能匹配的 PRD/spec 文件。
4. 如果都找不到，询问用户 spec 在哪里。如果用户表示没有 spec，**Spec** sub-agent 应跳过并报告“没有可用 spec”。

### 3. 确定标准来源

仓库中任何记录代码编写方式的材料，例如 `CODING_STANDARDS.md` 或 `CONTRIBUTING.md`。

除仓库自身文档外，“标准”维度始终携带下方的 **smell baseline**——一组固定的 Fowler 代码异味（《重构》第 3 章），即使仓库没有任何文档也适用。它受两条规则约束：

- **仓库规则优先。** 已记录的仓库标准始终胜出；如果仓库明确认可 baseline 会标记的做法，就抑制该 smell。
- **始终需要判断。** 每个 smell 都是带标签的启发式判断（“可能的 Feature Envy”），绝不是硬性违规；并且与这里的任何标准一样，跳过工具已经强制执行的事项。

每个 smell 采用“它是什么”→“如何修复”的形式；将其与 diff 对照：

- **Mysterious Name**——函数、变量或类型名称没有揭示其用途或内容。→ 重命名；如果无法找到诚实的名称，说明设计仍然混乱。
- **Duplicated Code**——相同逻辑形态出现在变更中的多个 hunk 或文件。→ 提取共享形态并由两处调用。
- **Feature Envy**——方法访问另一个对象的数据多于自身数据。→ 将方法移动到它所“羡慕”的数据所在对象。
- **Data Clumps**——同样的几个字段或参数总是成组传递（暗示应诞生一个类型）。→ 将它们打包成一个类型并传递该类型。
- **Primitive Obsession**——用 primitive 或 string 代表值得拥有独立类型的领域概念。→ 为该概念创建小型专用类型。
- **Repeated Switches**——针对同一类型的相同 `switch`/`if` 级联在变更中反复出现。→ 用多态替代，或让两个位置共享一个 map。
- **Shotgun Surgery**——一个逻辑变更迫使 diff 在多个文件中进行分散编辑。→ 将一起变化的内容集中到一个模块。
- **Divergent Change**——一个文件或模块因为多个不相关原因而被编辑。→ 拆分，使每个模块只有一个变化原因。
- **Speculative Generality**——为 spec 尚无需求的场景添加抽象、参数或 hook。→ 删除；内联回去，直到出现真实需求。
- **Message Chains**——调用方不应依赖的长 `a.b().c().d()` 导航链。→ 在第一个对象上用一个方法隐藏整段遍历。
- **Middle Man**——class 或函数大部分只是继续委派。→ 删除中间层，直接调用真正目标。
- **Refused Bequest**——subclass 或 implementer 忽略或覆盖了继承内容的大部分。→ 放弃继承，使用组合。

### 4. 并行创建两个 sub-agent

在一条消息中发出两次 `Agent` 工具调用。两者都使用 `general-purpose` subagent。

**标准 sub-agent prompt**——包括：

- 完整 diff 命令和 commit 列表。
- 第 3 步找到的标准来源文件列表，**以及完整粘贴第 3 步的 smell baseline**——sub-agent 无法从其他地方访问它。
- 任务说明：“在相关情况下按文件/hunk 报告：(a) diff 中每一处违反已记录标准的位置：引用标准（文件 + 规则）；(b) 发现的任何 baseline smell：说出名称并引用 hunk。区分硬性违规和判断项——违反已记录标准可以是硬性违规，但 baseline smell 始终是判断项，而且仓库文档标准优先于 baseline。跳过工具已强制执行的事项。少于 400 字。”

**Spec sub-agent prompt**——包括：

- diff 命令和 commit 列表。
- spec 的路径或获取到的内容。
- 任务说明：“报告：(a) spec 要求但缺失或只部分实现的需求；(b) diff 中未经要求的行为（范围蔓延）；(c) 看似已经实现但实现方式有误的需求。每项发现引用对应 spec 行。少于 400 字。”

如果缺少 spec，跳过 Spec sub-agent，并在最终报告中注明。

### 5. 汇总

在 `## Standards` 和 `## Spec` 标题下展示两份报告，可原样呈现或轻微清理。**不要**合并或重新排序发现——两个维度是刻意分开的（见*为什么使用两个维度*）。

最后用一行总结：每个维度的发现总数，以及各维度内最严重的问题（如有）。不要跨维度选出唯一最严重问题——这正是分离维度要避免的重新排序。

## 为什么使用两个维度

一项变更可能通过一个维度而在另一个维度失败：

- 代码遵循所有标准，却实现了错误内容 → **标准通过，Spec 失败。**
- 代码准确完成 issue 要求，却破坏项目约定 → **Spec 通过，标准失败。**

分开报告可以防止一个维度掩盖另一个维度。
