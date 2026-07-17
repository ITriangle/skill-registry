# 分诊标签

bundle 技能使用的规范分诊角色。将其映射到 tracker 的标签字符串。

| 规范角色 | 本 tracker 中的标签 | 含义 |
| --- | --- | --- |
| `needs-triage` | `needs-triage` | 需要维护者评估 |
| `needs-info` | `needs-info` | 等待报告者提供信息 |
| `ready-for-agent` | `ready-for-agent` | 可交给 AFK 代理 |
| `ready-for-human` | `ready-for-human` | 需要人工实现 |
| `wontfix` | `wontfix` | 不会处理 |

当技能说“应用 ready-for-agent 标签”时，使用此表中的 tracker 字符串。
