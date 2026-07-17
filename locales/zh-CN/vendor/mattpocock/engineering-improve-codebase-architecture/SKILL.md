---
name: improve-codebase-architecture
description: 扫描代码库寻找深化机会，以可视化 HTML 报告展示，然后针对你选中的候选项进行追问。
disable-model-invocation: true
---

# 改进代码库架构

揭示架构摩擦并提出**深化机会**——把浅 module 重构成深 module。目标是提升可测试性和 AI 可导航性。

此命令以项目领域模型为依据，并建立在共享设计词汇之上：

- 运行 `/codebase-design` 技能，获取架构词汇（**module**、**interface**、**depth**、**seam**、**adapter**、**leverage**、**locality**）及其原则（删除测试、“interface 就是测试表面”、“一个 adapter = 假设性 seam，两个 = 真实 seam”）。每项建议都必须准确使用这些词——不要漂移到“component”“service”“API”或“boundary”。
- `CONTEXT.md` 中的领域语言为优质 seam 命名；`docs/adr/` 中的 ADR 记录此命令不应重新争论的决策。

## 流程

### 1. 探索

先阅读项目领域术语表（`CONTEXT.md`），以及所触及区域的所有 ADR。

然后使用 Agent 工具和 `subagent_type=Explore` 遍历代码库。不要遵循僵硬启发式规则——自然探索，并记录遇到摩擦之处：

- 理解一个概念是否需要在许多小 module 之间来回跳转？
- 哪些 module 很**浅**——interface 几乎与 implementation 一样复杂？
- 是否有纯函数仅为可测试性而被提取，但真正 bug 隐藏在调用方式中（缺少 **locality**）？
- 哪些紧耦合 module 会跨 seam 泄漏？
- 哪些代码没有测试，或难以通过当前 interface 测试？

对任何疑似浅 module 应用**删除测试**：删除它会让复杂度集中，还是只会搬家？“会集中”就是你想要的信号。

### 2. 以 HTML 报告展示候选项

将自包含 HTML 文件写到操作系统临时目录，避免任何内容落入仓库。从 `$TMPDIR` 解析临时目录，失败则回退到 `/tmp`（Windows 上为 `%TEMP%`）；写入 `<tmpdir>/architecture-review-<timestamp>.html`，确保每次运行生成新文件。为用户打开它——Linux 使用 `xdg-open <path>`，macOS 使用 `open <path>`，Windows 使用 `start <path>`——并告诉用户绝对路径。

报告使用 CDN 版 **Tailwind** 进行布局和样式设计；当图、流程或时序能可靠表达结构时，使用 CDN 版 **Mermaid**。将 Mermaid 与手工 CSS/SVG 可视化结合：关系呈图形结构时（调用图、依赖、时序）使用 Mermaid；需要更具编辑感的表达（质量图、横截面、折叠动画）时使用手工 div/SVG。每个候选项都提供**之前/之后可视化**。要强调视觉表现。

为每个候选项渲染一张卡片，包含：

- **文件**——涉及哪些文件/module
- **问题**——当前架构为何造成摩擦
- **解决方案**——用通俗语言描述会发生什么变化
- **收益**——以 locality、leverage 和测试改进解释
- **之前 / 之后图**——并排、自定义绘制，展示浅化现状与深化结果
- **推荐强度**——`Strong`、`Worth exploring`、`Speculative` 之一，以 badge 展示

报告最后以**首要建议**一节收尾：最先处理哪个候选项，以及原因。

**领域部分使用 `CONTEXT.md` 的词汇，架构部分使用 `/codebase-design` 的词汇。** 如果 `CONTEXT.md` 定义了“Order”，就说“Order intake module”——不要说“FooBarHandler”，也不要说“Order service”。

**ADR 冲突**：如果候选项与现有 ADR 矛盾，只有当摩擦真实到值得重审 ADR 时才展示。务必在卡片中清晰标记（例如 warning callout：*“与 ADR-0007 矛盾——但值得重启讨论，因为……”*）。不要列出 ADR 所禁止的每种理论重构。

完整 HTML scaffold、图表模式和样式指南见 [HTML-REPORT.md](HTML-REPORT.md)。

此时不要提出 interface。文件写完后，询问用户：“你想探索其中哪一个？”

### 3. 追问循环

用户选择候选项后，运行 `/grilling` 技能，与用户一起遍历设计树——约束、依赖、深化后 module 的形态、seam 后包含什么、哪些测试能保留。

随着决策成形，立即执行副作用——运行 `/domain-modeling` 技能，在过程中保持领域模型最新：

- **用 `CONTEXT.md` 中没有的概念命名深化后的 module？** 将该术语加入 `CONTEXT.md`。如果文件不存在，延迟到此时再创建。
- **对话中澄清了模糊术语？** 当场更新 `CONTEXT.md`。
- **用户以承重理由拒绝候选项？** 提议建立 ADR：“要我把它记录成 ADR，让未来架构评审不再重复建议吗？”只有未来探索者确实需要该理由才能避免重复建议时才提议；短期理由（“现在不值得”）和不言自明的理由不要记录。
- **想探索深化后 module 的其他 interface？** 运行 `/codebase-design`，使用其 design-it-twice 并行 sub-agent 模式。
