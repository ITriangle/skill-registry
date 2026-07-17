# aiops.yaml——项目配置（可选）

放在**仓库根目录**。conductor **引导**和显式 `/aiops-setup` 都会读取。

## 规则

| `docs/agents/` | `aiops.yaml` | 引导行为 |
| --- | --- | --- |
| 缺失 | 不存在 | **静默默认**——本地 Markdown issue + 一一对应的分诊标签；不询问 tracker |
| 缺失 | 存在 | 应用 yaml 中的 `issue_tracker`（仅当 yaml 指定时使用 GitHub/GitLab） |
| 存在 | 任意 | 跳过引导；要更改 tracker，编辑 `docs/agents/*.md` |

## Schema（版本 1）

```yaml
version: 1

issue_tracker:
  kind: local          # local | github | gitlab——文件不存在时默认 local
  prs_as_triage: false # 仅 github | gitlab——是否将外部 PR 作为分诊入口

# 可选——省略时，默认与规范角色名一一对应
triage_labels:
  needs-triage: needs-triage
  needs-info: needs-info
  ready-for-agent: ready-for-agent
  ready-for-human: ready-for-human
  wontfix: wontfix

# 可选——省略时默认 single
domain:
  layout: single       # single → CONTEXT.md + docs/adr/ | multi → CONTEXT-MAP.md
```

## 写入内容

引导始终根据 `skills/aiops-setup/` 中的模板创建 `docs/agents/issue-tracker.md`、`triage-labels.md`、`domain.md`：

| `issue_tracker.kind` | 初始模板 |
| --- | --- |
| `local` | `issue-tracker-local.md` |
| `github` | `issue-tracker-github.md` |
| `gitlab` | `issue-tracker-gitlab.md` |

yaml 中的 `prs_as_triage` 为 `true` 时，在 `issue-tracker.md` 正文中作相同设置。

## 示例——GitHub 团队仓库

```yaml
version: 1
issue_tracker:
  kind: github
  prs_as_triage: false
```

## 示例——保持默认值（无需文件）

没有 `aiops.yaml` → 使用 `.scratch/<feature>/` 下的本地 Markdown——零配置。
