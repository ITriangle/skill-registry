---
name: claude-handoff
description: 将当前对话 hand off 给新的后台 agent，立即接续工作。
argument-hint: "下一会话将用于什么？"
disable-model-invocation: true
---

写当前对话的 handoff 摘要，使新 agent 能继续工作。不要保存它，而是用摘要作为 prompt 启动后台 agent：`claude --bg --name "<描述性名称>" "<handoff 摘要>"`。它在当前 working directory 启动并立即返回；用户用 `claude agents` 管理。

始终传 `-n`/`--name` 及描述性名称（如 `--name "Fix login bug"`）——它设置 job 列表、会话选择器和终端标题中的显示名。

摘要中包含「建议技能」部分，建议 agent 应调用的 skill。

不要重复其他 artifact 已捕获的内容（spec、plan、ADR、issue、commit、diff）。用路径或 URL 引用它们。

脱敏任何敏感信息，如 API key、密码或个人身份信息——摘要会成为 agent 的 prompt。

若用户传了参数，将其视为下一会话焦点的描述，并相应定制摘要。
