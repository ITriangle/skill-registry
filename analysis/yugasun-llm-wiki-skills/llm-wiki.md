# vendor/yugasun-llm-wiki-skills/llm-wiki

- Skill 名称：`llm-wiki`
- 当前状态：`candidate`
- 描述：构建并维护由 LLM 维护的个人知识库。触发：摄取来源进 wiki、查询 wiki 知识、lint 质量、'加入 wiki'、'关于 X 我知道什么'，或提到 LLM wiki / Karpathy wiki。

## 触发条件审查

- 审查描述是否足够聚焦，适合隐式调用。
- 确认显式触发词是否前置。

## 依赖与风险

- 脚本：scripts/init-wiki.sh, scripts/lint-wiki.sh, scripts/new-raw.sh, scripts/rehash-raw.sh
- 参考资料：references/archive-template.md, references/article-template.md, references/comparison-template.md, references/concept-template.md, references/entity-template.md, references/index-template.md, references/log-template.md, references/ops-loop.md, references/query-archive-template.md, references/raw-template.md, references/source-adapters.md, references/synthesis-template.md
- 风险提及：网络, shell

## 建议

- 建议状态：`candidate`
- 仅在检查许可证、脚本行为和触发范围重叠后再批准。
