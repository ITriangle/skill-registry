---
name: claude-handoff
description: 当当前对话需要交给新的后台 agent 立即接手并继续工作时使用。 当只是要总结、归档、发给人类阅读，或不需要启动另一个 agent 时不要用。
---

# 中文导读

- 使用场景：当当前对话需要交给新的后台 agent 立即接手并继续工作时使用。
- 不适用：当只是要总结、归档、发给人类阅读，或不需要启动另一个 agent 时不要用。

# 上游说明原文

Write a handoff summary of the current conversation so a fresh agent can continue the work. Instead of saving it, launch a background agent seeded with the summary as its prompt: `claude --bg --name "<descriptive name>" "<handoff summary>"`. It starts in the current working directory and returns immediately; the user manages it with `claude agents`.

Always pass `-n`/`--name` with a descriptive name (e.g. `--name "Fix login bug"`) — it sets the display name shown in the job list, session picker, and terminal title.

Include a "suggested skills" section in the summary, which suggests skills that the agent should invoke.

Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information — the summary becomes the agent's prompt.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the summary accordingly.
