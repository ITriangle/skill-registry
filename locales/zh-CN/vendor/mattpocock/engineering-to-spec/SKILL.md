---
name: to-spec
description: 将当前对话转为 spec 并发布到项目 issue tracker——不采访，只综合已讨论内容。
disable-model-invocation: true
---

本 skill 用当前对话上下文与代码库理解产出 spec。**不要**采访用户——只综合已知。

issue tracker 与 triage label 词汇应已提供——否则运行 `/setup-matt-pocock-skills`。

## 流程

1. 若尚未探索，探索 repo 理解代码库当前状态。spec 全程用项目领域 glossary 词汇，尊重触及区域 ADR。

2. 勾勒将在哪些 seam 测试该功能。优先现有 seam 于新 seam。尽可能用最高 seam。若需新 seam，在能到的最高点提议。代码库中 seam 越少越好——理想是一个。

与用户确认这些 seam 符合预期。

3. 用下方模板写 spec，然后发布到项目 issue tracker。应用 `ready-for-agent` triage label——无需额外 triage。

<spec-template>

## Problem Statement

用户面临的问题，从用户视角。

## Solution

问题的解决方案，从用户视角。

## User Stories

很长的编号用户故事列表。每条格式：

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story-example>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story-example>

列表应极 extensive，覆盖功能各方面。

## Implementation Decisions

已做实现决定列表。可包括：

- 将建/改的 module
- 将改的 interface
- 开发者的技术澄清
- 架构决定
- Schema 变更
- API 契约
- 具体交互

不要包含具体文件路径或代码片段。它们可能很快过时。

例外：若原型产出比 prose 更精确编码决定的片段（状态机、reducer、schema、type shape），在相关决定内 inline，并简短注明来自原型。trim 到决定丰富部分——不是可运行 demo，只是重要 bits。

## Testing Decisions

已做测试决定列表。包括：

- 好测试的描述（只测外部行为，非实现细节）
- 将测哪些 module
- 测试 prior art（代码库中类似测试）

## Out of Scope

本 spec 范围外事项描述。

## Further Notes

关于功能的进一步备注。

</spec-template>
