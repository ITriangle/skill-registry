# Contributing to think-in-ai-domain-research

Thank you for your interest in contributing! / 感谢你的关注和贡献！

## Getting Started / 快速开始

1. Fork this repository
2. Clone your fork locally
3. Install the skill for local testing:
   ```
   npx skills add ./path/to/your/fork
   ```
   Or symlink the `SKILL.md` directory into your `~/.claude/skills/` folder.

## Project Structure / 项目结构

```
think-in-ai-domain-research/
├── SKILL.md              # Core skill definition
├── reference/            # Detailed reference materials
│   ├── principles.md     # Operating principles and prompt patterns
│   └── high-stakes.md    # High-stakes domain guardrails
├── examples/             # Worked examples
│   ├── credit-rating.md
│   ├── product-workflow.md
│   ├── tech-ecosystem.md
│   └── sample-output.md
└── evals/
    └── evals.json        # Evaluation test cases
```

## How to Contribute / 如何贡献

### Reporting Issues / 报告问题

- Open an issue describing the problem or suggestion
- Include example inputs and the expected vs actual behavior
- If possible, include the source materials you used

### Adding Examples / 添加示例

1. Create a new markdown file in `examples/`
2. Follow the existing example format: Input → Process → Output Focus
3. Reference the new file in `SKILL.md` if appropriate
4. Add a corresponding eval case in `evals/evals.json`

### Improving the Skill / 改进 Skill

1. Keep `SKILL.md` under 500 lines
2. Move detailed content to `reference/` files
3. Use third person in descriptions ("Processes documents", not "I process documents")
4. Test with all three example scenarios after changes

### Writing Evals / 编写评估

Evals are critical for quality. Each eval in `evals/evals.json` should have:

```json
{
  "id": 4,
  "prompt": "A realistic user request with source materials",
  "expected_output": "Description of what the skill should produce",
  "files": []
}
```

Best practices:
- Write evals BEFORE making changes (evaluation-driven development)
- Cover both happy path and edge cases
- Include at least one high-stakes domain scenario
- Test with a fresh Claude instance (not the one you authored with)

### Testing / 测试

1. Install the skill locally
2. Open a new Claude Code session
3. Run each eval prompt and verify the output quality
4. Compare with-skill vs. without-skill baselines

## Code of Conduct / 行为准则

Be respectful, constructive, and inclusive. We're all here to make domain research more accessible.

## License / 许可证

By contributing, you agree that your contributions will be licensed under the MIT License.
