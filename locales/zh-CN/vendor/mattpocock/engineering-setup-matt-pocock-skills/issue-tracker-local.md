# Issue tracker：本地 Markdown

当前仓库的 issue 和 PRD 以 Markdown 文件形式保存在 `.scratch/` 中。

## 约定

- 每个功能使用一个目录：`.scratch/<feature-slug>/`
- PRD 位于 `.scratch/<feature-slug>/PRD.md`
- 实现 issue 位于 `.scratch/<feature-slug>/issues/<NN>-<slug>.md`，从 `01` 开始编号
- 分诊状态记录在每个 issue 文件顶部附近的 `Status:` 行中（角色字符串参见 `triage-labels.md`）
- 评论和对话历史追加到文件底部的 `## Comments` 标题下

## 当技能要求“发布到 issue tracker”时

在 `.scratch/<feature-slug>/` 下创建新文件（必要时创建目录）。

## 当技能要求“获取相关 ticket”时

读取引用路径中的文件。用户通常会直接给出路径或 issue 编号。

## 寻路操作

由 `/wayfinder` 使用。**地图**是一个文件，每个 **child** ticket 对应一个文件。

- **地图**：`.scratch/<effort>/map.md`——包含 Notes / Decisions-so-far / Fog 正文。
- **子 ticket**：`.scratch/<effort>/issues/NN-<slug>.md`，从 `01` 开始编号，正文中写问题。`Type:` 行记录 ticket 类型（`research`/`prototype`/`grilling`/`task`）；`Status:` 行记录 `claimed`/`resolved`。
- **阻塞关系**：顶部附近的 `Blocked by: NN, NN` 行。列出的每个文件都标为 `resolved` 后，ticket 才解除阻塞。
- **前沿**：扫描 `.scratch/<effort>/issues/`，查找开放、未阻塞且无人领取的文件；编号最小者优先。
- **领取**：在开始任何工作前，将 `Status` 设为 `claimed` 并保存。
- **解决**：在 `## Answer` 标题下追加答案，把 `Status` 设为 `resolved`，再把上下文指针（摘要 + 链接）追加到 `map.md` 的 Decisions-so-far 中。
