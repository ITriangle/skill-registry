---
name: improve-codebase-architecture
description: 扫描代码库寻找 deepening opportunities，以可视化 HTML 报告呈现，然后对你选的项进行 grilling。
disable-model-invocation: true
---

# Improve Codebase Architecture

Surface 架构摩擦并提出 **deepening opportunities**——把 shallow module 变成 deep module 的重构。目标是可测试性与 AI 可导航性。

本命令* informed* 于项目领域模型，建立在共享设计词汇上：

- 运行 `/codebase-design` skill 获取架构词汇（**module**、**interface**、**depth**、**seam**、**adapter**、**leverage**、**locality**）及其原则（deletion test、「interface 即测试面」、「一个 adapter = 假设 seam，两个 = 真」）。每条建议中精确使用这些术语——不要漂移到「component」「service」「API」或「boundary」。
- `CONTEXT.md` 中的领域语言给好 seam 命名；`docs/adr/` 中的 ADR 记录本命令不应 re-litigate 的决定。

## 流程

### 1. Explore

**扫描前先界定范围——YAGNI。**加深 module 靠让未来变更更容易而 payoff，因此对最近变更的部分加重权重。看之前先决定*看哪*：

- 若用户指定方向——module、子系统、痛点——采用，跳过下方推断。
- 否则，回溯足够长的 commit 历史（`git log --oneline`）找 hot spot——反复出现的文件和区域——让路径先吸引注意。若变更分散无清晰 hot spot，扩大范围。

先读项目领域 glossary（`CONTEXT.md`）及触及区域任何 ADR。

然后 spawn sub-agent 遍历代码库。不要 rigid heuristic——有机探索并记录摩擦体验：

- 理解一个概念为何要在许多小 module 间 bounce？
- 哪里 **shallow**——interface 几乎与实现同复杂？
- 纯函数仅为可测试性抽出，但真 bug 藏在调用方式（无 **locality**）？
- 紧耦合 module 泄漏过 seam？
- 哪些部分 untested，或难以通过当前 interface 测试？

对怀疑 shallow 的任何东西应用 **deletion test**：删除会集中复杂度，还是只移动？「是，集中」是你要的 signal。

### 2. 以 HTML 报告呈现候选

写自包含 HTML 到 OS 临时目录，不落 repo。从 `$TMPDIR` 解析 temp dir，回退 `/tmp`（Windows 为 `%TEMP%`），写到 `<tmpdir>/architecture-review-<timestamp>.html`，每次运行新文件。为用户打开——Linux `xdg-open <path>`，macOS `open <path>`，Windows `start <path>`——并告知绝对路径。

报告用 **Tailwind CDN** 做布局样式，**Mermaid CDN** 做关系图形的 diagram（图/流/序列可靠传达结构时）。Mermaid 与手工 CSS/SVG 混用——关系是图形状时用 Mermaid，要更 editorial（质量图、截面、collapse 动画）时用手工 div/SVG。每个候选有**前后可视化**。要 visual。

每个候选一张 card：

- **Files**——涉及哪些文件/module
- **Problem**——当前架构为何造成摩擦
- **Solution**——将变更什么的 plain English 描述
- **Benefits**——用 locality 和 leverage 解释，测试如何改善
- **Before / After diagram**——并排，custom-drawn，illustrate shallowness 与 deepening
- **Recommendation strength**——`Strong`、`Worth exploring`、`Speculative` 之一，badge 呈现

报告末尾 **Top recommendation**：你会先 tackle 哪个及为何。

**领域用 CONTEXT.md 词汇，架构用 `/codebase-design` 词汇。**若 `CONTEXT.md` 定义「Order」，谈「Order intake module」——不是「FooBarHandler」，也不是「Order service」。

**ADR 冲突**：仅当摩擦真值得 reopen ADR 时，才 surface 与现有 ADR 矛盾的候选。在 card 中清楚标记（如 warning callout：_"contradicts ADR-0007 — but worth reopening because…"_）。不要列出 ADR 禁止的每个理论 refactor。

见 [HTML-REPORT.md](HTML-REPORT.md) 完整 HTML scaffold、diagram 模式与样式指引。

**不要**此时提议 interface。文件写好后问用户：「你想探索哪些？」

### 3. Grilling loop

用户选定候选后，运行 `/grilling` skill 与他们走决策树——约束、依赖、加深 module 形状、seam 后有什么、哪些测试 survive。

副作用 inline 随决定 crystallize——运行 `/domain-modeling` skill 保持领域模型 current：

- **用 CONTEXT.md 没有的概念命名加深 module？**把术语加入 `CONTEXT.md`。不存在则 lazy create。
- **对话中 sharpen 模糊术语？**当场更新 `CONTEXT.md`。
- **用户以 load-bearing 理由拒绝候选？**提供 ADR， framing：_"Want me to record this as an ADR so future architecture reviews don't re-suggest it?"_ 仅当理由真能让未来 explorer 避免 re-suggest 时提供——跳过 ephemeral（「现在不值得」）和自明的。
- **想探索加深 module 的替代 interface？**运行 `/codebase-design` skill 及其 design-it-twice 并行 sub-agent 模式。
