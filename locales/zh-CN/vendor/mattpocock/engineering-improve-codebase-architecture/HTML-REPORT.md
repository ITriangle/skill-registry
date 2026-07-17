# HTML 报告格式

架构评审以单个自包含 HTML 文件呈现，存放在操作系统临时目录中。Tailwind 和 Mermaid 都从 CDN 加载。Mermaid 能可靠处理图形结构的图表；手工构建的 div 和内联 SVG 则适合更具编辑感的视觉表达（质量图、横截面）。两者混合使用——不要所有内容都依赖 Mermaid，否则会显得千篇一律。

## Scaffold

```html
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <title>架构评审 — {{repo name}}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="module">
      import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
      mermaid.initialize({ startOnLoad: true, theme: "neutral", securityLevel: "loose" });
    </script>
    <style>
      /* 对 Tailwind 难以整洁覆盖的部分添加少量自定义样式：
         seam 虚线、手绘感箭头等。 */
      .seam { stroke-dasharray: 4 4; }
      .leak { stroke: #dc2626; }
      .deep { background: linear-gradient(135deg, #0f172a, #1e293b); }
    </style>
  </head>
  <body class="bg-stone-50 text-slate-900 font-sans">
    <main class="max-w-5xl mx-auto px-6 py-12 space-y-12">
      <header>...</header>
      <section id="candidates" class="space-y-10">...</section>
      <section id="top-recommendation">...</section>
    </main>
  </body>
</html>
```

## Header

仓库名称、日期，以及紧凑图例：实线框 = module、虚线 = seam、红色箭头 = 泄漏、粗深色框 = deep module。不要写介绍段落——直接进入候选项。

## 候选项卡片

让图表承担主要表达。文字保持稀疏、直白，自然使用（来自 `/codebase-design` 技能的）术语表词汇。

每个候选项使用一个 `<article>`：

- **标题**——简短，点明深化内容（例如“合并 Order intake pipeline”）。
- **Badge 行**——推荐强度（`Strong` = emerald、`Worth exploring` = amber、`Speculative` = slate），外加依赖类别标签（`in-process`、`local-substitutable`、`ports & adapters`、`mock`）。
- **文件**——等宽字体列表，`font-mono text-sm`。
- **之前 / 之后图**——核心内容。两列并排。模式见下文。
- **问题**——一句话。说明痛点。
- **解决方案**——一句话。说明会改变什么。
- **收益**——bullet，每条不超过 6 个词。例如“Tests hit one interface”“Pricing logic stops leaking”“Delete 4 shallow wrappers”。
- **ADR callout**（如适用）——amber 色调框中的一行文字。

不要写解释段落。如果图表必须借助一整段文字才能理解，就重画图表。

## 图表模式

选择适合候选项的模式，并混合使用。不要让每张图都长得一样——多样性本身就是目的之一。

### Mermaid 图（依赖 / 调用流的主力）

当重点是“X 调用 Y、Y 调用 Z，看看有多混乱”时，使用 Mermaid `flowchart` 或 `graph`。将其包在 Tailwind 风格卡片中，避免显得像从外部空降进来。使用 `classDef` 将泄漏边染成红色，将 deep module 设为深色。Sequence diagram 很适合表达“之前：6 次往返；之后：1 次”。

```html
<div class="rounded-lg border border-slate-200 bg-white p-4">
  <pre class="mermaid">
    flowchart LR
      A[OrderHandler] --> B[OrderValidator]
      B --> C[OrderRepo]
      C -.leak.-> D[PricingClient]
      classDef leak stroke:#dc2626,stroke-width:2px;
      class C,D leak
  </pre>
</div>
```

### 手工框与箭头（Mermaid 布局与你对着干时）

用带边框和标签的 `<div>` 表示 module。用内联 SVG `<line>` 或 `<path>` 表示箭头，并在相对定位容器上绝对定位。当你希望“之后”图看起来像一个带粗边框的 deep module，内部元素变灰时，采用此方式——Mermaid 无法呈现出正确的视觉重量。

### 横截面（适合表现分层的浅化）

堆叠水平条带（`h-12 border-l-4`），展示一次调用穿过的各个层。之前：6 层很薄，每层几乎什么都不做。之后：1 条粗带，标注合并后的职责。

### 质量图（适合表现“interface 与 implementation 一样宽”）

每个 module 使用两个矩形——一个表示 interface 表面积，一个表示 implementation。之前：interface 矩形几乎与 implementation 矩形一样高（shallow）。之后：interface 矩形很矮，implementation 矩形很高（deep）。

### 调用图折叠

之前：以嵌套框呈现函数调用树。之后：将同一棵树折叠进一个框中，把现在属于内部的调用以淡色显示在框内。

## 样式指南

- 采用简洁的编辑风格，而不是企业 dashboard 风格。留出充足空白。标题可选用衬线字体（`font-serif` 与 stone/slate 很搭）。
- 谨慎使用颜色：一个强调色（emerald 或 indigo），另用红色表示泄漏、amber 表示警告。
- 图表高度保持在约 320px，使之前/之后可以舒适地并排显示，无需滚动。
- 图表中的 module label 使用 `text-xs uppercase tracking-wider`——它们应读起来像示意图，而不是 UI。
- 唯一脚本是 Tailwind CDN 和 Mermaid ESM import。除此之外报告保持静态——没有 app code，除 Mermaid 自身渲染外没有交互。

## 首要建议一节

使用一张较大的卡片。候选项名称、说明原因的一句话、指向其卡片的 anchor link。仅此而已。

## 语气

使用简洁、直白的中文——但架构名词和动词必须直接来自 `/codebase-design` 技能。简洁不能成为偏离词汇的借口。

**必须准确使用：**module、interface、implementation、depth、deep、shallow、seam、adapter、leverage、locality。

**绝不要替换为：**component、service、unit（代替 module）· API、signature（代替 interface）· boundary（代替 seam）· layer、wrapper（实际指 module 时）。

**符合此风格的措辞：**

- “Order intake module 很 shallow——interface 几乎等同于 implementation。”
- “Pricing 跨 seam 泄漏。”
- “深化：一个 interface，一个测试位置。”
- “两个 adapter 证明 seam 合理：生产环境使用 HTTP，测试使用内存实现。”

**收益 bullet** 应以术语表词汇命名收益：*“locality：bug 集中在一个 module”*、*“leverage：一个 interface，N 个调用点”*、*“interface 缩小；implementation 吸收 wrapper”*。不要写*“更容易维护”*或*“代码更干净”*——这些词不在术语表中，不值得占据位置。

不要含糊其辞，不要铺垫，不要写“值得注意的是……”。能写成 bullet 的句子就写成 bullet。能删掉的 bullet 就删掉。某个术语如果不在 `/codebase-design` 术语表中，先从中寻找可用词汇，再考虑发明新词。
