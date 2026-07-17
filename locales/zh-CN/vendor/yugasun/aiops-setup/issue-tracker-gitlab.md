# Issue tracker：GitLab

本仓库的 issue 和 PRD 存放在 GitLab issue 中。所有操作都使用 [`glab`](https://gitlab.com/gitlab-org/cli) CLI。

## 约定

- **创建 issue**：`glab issue create --title "..." --description "..."`。多行描述使用 heredoc。传入 `--description -` 可打开编辑器。
- **读取 issue**：`glab issue view <number> --comments`。机器可读输出使用 `-F json`。
- **列出 issue**：`glab issue list -F json`，并使用适当的 `--label` 过滤器。
- **评论 issue**：`glab issue note <number> --message "..."`。GitLab 将评论称为 “note”。
- **添加/删除标签**：`glab issue update <number> --label "..."` / `--unlabel "..."`。多个标签可以逗号分隔，或重复使用该标志。
- **关闭**：`glab issue close <number>`。`glab issue close` 不接受关闭评论，因此先使用 `glab issue note <number> --message "..."` 发布说明，再关闭。
- **Merge request**：GitLab 将 PR 称为 “merge request”。使用 `glab mr create`、`glab mr view`、`glab mr note` 等——形状与 `gh pr ...` 相同，只是将 `pr` 换为 `mr`，将 `comment`/`--body` 换为 `note`/`--message`。

根据 `git remote -v` 推断仓库——在 clone 内运行时，`glab` 会自动完成。

## 将 Merge request 作为分诊入口

**是否将 MR 作为请求入口：否。**（如果本仓库将外部 merge request 视为功能请求，改为 `yes`；`/triage` 会读取此标志。）

设为 `yes` 时，MR 使用对应的 `glab mr` 命令，经历与 issue 相同的标签和状态：

- **读取 MR**：`glab mr view <number> --comments`，并使用 `glab mr diff <number>` 读取 diff。
- **列出需分诊的外部 MR**：`glab mr list -F json`，然后只保留作者不是项目成员/所有者的 MR（贡献者的 MR，而非维护者进行中的工作）。
- **评论/添加标签/关闭**：`glab mr note`、`glab mr update --label`/`--unlabel`、`glab mr close`。

与 GitHub 不同，GitLab 分别为 issue 和 MR 编号，因此一旦知道维护者指的是哪个入口，`#42` 就没有歧义。

## 技能要求“发布到 issue tracker”时

创建 GitLab issue。

## 技能要求“获取相关工单”时

运行 `glab issue view <number> --comments`。
