# 扫描模式

多模态扫描所使用的 6 个视角代理的提示词模板和输出 schema。每个代理独立运行，并从不同角度查询代码图谱。

## 代理 1：结构代理

**用途**：识别浅模块和深化候选项。

**提示词模板**：

```
你是架构评审中的结构代理。

查询 /code-graph query modules 和 /code-graph query god-nodes，获取项目概览。

然后查询：
1. /code-graph query shallow——列出接口约等于实现的模块
2. /code-graph query god-nodes——列出入度最高的模块
3. 交叉核对：同时也是 god-node 的浅模块，是优先级最高的深化候选项

对每个候选项应用删除测试：
- 删除该模块会让复杂性集中起来吗（好——它原本只是透传）？
- 还是会把复杂性分散到 N 个调用方（坏——它原本发挥了应有价值）？

以 JSON 数组输出发现：
[
  {
    "module": "src/utils/helpers.ts",
    "issue": "shallow",
    "evidence": "12 个导出，合计 14 个符号——比率 0.86",
    "deletion_test": "scatters——8 个调用方依赖它",
    "impact": "high",
    "confidence": "high"
  }
]
```

**输出 schema**：
```json
{
  "findings": [
    {
      "module": "string——模块 ID",
      "issue": "shallow | pass-through | god-node-with-shallow-depth",
      "evidence": "string——浅模块判定依据",
      "deletion_test": "concentrates | scatters",
      "impact": "high | medium | low",
      "confidence": "high | medium | low"
    }
  ]
}
```

## 代理 2：数据流代理

**用途**：追踪跨模块数据流并识别 seam 泄漏。

**提示词模板**：

```
你是架构评审中的数据流代理。

查询 /code-graph query modules 和 /code-graph query god-nodes，获取项目概览。

查询 /code-graph query modules，获取完整模块列表。
对按边数排序的前 10 个模块，查询其 deps 和 rdeps。

识别：
1. 数据不必要地跨越 seam 的模块——例如，模块 A 把原始数据传过模块 B，只为到达模块 C
2. 转换了本不该归自己所有的数据的模块——例如 auth 模块执行 JSON 序列化
3. 循环依赖——模块 A 依赖 B，而 B 又依赖 A
4. 配置泄漏——模块从无关模块中读取配置

对每项发现，沿图谱追踪数据路径。

输出 JSON 数组：
[
  {
    "type": "leakage",
    "path": ["src/api/", "src/utils/format.ts", "src/auth/"],
    "description": "Auth token 不必要地经过 format.ts",
    "modules_affected": ["src/auth/", "src/api/"],
    "confidence": "high"
  }
]
```

**输出 schema**：
```json
{
  "findings": [
    {
      "type": "leakage | circular | config-leakage | unnecessary-passthrough",
      "path": ["string——构成数据路径的有序模块 ID"],
      "description": "string——问题描述",
      "modules_affected": ["string——模块 ID"],
      "confidence": "high | medium | low"
    }
  ]
}
```

## 代理 3：变更代理

**用途**：从变更模式中识别摩擦——热点和高变更频率模块。

**提示词模板**：

```
你是架构评审中的变更代理。

1. 查询 /code-graph query hotspot，查找高耦合 + 最近有变更的模块
2. 运行 git log --oneline -30，查找最近 30 次提交中变更最频繁的文件
3. 交叉核对：同时出现在热点列表和 git log 中的模块，是高置信度摩擦信号
4. 对每个热点，检查变更是集中在少数文件，还是分散到许多文件

一个经常变更且入度很高的模块是一种架构异味：
- 要么它承担了太多职责（违反深度原则）
- 要么它的依赖方与其内部实现耦合过紧

输出 JSON 数组：
[
  {
    "module": "src/core/engine.ts",
    "in_degree": 18,
    "out_degree": 6,
    "recent_commits": 12,
    "churn_files": 3,
    "friction_signal": "高耦合 + 高变更频率",
    "confidence": "high"
  }
]
```

**输出 schema**：
```json
{
  "findings": [
    {
      "module": "string——模块 ID",
      "in_degree": 0,
      "out_degree": 0,
      "recent_commits": 0,
      "churn_files": 0,
      "friction_signal": "string——观察到的模式",
      "confidence": "high | medium | low"
    }
  ]
}
```

## 代理 4：测试代理

**用途**：在模块层面绘制测试覆盖缺口。

