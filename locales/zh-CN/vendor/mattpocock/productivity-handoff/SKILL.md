---
name: handoff
description: 将当前对话压缩成交接文档，供另一个 agent 接手。
argument-hint: "下一次会话将用于什么？"
disable-model-invocation: true
---

编写一份总结当前对话的交接文档，让新的 agent 能继续工作。将它保存到用户操作系统的临时目录，而不是当前工作区。

在文档中加入“建议使用的技能”一节，推荐该 agent 应调用的技能。

不要重复其他工件（spec、计划、ADR、issue、commit、diff）中已经记录的内容。改为通过路径或 URL 引用它们。

隐去任何敏感信息，例如 API key、密码或个人身份信息。

如果用户传入了参数，将其视为下一次会话关注内容的说明，并据此调整文档。
