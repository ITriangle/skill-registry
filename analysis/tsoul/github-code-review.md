# vendor/tsoul/github-code-review

- Skill 名称：`github-code-review`
- 当前状态：`candidate`
- 描述：对 GitHub 拉取请求或本地 Git 变更执行只读门禁式审查。适用于 PR URL 或编号、分支、提交区间、暂存或未暂存改动、推送前审查，以及 code review、review this PR、审 PR、代码审查、检查提交前改动等请求。不用于直接实现修复或向 GitHub 发布 review。

## 触发条件审查

- 审查描述是否足够聚焦，适合隐式调用。
- 确认显式触发词是否前置。

## 依赖与风险

- 脚本：未检测到
- 参考资料：references/review-rubric.md
- 风险提及：网络, 密钥

## 建议

- 建议状态：`candidate`
- 仅在检查许可证、脚本行为和触发范围重叠后再批准。
