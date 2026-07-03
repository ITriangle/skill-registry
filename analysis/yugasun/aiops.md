# vendor/yugasun/aiops

- Skill 名称：`aiops`
- 当前状态：`candidate`
- 描述：Flow Conductor for the aiops bundle. One entry — infers task type, shows plain-language steps, tracks journey in flow.state.yaml, dispatches skill + agent per phase.

## 触发条件审查

- 审查描述是否足够聚焦，适合隐式调用。
- 确认显式触发词是否前置。

## 依赖与风险

- 脚本：scripts/code_graph_query.py, scripts/flow_cli.py, scripts/gates.py, scripts/journey_state.py, scripts/phases.py, scripts/task_dag.py, scripts/test_code_graph.py, scripts/test_router.py
- 参考资料：未检测到
- 风险提及：shell

## 建议

- 建议状态：`candidate`
- 仅在检查许可证、脚本行为和触发范围重叠后再批准。
