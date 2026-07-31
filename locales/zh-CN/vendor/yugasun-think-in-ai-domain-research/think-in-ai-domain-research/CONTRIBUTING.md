# 为 think-in-ai-domain-research 贡献

感谢你有兴趣参与贡献！

## 快速开始

1. Fork 此仓库
2. 在本地克隆你的 fork
3. 安装 skill 以进行本地测试：

   ```
   npx skills add ./path/to/your/fork
   ```

   也可以将包含 `SKILL.md` 的目录以符号链接方式放入 `~/.claude/skills/`。

## 项目结构

```
think-in-ai-domain-research/
├── SKILL.md              # 核心 skill 定义
├── reference/            # 详细参考材料
│   ├── principles.md     # 操作原则和提示词模式
│   └── high-stakes.md    # 高风险领域规则
├── examples/             # 完整示例
│   ├── credit-rating.md
│   ├── product-workflow.md
│   ├── tech-ecosystem.md
│   └── sample-output.md
└── evals/
    └── evals.json        # 评估测试用例
```

## 如何贡献

### 报告问题

- 创建 issue，说明问题或建议
- 包含示例输入，以及预期行为与实际行为的差异
- 如果可以，请附上你使用的源材料

### 添加示例

1. 在 `examples/` 中创建新的 Markdown 文件
2. 遵循现有示例格式：输入 → 过程 → 输出重点
3. 适当时在 `SKILL.md` 中引用新文件
4. 在 `evals/evals.json` 中增加对应的评估用例

### 改进 Skill

1. 保持 `SKILL.md` 不超过 500 行
2. 将详细内容移入 `reference/` 文件
3. 描述使用第三人称，例如写“处理文档”，不要写“我处理文档”
4. 修改后使用全部三个示例场景测试

### 编写 Evals

Eval 对质量至关重要。`evals/evals.json` 中的每个评估应包含：

```json
{
  "id": 4,
  "prompt": "包含源材料的真实用户请求",
  "expected_output": "skill 应产出内容的说明",
  "files": []
}
```

最佳实践：

- 修改前先编写 Eval（评估驱动开发）
- 同时覆盖正常路径和边缘情况
- 至少包含一个高风险领域场景
- 使用全新的 Claude 实例测试，而不是创作此 skill 的实例

### 测试

1. 在本地安装 skill
2. 打开新的 Claude Code 会话
3. 运行每个 Eval 提示词并验证输出质量
4. 比较启用 skill 和未启用 skill 的基线

## 行为准则

保持尊重、建设性和包容。我们共同的目标是让领域研究更易获得。

## 许可证

参与贡献即表示你同意所提交的内容采用 MIT License。
