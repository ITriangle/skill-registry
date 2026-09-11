# vendor/tsoul/word-stamp

- Skill 名称：`word-stamp`
- 当前状态：`candidate`
- 描述：把公章/合同专用章扫描件或照片做成 Word 可用的透明底 PNG 电子图章。用户说电子图章、电子印章、公章去底、印章透明、Word 盖章，或要把红章 JPG/PNG 插进 Word 时使用。不用于法定 CA 电子签章，也不处理蓝章/黑章。

## 触发条件审查

- 审查描述是否足够聚焦，适合隐式调用。
- 确认显式触发词是否前置。

## 依赖与风险

- 脚本：scripts/stamp_to_png.py
- 参考资料：未检测到
- 风险提及：shell

## 建议

- 建议状态：`candidate`
- 仅在检查许可证、脚本行为和触发范围重叠后再批准。
