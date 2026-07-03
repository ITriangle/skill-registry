# vendor/mattpocock/deprecated-qa

- Skill 名称：`qa`
- 当前状态：`analysis-only`
- 描述：Interactive QA session where user reports bugs or issues conversationally, and the agent files GitHub issues. Explores the codebase in the background for context and domain language. Use when user wants to report bugs, do QA, file issues conversationally, or mentions "QA session".

## 触发条件审查

- 审查描述是否足够聚焦，适合隐式调用。
- 确认显式触发词是否前置。

## 依赖与风险

- 脚本：未检测到
- 参考资料：未检测到
- 风险提及：文件系统

## 建议

- 建议状态：`candidate`
- 仅在检查许可证、脚本行为和触发范围重叠后再批准。
