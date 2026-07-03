# vendor/mattpocock/in-progress-wizard

- Skill 名称：`wizard`
- 当前状态：`analysis-only`
- 描述：Generate an interactive bash wizard that walks a human through a manual procedure — third-party setup, a one-off migration, an A→B state transition — opening URLs, capturing values, confirming each step, and writing .env files and GitHub Actions secrets.

## 触发条件审查

- 审查描述是否足够聚焦，适合隐式调用。
- 确认显式触发词是否前置。

## 依赖与风险

- 脚本：未检测到
- 参考资料：未检测到
- 风险提及：网络, 文件系统, shell, 密钥

## 建议

- 建议状态：`candidate`
- 仅在检查许可证、脚本行为和触发范围重叠后再批准。
