# vendor/mattpocock/misc-git-guardrails-claude-code

- Skill 名称：`git-guardrails-claude-code`
- 当前状态：`candidate`
- 描述：Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code.

## 触发条件审查

- 审查描述是否足够聚焦，适合隐式调用。
- 确认显式触发词是否前置。

## 依赖与风险

- 脚本：scripts/block-dangerous-git.sh
- 参考资料：未检测到
- 风险提及：文件系统, shell

## 建议

- 建议状态：`candidate`
- 仅在检查许可证、脚本行为和触发范围重叠后再批准。
