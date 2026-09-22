# vendor/yugasun-skills/nice-lark-doc

- Skill 名称：`nice-lark-doc`
- 当前状态：`candidate`
- 描述：美化飞书文档排版，通过 6 种风格配方（Recipe）智能匹配，生成结构清晰、视觉专业的飞书文档。 支持画板（SVG/Mermaid）、表格、Callout、Grid 等富视觉元素。 Use when：创建新飞书文档并希望排版美观、美化/优化现有文档视觉和结构、 将素材整理为专业文档、为技术方案/产品文档/会议纪要生成配套画板。 触发词：美化飞书文档、nice doc、漂亮文档、飞书排版、写一份好看的文档、 文档排版、lark doc 美化、文档视觉优化、专业文档、文档设计。

## 触发条件审查

- 审查描述是否足够聚焦，适合隐式调用。
- 确认显式触发词是否前置。

## 依赖与风险

- 脚本：scripts/check-deps.sh, scripts/setup.sh
- 参考资料：references/blocks-mapping.md, references/color-palette.md, references/delivery-templates.md, references/flowchart-theme.md, references/quality-checklist.md, references/recipe-index.json, references/recipes/action-oriented.md, references/recipes/data-dense.md, references/recipes/editorial-clean.md, references/recipes/presentation.md, references/recipes/product-visual.md, references/recipes/tech-structured.md, references/reference-gallery.md, references/setup-guide.md, references/whiteboard-bridge.md, references/whiteboard-examples/01-flowchart-rail-release.jpg, references/whiteboard-examples/01-flowchart-rail-release.svg, references/whiteboard-examples/02-cloud-topology.jpg, references/whiteboard-examples/02-cloud-topology.svg, references/whiteboard-examples/03-tech-layers.jpg, references/whiteboard-examples/03-tech-layers.svg, references/whiteboard-examples/04-algorithm-deep.jpg, references/whiteboard-examples/04-algorithm-deep.svg
- 风险提及：网络, shell

## 建议

- 建议状态：`candidate`
- 仅在检查许可证、脚本行为和触发范围重叠后再批准。

## 本次注册审查

- 来源：`https://github.com/yugasun/skills.git`，提交 `425964919f88b7bae0aec6a40c7a6b4a2c645c3b`，MIT 许可证随技能保留。现有 `yugasun` 指向独立的 `yugasun/aiops`，故使用独立来源 `yugasun-skills`。
- 无同名已注册变体，默认使用此来源。与 `feishu-doc-writing` 有场景重叠：前者按六种配方选择视觉风格，后者使用克制的固定规格风格；保留两者，需要六种配方或用户点名时选择 `nice-lark-doc`。
- `SKILL.md` 显式使用 `lark-doc`；其引用的设置指南和脚本列出 `lark-shared`、`lark-doc`、`lark-whiteboard`、`lark-drive`。四项均记录在组依赖中，并已存在于本机全局技能目录，由外部工具维护，不重复导入。
- 已检查两个 shell 脚本：设置脚本可安装 npm CLI 和上游飞书技能，并检查认证；本次仅注册技能，不运行安装及授权流程。
- 上游所有 Markdown 文档已有中文正文，中文镜像保留完整原文，许可证、代码、脚本不翻译。
- 保持 `candidate` 状态，通过 `--allow-candidate` 全局同步；未将候选状态自动提升为 approved。
