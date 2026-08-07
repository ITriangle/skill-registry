# vendor/mattpocock/engineering-code-review

- Skill 名称：`code-review`
- 当前状态：`candidate`
- 描述：Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/spec asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to "review since X".

## 触发条件审查

- 审查描述是否足够聚焦，适合隐式调用。
- 确认显式触发词是否前置。

## 依赖与风险

- 脚本：未检测到
- 参考资料：未检测到
- 风险提及：文件系统, shell

## 建议

- 建议状态：`candidate`
- 仅在检查许可证、脚本行为和触发范围重叠后再批准。
