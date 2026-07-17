# Issue tracker：GitHub

本仓库的 issue 和 PRD 存放在 GitHub issue 中。所有操作都使用 `gh` CLI。

## 约定

- **创建 issue**：`gh issue create --title "..." --body "..."`。多行正文使用 heredoc。
- **读取 issue**：`gh issue view <number> --comments`；使用 `jq` 过滤评论，并同时获取标签。
- **列出 issue**：`gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'`，并使用适当的 `--label` 和 `--state` 过滤器。
- **评论 issue**：`gh issue comment <number> --body "..."`
- **添加/删除标签**：`gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **关闭**：`gh issue close <number> --comment "..."`

根据 `git remote -v` 推断仓库——在 clone 内运行时，`gh` 会自动完成。

## 将 Pull request 作为分诊入口

**是否将 PR 作为请求入口：否。**（如果本仓库将外部 PR 视为功能请求，改为 `yes`；`/triage` 会读取此标志。）

设为 `yes` 时，PR 使用对应的 `gh pr` 命令，经历与 issue 相同的标签和状态：

- **读取 PR**：`gh pr view <number> --comments`，并使用 `gh pr diff <number>` 读取 diff。
- **列出需分诊的外部 PR**：`gh pr list --state open --json number,title,body,labels,author,authorAssociation,comments`，然后只保留 `authorAssociation` 为 `CONTRIBUTOR`、`FIRST_TIME_CONTRIBUTOR` 或 `NONE` 的项（排除 `OWNER`/`MEMBER`/`COLLABORATOR`）。
- **评论/添加标签/关闭**：`gh pr comment`、`gh pr edit --add-label`/`--remove-label`、`gh pr close`。

GitHub 的 issue 和 PR 共用同一编号空间，所以单独的 `#42` 可能属于任意一种——先用 `gh pr view 42` 解析，失败后回退到 `gh issue view 42`。

## 技能要求“发布到 issue tracker”时

创建 GitHub issue。

## 技能要求“获取相关工单”时

运行 `gh issue view <number> --comments`。
