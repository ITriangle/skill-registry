---
name: claude-handoff
description: 将当前对话交给一个立即接手工作的全新后台 agent。
argument-hint: "下一次会话将用于什么？"
disable-model-invocation: true
---

编写当前对话的交接摘要，让新的 agent 能继续工作。不要保存摘要，而是以摘要作为 prompt 启动后台 agent：`claude --bg --name "<描述性名称>" "<交接摘要>"`。它会在当前工作目录启动并立即返回；用户通过 `claude agents` 管理它。

始终通过 `-n`/`--name` 传入描述性名称（例如 `--name "Fix login bug"`）——该名称会成为任务列表、会话选择器和终端标题中显示的名称。

在摘要中加入“建议使用的技能”一节，推荐该 agent 应调用的技能。

不要重复其他工件（PRD、计划、ADR、issue、commit、diff）中已经记录的内容。改为通过路径或 URL 引用它们。

隐去任何敏感信息，例如 API key、密码或个人身份信息——该摘要会成为 agent 的 prompt。

如果用户传入了参数，将其视为下一次会话关注内容的说明，并据此调整摘要。
