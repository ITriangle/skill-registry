# vendor/itriangle/github-code-review

- Skill 名称：`github-code-review`
- 当前状态：`candidate`
- 描述：Perform a read-only, gated review of a GitHub pull request or local Git changes. Use for PR URLs or numbers, branches, commit ranges, staged or unstaged changes, pre-push reviews, and requests such as code review, review this PR, 审 PR, 代码审查, or 检查提交前改动. Do not use to implement fixes or publish a GitHub review.

## 触发条件审查

- 审查描述是否足够聚焦，适合隐式调用。
- 确认显式触发词是否前置。

## 依赖与风险

- 脚本：未检测到
- 参考资料：references/review-rubric.md
- 风险提及：网络, 文件系统, shell, 密钥

## 建议

- 建议状态：`candidate`
- 仅在检查许可证、脚本行为和触发范围重叠后再批准。
