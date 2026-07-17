---
name: triage
description: 让 issue 和外部 PR 依次经过分诊角色——分类、验证、必要时深入追问，并编写代理可直接执行的简报。
disable-model-invocation: true
---

# 分诊

用于 issue（以及在 `docs/agents/issue-tracker.md` 中配置过的外部 PR）的状态机。每条跟踪器评论都以以下内容开头：

> *此内容由 AI 在分诊过程中生成。*

如果缺少分诊标签映射，运行 `/aiops-setup`。

## 角色

**类别：** `bug` | `enhancement`

**状态：** `needs-triage` | `needs-info` | `ready-for-agent` | `ready-for-human` | `wontfix`

每个项目一个类别加一个状态。实际标签字符串可能不同——使用 `docs/agents/triage-labels.md`。

简报格式：[AGENT-BRIEF.md](AGENT-BRIEF.md)。拒绝项知识库：[OUT-OF-SCOPE.md](OUT-OF-SCOPE.md)。

## 调用方式

自然语言：“哪些内容需要关注”“分诊 #42”“把 #42 移到 ready-for-agent”。

## 展示待关注内容

按以下分组展示（组内最旧的在前）：无标签、`needs-triage`、有报告者新活动的 `needs-info`。当 PR 在处理范围内时，用 `[PR]` 和 `[issue]` 标明类型。

## 分诊一个项目

1. **收集**——正文、评论、标签、diff（PR）。检查 `.out-of-scope/` 中此前的拒绝记录；搜索代码库，确认是否已有实现。
2. **建议**类别和状态；等待维护者确认。
3. **验证**——在深入追问前复现 bug 或验证 PR 的主张。
4. **必要时深入追问**——使用 `/grilling` + `/domain-modeling`，就地更新 CONTEXT/ADR。
5. **应用结果：**
   - `ready-for-agent` / `ready-for-human`——发布简报
   - `needs-info`——发布分诊备注（已确定事实 + 给报告者的问题）
   - `wontfix`——已经实现（指向代码）| 被拒绝的 bug（关闭）| 被拒绝的增强项（写入 `.out-of-scope/` 后关闭）

## 快速覆盖

“把 #N 移到 ready-for-agent”——确认后直接应用；除非缺少简报，否则跳过 grilling。
