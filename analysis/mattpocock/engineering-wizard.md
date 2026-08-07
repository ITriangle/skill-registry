# vendor/mattpocock/engineering-wizard

- Skill 名称：`wizard`
- 当前状态：`candidate`
- 描述：Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover. Don't invoke this for steps the agent can perform itself.

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
