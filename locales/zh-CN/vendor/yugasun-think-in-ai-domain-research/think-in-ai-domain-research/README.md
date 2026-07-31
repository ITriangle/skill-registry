# Think in AI Domain Research

[![许可证：MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-open_standard-green.svg)](https://agentskills.io)

[中文文档](README_zh.md)

> 将原始材料转化为结构化领域知识。AI 完成第一轮严肃调研，让你能与专家进行更高质量的对话。

## 适用场景

需要完成以下工作时使用此 skill：

- **学习新领域**——业务、行业、监管、方法论或技术生态
- **理解文档**——报告、规格、政策、代码、工单或会议纪要
- **准备专家沟通**——与产品经理、分析师、利益相关方或客户对话
- **把理解转化为工作**——需求、测试、Eval、Benchmark 或实施计划

**不适用于：** 简单事实查询、没有源材料的头脑风暴或纯创意写作。

## 安装

**自然语言方式**（在 Claude Code、Cursor、Codex 等环境中）：

```
从 https://github.com/yugasun/think-in-ai-domain-research 安装 think-in-ai-domain-research skill
```

**CLI：**

```bash
npx skills add yugasun/think-in-ai-domain-research
```

**手动安装：**

```bash
# 克隆到 skill 目录
git clone https://github.com/yugasun/think-in-ai-domain-research ~/.claude/skills/think-in-ai-domain-research
```

## 功能

- 🔍 **建立领域模型**——概念地图、核心对象、流程链、决策边界
- 📊 **多来源对齐**——比较材料，而不是分别摘要
- 🎯 **事实/推断分离**——将每项结论标为事实、规则、推断或边界
- ❓ **专家校准问题**——为领域专家生成范围窄、与证据相关的具体问题
- 🔧 **工作产物转化**——把洞察映射成需求、测试、Eval 和 Benchmark
- ⚠️ **高风险防护规则**——为法律、医疗、金融和合规领域提供额外严谨性

## 使用示例

```text
我拿到一份评级方法论和三份评级报告，请帮我建立业务认知。
```

```text
这里有一份 PRD、客服工单和会议纪要。请帮我理解这个领域并转成测试用例。
```

```text
我要学习一个新的技术生态，手里有官方文档和示例代码。请帮我快速入门。
```

## 工作原理

此 skill 遵循 7 步流程：

| 步骤 | 动作 | 输出 |
|------|------|------|
| 1. 盘点 | 整理所有源材料 | 来源表 |
| 2. 目标 | 定义研究目的和下游产物 | 研究目标陈述 |
| 3. 规则 | 编译方法论、政策或规格 | 规则模型 |
| 4. 对齐 | 将案例与已编译规则比较 | 证据 → 判断链 |
| 5. 领域模型 | 建立概念地图、对象、流程和边界 | 领域模型 |
| 6. 专家问题 | 生成具体校准问题 | 问题清单 |
| 7. 产物 | 把洞察映射到需求、测试和 Eval | 工作产物映射 |

## 默认输出：领域入门包

除非要求其他格式，否则此 skill 会生成包含 13 节的入门包：

1. 研究目标
2. 材料清单
3. 概念地图
4. 核心对象
5. 规则/方法论
6. 案例对齐
7. 判断链/工作流
8. 关键指标与术语
9. 风险信号与失败模式
10. 证据支持什么
11. 证据不支持什么
12. 专家校准问题
13. 可转化的工作产物

## 项目结构

```
think-in-ai-domain-research/
├── SKILL.md              # 核心 skill 定义
├── reference/
│   ├── principles.md     # 操作原则与提示词模式
│   └── high-stakes.md    # 高风险领域规则
├── examples/
│   ├── credit-rating.md  # 信用评级案例
│   ├── product-workflow.md # 产品工作流案例
│   ├── tech-ecosystem.md # 技术生态案例
│   └── sample-output.md  # 完整输出示例
└── evals/
    └── evals.json        # 评估测试用例
```

## 参与贡献

如何报告问题、添加示例和编写评估，见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE) © [yugasun](https://github.com/yugasun)
