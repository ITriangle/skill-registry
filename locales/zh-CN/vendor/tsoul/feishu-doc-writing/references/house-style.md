# 飞书文档房屋风格

本文件只给 XML 配方和结构示例。CLI、block 操作、画板插入走 lark-doc。

## Callout

全篇最多 4 个，颜色只蓝。第一个结论框可加字色。

```xml
<callout emoji="💡" background-color="rgb(240,244,255)" border-color="rgb(130,167,252)" text-color="rgb(36,91,219)">
  <p><b>核心结论：</b>一句话决策，加粗关键词。</p>
</callout>
<callout emoji="📌" background-color="rgb(240,244,255)" border-color="rgb(130,167,252)">
  <p><b>读文档时先分清两层：</b>A 是什么；B 是什么。不要把两层合成一个状态。</p>
</callout>
```

允许的加粗标签：`核心结论：` / `读文档时先分清两层：` / `关键设计：` / `信任边界：`。emoji 可用 💡 📌 🔐。子块只放段落或列表，不放表格。

## 表格

```xml
<table>
  <colgroup>
    <col width="160"/>
    <col width="280"/>
    <col width="280"/>
  </colgroup>
  <thead>
    <tr>
      <th background-color="rgba(245,246,247,0.9)" vertical-align="top"><p>维度</p></th>
      <th background-color="rgba(245,246,247,0.9)" vertical-align="top"><p>A</p></th>
      <th background-color="rgba(245,246,247,0.9)" vertical-align="top"><p>明确边界</p></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td vertical-align="top"><p><b>先列概念</b></p></td>
      <td vertical-align="top"><p>做什么。</p></td>
      <td vertical-align="top"><p>不做什么。</p></td>
    </tr>
  </tbody>
</table>
```

- 表头统一 `rgba(245,246,247,0.9)`，单元格 `vertical-align="top"`。
- 先列加粗或 `<code>`。列宽用 `<colgroup>`，避免过宽。
- 模块 / 分流 / 角色表必须有边界列。短对照用「维度 | A | B」。

## 元信息与段落

```xml
<title>主题：职能</title>
<p>对照：2026-09-04　状态：内部同步稿</p>
<p><b>工单真源。</b>一句话定义。标识符写成 <code>/admin/feedback</code>。</p>
```

落地顺序：

```xml
<ol>
  <li seq="auto"><b>先做</b>：对齐稿，产品确认前不改代码。</li>
  <li seq="auto"><b>下一步</b>：确认后的实现切片。</li>
</ol>
```

## 图

- 流程图、架构图用 `<whiteboard type="svg">` 完整自包含 SVG；思维导图 / 时序 / 饼图 / 甘特才用 mermaid 画板。
- 禁止在正文放 mermaid 源码块。
- 图前：`<p><b>分流后三条路。</b>这张图在回答什么。</p>`
- 图后：一段把分支收束成文字，不重复图里每个节点。
- SVG 不用 `<radialGradient>` / `<filter>` / `<clipPath>` / `<mask>`；连线用正交折线；禁止白底大方卡片网格。

## 结构示例

参照稿形态（不必同题）：

1. 元信息行 + **核心结论** + **读文档时先分清两层**
2. `1. 目标与边界` — 真源、不做的事
3. `2. 流程 / 总体架构` — 短列表 + 导语 + 画板 + 收束
4. 之后按源稿编号展开对照表；源稿没有的章不补

| 源稿常见块 | 飞书表达 |
|---|---|
| 开篇三段结论 | 两个蓝 callout，不把元信息放进框 |
| mermaid flowchart | SVG 画板；图前导语、图后一句 |
| 模块 / 标签表 | 表 + 边界列或「不打」列 |
| A vs B 散文 | 对照表：维度 \| A \| B |
| 落地 TODO | 编号 + **先做 / 下一步**，不是 checkbox |

## 转义

标签本身不转义。文本里的 `&` `<` `>` 写成 `&amp;` `&lt;` `&gt;`。
