---
name: to-tickets
description: 将计划、spec 或当前对话拆成 tracer-bullet ticket 集，每个声明阻塞边，发布到配置的 tracker——本地每 ticket 一文件文本边，或真实 tracker 上原生 blocking link。
disable-model-invocation: true
---

# To Tickets

将计划、spec 或对话拆成 **ticket** 集——tracer-bullet 垂直切片，每个声明**阻塞**它的其他 ticket。

issue tracker 与 triage label 词汇应已提供——否则运行 `/setup-matt-pocock-skills`。

## 流程

### 1. Gather context

用对话上下文中已有内容。若用户传引用（spec 路径、issue 号或 URL）作参数，获取并读完整 body 与 comments。

### 2. Explore 代码库（可选）

若尚未探索，探索以理解代码当前状态。ticket 标题与描述用项目领域 glossary 词汇，尊重触及区域 ADR。

寻找 prefactor 机会使实现更容易。「Make the change easy, then make the easy change.」

### 3. Draft vertical slices

拆成 **tracer bullet** ticket。

<vertical-slice-rules>

- 每片切过每层（schema、API、UI、tests）的窄但 COMPLETE 路径——垂直，非单层水平切片
- 完成的片可单独 demo 或验证
- 每片大小 fit 单个新鲜上下文窗口
- 任何 prefactoring 应先做

</vertical-slice-rules>

给每个 ticket **blocking edges**——必须先完成的其他 ticket。无 blocker 的 ticket 可立即开始。

**Wide refactor 是垂直切片的例外。** **Wide refactor** 是一种机械变更——重命名列、重类型共享符号——其**blast radius** fan 遍代码库，单次编辑同时破数千 call site，无垂直切片能 green land。不要硬塞进 tracer bullet；按 **expand–contract** 排序。先 expand：旧形式旁加新形式，什么都不破。再按 blast radius 分批 migrate call site（每包、每目录），每批 own ticket、blocked by expand，CI 批批 green，因旧形式仍存在。最后 contract：无 caller 留旧形式时删旧形式，ticket blocked by 每个 migrate batch。连 batch 都无法单独 green 时，保持序列但让它们共享 integration branch，全部 block 最终 integrate-and-verify ticket——green 只承诺在那里。

### 4. Quiz the user

以编号列表呈现 proposed breakdown。每个 ticket 展示：

- **Title**：短描述名
- **Blocked by**：须先完成哪些其他 ticket（若有）
- **What it delivers**：此 ticket 使端到端行为 work 的内容

问用户：

- 粒度是否合适？（太粗 / 太细）
- blocking edges 是否正确——每个 ticket 只依赖真正 gate 它的 ticket？
- 是否应合并或进一步拆分 ticket？

迭代直到用户批准 breakdown。

### 5. 发布 ticket 到配置的 tracker

发布 approved ticket。**如何**取决于 `/setup-matt-pocock-skills` 配置的 tracker——ticket 相同，仅 blocking edges 形状变：

- **Local files** → 每个 ticket 一文件于 `.scratch/<feature-slug>/issues/<NN>-<slug>.md`，从 `01` 按依赖顺序编号（blocker 先）。每文件「Blocked by」列依赖的编号/标题。用下方 per-ticket 文件模板——每 ticket 一文件，从不是单个合并文件。
- **真实 issue tracker（GitHub、Linear、…）** → 按依赖顺序（blocker 先）每 ticket 一 issue，使 blocking edges 可引用真实 id。平台有原生 blocking / sub-issue 关系则用；否则每 ticket「Blocked by」设为 blocking issues。除非另有指示，应用 `ready-for-agent` triage label——ticket 按构造可 agent-grab。

处理 **frontier**：blocker 都 done 的 ticket。纯线性链即自上而下。

不要关闭或修改任何 parent issue。

<local-ticket-template>

# <NN> — <Ticket title>

**What to build:** 此 ticket 使端到端行为 work 的内容，从用户视角——不是逐层实现列表。

**Blocked by:** gate 此 ticket 的编号/标题，或「None — can start immediately」。

**Status:** ready-for-agent

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2

</local-ticket-template>

<issue-template>

## Parent

tracker 上 parent issue 引用（若来源是现有 issue，否则省略本节）。

## What to build

此 ticket 使端到端行为 work 的内容，从用户视角——非逐层实现。

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Blocked by

- 每个 blocking ticket 引用，或「None — can start immediately」。

</issue-template>

两种形式都避免具体文件路径或代码片段——很快 stale。例外：原型产出比 prose 更精确编码决定的片段（状态机、reducer、schema、type shape），inline 并简短注明来自原型。trim 到决定丰富部分——不是可运行 demo，只是重要 bits。