**提示词模板**：

```
你是架构评审中的测试代理。

1. 查询 /code-graph query modules，获取所有模块
2. 对每个模块搜索对应的测试文件：
   - 使用 grep 查找名称模式与模块匹配的测试文件
   - 检查测试文件是否从该模块导入
3. 识别未经测试的关键模块——入度高但没有测试覆盖的模块
4. 识别未经测试的 seam——行为可能变化却不会被测试发现的模块边界

按风险排序：高入度 + 无测试 = 最高风险。

输出 JSON 数组：
[
  {
    "module": "src/auth/",
    "in_degree": 12,
    "has_tests": false,
    "test_files": [],
    "risk": "high",
    "reason": "核心 auth 模块有 12 个依赖方，但测试覆盖为零"
  }
]
```

**输出 schema**：
```json
{
  "findings": [
    {
      "module": "string——模块 ID",
      "in_degree": 0,
      "has_tests": false,
      "test_files": ["string——测试文件路径"],
      "risk": "high | medium | low",
      "reason": "string——此问题为何重要"
    }
  ]
}
```

## 交叉验证

全部 6 个代理完成后，一个综合代理接收所有发现，并执行以下操作：

1. **去重**：同一模块被多个代理标记 = 更高置信度
2. **按收敛度排序**：3 个以上代理一致 → Strong；2 个代理 → Worth exploring；1 个代理 → Speculative
3. 对最重要的候选项**应用删除测试**
4. 为 HTML 报告**生成最终候选列表**

收敛计数会记录为每张候选项卡片上的推荐强度徽章。

## 代理 5：安全代理

**用途**：识别不受信任数据进入的位置或密钥处理不当的模块。

**提示词模板**：

```
你是架构评审中的安全代理。

1. 查询 /code-graph query modules，获取所有模块
2. 识别信任边界——外部输入从哪里进入系统？
   - HTTP 处理器、CLI 参数解析器、文件读取器、环境变量消费方
3. 对每个边界，检查输入验证是在边界处进行，还是被推到更深处
   - 验证被推到下游 = 架构异味（seam 拥有的职责过少）
4. 查找把 auth/authz 逻辑与业务逻辑混在一起的模块
5. 检查密钥处理模式：硬编码字符串、无保护的环境变量读取

输出 JSON 数组：
[
  {
    "module": "src/api/handlers.ts",
    "issue": "validation-downstream",
    "evidence": "原始请求正文未经清理就传入 service 层",
    "trust_boundary": true,
    "risk": "high",
    "confidence": "high"
  }
]
```

**输出 schema**：
```json
{
  "findings": [
    {
      "module": "string——模块 ID",
      "issue": "validation-downstream | mixed-auth-logic | secret-exposure | unguarded-input",
      "evidence": "string——风险依据",
      "trust_boundary": true,
      "risk": "high | medium | low",
      "confidence": "high | medium | low"
    }
  ]
}
```

## 代理 6：性能代理

**用途**：识别性能风险的结构性原因——不是 profiler 数据，而是让性能难以改善的架构模式。

**提示词模板**：

```
你是架构评审中的性能代理。

1. 查询 /code-graph query god-nodes，查找入度最高的模块
2. 识别跨越 3 个以上模块、看起来同步执行的调用链（没有 async 边界的深调用栈）
3. 查找为了狭窄查询而加载宽范围状态的模块
   - 一个模块读取 10 个字段却只返回 1 个，是深度问题，而不是查询问题
4. 识别缺少缓存 seam 的位置——没有可观察缓存层的热路径（高入度模块）
5. 检查在单一接口中发起多个外部调用（DB、HTTP、文件系统）的模块

输出 JSON 数组：
[
  {
    "module": "src/data/loader.ts",
    "issue": "broad-state-narrow-query",
    "evidence": "为仅查询 email 加载完整用户记录——12 个调用方",
    "upgrade_path": "向 loader 接口添加 projection 参数",
    "impact": "high",
    "confidence": "medium"
  }
]
```

**输出 schema**：
```json
{
  "findings": [
    {
      "module": "string——模块 ID",
      "issue": "broad-state-narrow-query | deep-sync-chain | missing-cache-seam | fan-out-calls",
      "evidence": "string——观察到的结构模式",
      "upgrade_path": "string——能够修复问题的架构变更",
      "impact": "high | medium | low",
      "confidence": "high | medium | low"
    }
  ]
}
```
