# Think in AI Domain Research

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-open_standard-green.svg)](https://agentskills.io)

[English](README.md)

> 将原始材料转化为结构化领域知识。AI 完成第一轮严肃调研，让你和专家的对话更有质量。

## 适用场景

- **学习新领域** — 业务、行业、监管、方法论或技术生态
- **理解文档** — 报告、规范、政策、代码、工单或会议纪要
- **准备专家对话** — 与产品经理、分析师、利益相关者或客户沟通
- **将认知转化为工作产出** — 需求、测试、评估、基准或实施方案

**不适用于：** 简单事实查询、无材料的头脑风暴、纯创意写作。

## 安装方式

**自然语言**（在 Claude Code、Cursor、Codex 等中）：

```
安装 think-in-ai-domain-research skill，来源 https://github.com/yugasun/think-in-ai-domain-research
```

**命令行：**

```bash
npx skills add yugasun/think-in-ai-domain-research
```

**手动安装：**

```bash
git clone https://github.com/yugasun/think-in-ai-domain-research ~/.claude/skills/think-in-ai-domain-research
```

## 核心特性

- 🔍 **领域模型构建** — 概念地图、核心对象、流程链、决策边界
- 📊 **多源对齐** — 比较材料而非逐个摘要
- 🎯 **事实/推断分离** — 每条结论标注：事实、规则、推断或边界
- ❓ **专家校准问题** — 针对证据的精准问题，用于和领域专家确认
- 🔧 **工作产物转化** — 将洞察映射为需求、测试、评估和基准
- ⚠️ **高风险领域守则** — 法律、医疗、金融、合规领域的额外严谨性

## 使用示例

```text
我拿到一份评级方法论和三份评级报告，请帮我建立业务认知。
```

```text
这里有一个新产品的 PRD、几条客服工单和一份会议纪要。我不清楚业务流程，帮我先研究这个领域，再转成研发验收标准。
```

```text
我要学习一个新的技术生态，手里有官方文档和示例代码。请帮我快速入门。
```

## 工作流程

技能遵循 7 步工作流程：

| 步骤 | 动作 | 输出 |
|------|------|------|
| 1. 盘点 | 清点所有源材料 | 材料清单表 |
| 2. 目标 | 定义研究目的和下游产物 | 研究目标声明 |
| 3. 规则 | 编译方法论、政策或规范 | 规则模型 |
| 4. 对齐 | 将案例与编译的规则比较 | 证据→判断链 |
| 5. 领域模型 | 构建概念图、对象、流程、边界 | 领域模型 |
| 6. 专家问题 | 生成精准的校准问题 | 问题清单 |
| 7. 工作产物 | 将洞察映射为需求、测试、评估 | 产物映射 |

## 默认输出：领域入门包

除非你指定其他格式，技能会生成 13 节的入门包：

1. 研究目标
2. 材料清单
3. 概念地图
4. 核心对象
5. 规则/方法论
6. 案例对齐
7. 判断链/工作流
8. 关键指标与术语
9. 风险信号与失败模式
10. 证据能支持的结论
11. 证据不能支持的结论
12. 专家校准问题
13. 可转化的工作产物

## 项目结构

```
think-in-ai-domain-research/
├── SKILL.md              # 核心技能定义
├── reference/
│   ├── principles.md     # 操作原则与 prompt 模式
│   └── high-stakes.md    # 高风险领域守则
├── examples/
│   ├── credit-rating.md  # 信用评级案例
│   ├── product-workflow.md # 产品工作流案例
│   ├── tech-ecosystem.md # 技术生态案例
│   └── sample-output.md  # 完整输出示例
└── evals/
    └── evals.json        # 评估测试用例
```

## 贡献指南

参见 [CONTRIBUTING.md](CONTRIBUTING.md) 了解报告问题、添加示例和编写评估的指南。

## 许可证

[MIT](LICENSE) © [yugasun](https://github.com/yugasun)
