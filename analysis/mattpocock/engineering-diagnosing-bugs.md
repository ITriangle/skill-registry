# vendor/mattpocock/engineering-diagnosing-bugs

- Skill 名称：`diagnosing-bugs`
- 当前状态：`candidate`
- 描述：Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow.

## 触发条件审查

- 审查描述是否足够聚焦，适合隐式调用。
- 确认显式触发词是否前置。

## 依赖与风险

- 脚本：scripts/hitl-loop.template.sh
- 参考资料：未检测到
- 风险提及：网络, 文件系统, shell, 密钥

## 建议

- 建议状态：`candidate`
- 仅在检查许可证、脚本行为和触发范围重叠后再批准。
