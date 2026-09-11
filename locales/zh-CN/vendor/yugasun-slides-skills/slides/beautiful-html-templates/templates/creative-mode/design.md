---
version: alpha
name: Creative Mode
description: A neo-brutalist editorial presentation system built for 1920x1080 slides. The deck anchors on a warm cream canvas with heavy 4px ink borders, hard offset drop-shadows, and a bold four-color accent palette (forest green, hot pink, burnt orange, sunshine yellow). Display headlines run Archivo Black in pure uppercase — aggressive, loud, zero letter-spacing softness. Monospace labels in JetBrains Mono echo a typesetting rule-sheet. Body copy sits in Space Grotesk. Every slide uses flat color-blocking with no gradients, no rounded cards, and no subtlety. The aesthetic is part Bauhaus grid, part punk zine, part Swiss editorial.

colors:
  cream: "#EFE9D9"
  cream-2: "#E4DCC4"
  ink: "#0F0F0F"
  ink-2: "#2A2A2A"
  green: "#1F8A4C"
  green-dark: "#136636"
  pink: "#F06CA8"
  pink-dark: "#D14E8B"
  orange: "#E85A1F"
  yellow: "#F5C518"

typography:
  display-jumbo:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 220px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.01em
    textTransform: uppercase
  display-hero:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 160px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.01em
    textTransform: uppercase
  display-xl:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 140px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.01em
    textTransform: uppercase
  display-lg:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 100px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.01em
    textTransform: uppercase
  display-md:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 96px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.01em
    textTransform: uppercase
  display-sm:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 84px
    fontWeight: 400
    lineHeight: 0.92
    letterSpacing: -0.01em
    textTransform: uppercase
  display-xs:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: -0.01em
    textTransform: uppercase
  stat-num:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 96px
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: 0
  step-num:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 140px
    fontWeight: 400
    lineHeight: 0.85
    letterSpacing: 0
  step-title:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 34px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    textTransform: uppercase
  stamp-num:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: 0
  marker-label:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 46px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    textTransform: uppercase
  badge-label:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    textTransform: uppercase
  table-head:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    textTransform: uppercase
  table-label:
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
    textTransform: uppercase
  body-lg:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  mono-label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.06em
    textTransform: uppercase
  mono-kicker:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.14em
    textTransform: uppercase
  mono-tag:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.1em
    textTransform: uppercase
  mono-chart:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase

spacing:
  slide-gutter: 96px
  chrome-gutter: 64px
  grid-gap: 28px
  cell-pad: 32px
  step-pad: 28px
  topbar-top: 48px
  meta-bottom: 40px
  table-cell-pad: 18px 26px

canvas:
  width: 1920px
  height: 1080px

components:
  slide-chrome:
    topbar:
      fontFamily: "JetBrains Mono, monospace"
      fontSize: 24px
      letterSpacing: 0.08em
      textTransform: uppercase
      position: absolute
      left: 64px
      right: 64px
      top: 48px
    topbar-pill:
      border: "2px solid {colors.ink}"
      padding: 6px 14px
      borderRadius: 999px
    slide-meta:
      fontFamily: "JetBrains Mono, monospace"
      fontSize: 24px
      letterSpacing: 0.06em
      textTransform: uppercase
      position: absolute
      left: 64px
      right: 64px
      bottom: 40px
    slide-meta-dot:
      width: 10px
      height: 10px
      background: "{colors.ink}"
      borderRadius: 50%
  stat-cell:
    border: "4px solid {colors.ink}"
    padding: 28px 32px
  stat-cell-green:
    background: "{colors.green}"
    color: "{colors.cream}"
  stat-cell-pink:
    background: "{colors.pink}"
    color: "{colors.ink}"
  stat-cell-cream:
    background: "{colors.cream}"
    color: "{colors.ink}"
  stat-cell-orange:
    background: "{colors.orange}"
    color: "{colors.cream}"
  step-card:
    border: "4px solid {colors.ink}"
    padding: 28px
    height: 420px
  step-card-cream:
    background: "{colors.cream}"
    color: "{colors.ink}"
  step-card-pink:
    background: "{colors.pink}"
    color: "{colors.ink}"
  step-card-yellow:
    background: "{colors.yellow}"
    color: "{colors.ink}"
  step-card-green:
    background: "{colors.green}"
    color: "{colors.cream}"
  step-arrow:
    borderTop: "18px solid transparent"
    borderBottom: "18px solid transparent"
    borderLeft: "24px solid {colors.ink}"
  table:
    border: "4px solid {colors.ink}"
    background: "{colors.cream-2}"
    rowBorder: "3px solid {colors.ink}"
    colBorder: "3px solid {colors.ink}"
  table-head-row:
    background: "{colors.ink}"
    color: "{colors.cream}"
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 28px
    borderColor: "{colors.cream}"
  table-col-pink:
    background: "{colors.pink}"
    color: "{colors.ink}"
  table-col-green:
    background: "{colors.green}"
    color: "{colors.cream}"
  table-col-orange:
    background: "{colors.orange}"
    color: "{colors.cream}"
  marker-block:
    background: "{colors.pink}"
    border: "4px solid {colors.ink}"
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 46px
    hardShadow: "24px 24px 0 {colors.orange}, 24px 24px 0 4px {colors.ink}"
  iso-panel:
    background: "{colors.green}"
    border: "4px solid {colors.ink}"
  stacked-block:
    border: "4px solid {colors.ink}"
    hardShadow: "18px 18px 0 {colors.ink}"
  badge-rotated:
    background: "{colors.yellow}"
    border: "4px solid {colors.ink}"
    fontFamily: "Archivo Black, sans-serif"
    fontSize: 28px
    textTransform: uppercase
    transform: rotate(-4deg)
  stamp:
    background: "{colors.pink}"
    border: "4px solid {colors.cream}"
    width: 340px
    height: 340px
    transform: rotate(-6deg)
  stamp-inner:
    border: "4px solid {colors.cream}"
    borderRadius: 50%
  kicker-block:
    background: "{colors.ink}"
    color: "{colors.cream}"
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 24px
    letterSpacing: 0.14em
    textTransform: uppercase
    padding: 8px 16px
  bar-chart-bar:
    border: "3px solid {colors.ink}"
  bar-chart-axis:
    borderRight: "3px solid {colors.ink}"
    borderBottom: "3px solid {colors.ink}"
  decorative-circle:
    background: "{colors.yellow}"
    border: "4px solid {colors.ink}"
    borderRadius: 50%
  closing-slide:
    background: "{colors.green}"
    color: "{colors.cream}"
---

## 概览

Creative Mode 是一套面向 1920x1080 演示的**新粗野主义编辑幻灯片系统**。底层审美选择是手法克制、表达凶猛：不要圆角卡片、不要渐变、不要暗示光源的阴影——只有平面色块，以及硬偏移投影（「Risograph」或「丝网印刷」那种，阴影是实心同色偏移）。

画布是暖奶油色（`{colors.cream}` — #EFE9D9），近黑墨色（`{colors.ink}` — #0F0F0F）用于描边、文字和规则线。四种强调色以满饱和开火：森林绿、热粉、焦橙、阳光黄。它们从不混溶——在幻灯片上对撞，对撞本身就是设计。

标题跑 **Archivo Black**（字重 400，因为这张展示脸本身就极重）严格全大写，行高收紧（0.92）。字号极端：收场页 220px，标题 160px。**JetBrains Mono** 承担全部元信息、标签、顶栏文字和坐标标签——强化「设计制品」或「技术手册」的语域。**Space Grotesk** 处理全部正文段落。

每一页都遵循同一套铬件外框：距顶 48px 的 JetBrains Mono 顶栏（左文字 + 右胶囊），距底 40px 的 JetBrains Mono 元信息页脚（左标签，右页码，中间墨色圆点分隔）。内容落在此外框内，左右各 96px 边距。

**关键特征：**
- 奶油画布（`{colors.cream}` — #EFE9D9）作为通用背景；绿色（`{colors.green}` — #1F8A4C）只用于收场页。
- 每个结构元素都是 4px 实心墨色描边——卡片、面板、表格单元格、图表坐标轴。
- 用硬偏移 box-shadow 代替模糊投影：特色块上用 `24px 24px 0 color, 24px 24px 0 4px ink`。
- Archivo Black 展示字体全大写，行高 0.92，极端紧凑。
- 四种强调色作平面填色；每页用其中两到三种，从不四种同时上场。
- 顶栏胶囊徽章（JetBrains Mono，2px 墨色描边，999px 圆角）是每页唯一的圆角元素。

## 颜色

### 画布与墨色
- **Cream**（`{colors.cream}` — #EFE9D9）：通用幻灯片背景。暖，不是白。把这套 deck 从无菌白底幻灯片里区分出来。
- **Cream 2**（`{colors.cream-2}` — #E4DCC4）：深一档的奶油色。专用于对比表的背景填充，在墨色描边内做出微微凹进的表面。
- **Ink**（`{colors.ink}` — #0F0F0F）：近黑，用于全部描边、正文、规则线、顶栏铬件和收场印章描边。不是纯 #000000——略微柔化。
- **Ink 2**（`{colors.ink-2}` — #2A2A2A）：更软的近黑，用于次级正文、统计格内的描述、图表脚注。

### 强调色
- **Green**（`{colors.green}` — #1F8A4C）：森林绿。主导强调色。用在统计格、图示面板、流程步骤，以及整页背景以求最大视觉冲击。
- **Green Dark**（`{colors.green-dark}` — #136636）：更深的绿色变体——可用于杠杆/纵深装饰效果。不作主表面填充。
- **Pink**（`{colors.pink}` — #F06CA8）：热粉。高能量。用在拨动开关图示、章节标记、统计格、流程步骤和印章元素。
- **Pink Dark**（`{colors.pink-dark}` — #D14E8B）：更深的粉，用于装饰杠杆元素的纵深。可用于阴影侧强调。
- **Orange**（`{colors.orange}` — #E85A1F）：焦橙。特色块上的硬投影色；也可用作统计格填充、柱状图颜色和表格列背景。
- **Yellow**（`{colors.yellow}` — #F5C518）：阳光黄。用在装饰圆、流程步骤、旋转徽章和柱状图柱。一种暖的标点色。


## 字体

### 字族
系统使用三套字体，各守严格语域：
- **Archivo Black** — 展示标题、步骤数字、统计数字、表格标签、全部大写演示文字。本身极重，不需要额外 font-weight。
- **JetBrains Mono** — 全部元信息：顶栏标签、元信息页脚、kicker 标签、图表坐标、图例行、图层标签、图注。承担「技术规格」声线。
- **Space Grotesk** — 仅正文：正文栏文字（第 2 页）、统计格描述、图示副文、步骤说明、收场副标。

### 展示字号阶梯
幻灯片画布是 1920x1080px，所以字号远大于网页常态。

| Token | 字号 | 用途 |
|---|---|---|
| `{typography.display-jumbo}` | 220px | 超大标题或收场标题 |
| `{typography.display-hero}` | 160px | 主 deck 标题或 hero 名称 |
| `{typography.display-xl}` | 140px | 章节开场展示标题 |
| `{typography.display-lg}` | 100px | 与面板并排的章节标题 |
| `{typography.display-md}` | 96px | 中等重量的章节标题 |
| `{typography.display-sm}` | 84px | 数据密集版式的章节标题 |
| `{typography.display-xs}` | 72px | 网格版式的章节标题 |
| `{typography.step-num}` | 140px | 步进版式里的大序号数字 |
| `{typography.stat-num}` | 96px | 统计或数据格里的大数字 |
| `{typography.stamp-num}` | 64px | 印章或封缄数字 |
| `{typography.marker-label}` | 46px | 特色标记或 callout 块标签 |
| `{typography.step-title}` | 34px | 卡片或步骤标题 |
| `{typography.table-head}` | 28px | 表头或标签行文字 |
| `{typography.badge-label}` | 28px | 旋转徽章或注释标签 |

### 等宽字号阶梯
所有 JetBrains Mono 文字都是 24px。字距按用途变化：
- 顶栏标签：0.08em
- 元信息页脚：0.06em
- Kicker 标签（反相）：0.14em
- 图表坐标：0.08em（经 `{typography.mono-chart}`）
- 图例行：0.06em
- 图层标签：0.1em

### 正文字号阶梯
- `{typography.body-lg}`（28px）：宽栏版式或导语段落的正文。
- `{typography.body-md}`（24px）：统计格、图示注释、步骤说明、脚注和副标行的正文。

### 原则
Archivo Black 的行高是 0.92——标题会叠进自己的 cap-height，这是故意的。展示脸锁定全大写不可商量；小写 Archivo Black 会破坏编辑语域。等宽脸用慷慨字距（0.06–0.16em）来感觉像打字机标签。永远不要给 Archivo Black 或 Space Grotesk 加字距。

## 布局

### 画布系统
每一页都精确 1920×1080px，固定、不可滚动的视口。`deck-stage` 自定义元素负责居中和缩放。

### 边距系统
- **铬件边距**（左右 64px）：仅顶栏和 slide-meta 使用。
- **内容边距**（左右 96px）：全部内容使用——标题、正文、网格。
- 标题偶尔会向右推到距右缘 96px 以内，或用 `right: 1000px` / `right: 900px` 约束，以便与右侧面板图示共存。


### 铬件外框（所有幻灯片）
```
┌─ topbar @ top:48px, left:64px, right:64px ──────────────────────────────────┐
│  章节标签                                              [胶囊徽章]            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   内容（左侧 96px 边距，右侧 96px 边距）                                     │
│                                                                              │
├─ slide-meta @ bottom:40px, left:64px, right:64px ───────────────────────────┤
│  描述标签                                              01 • 08               │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 纵深与抬升

本系统使用**零模糊阴影**。纵深通过两种手法表达：

### 硬偏移阴影
招牌处理：第二块实心形状在 X 和 Y 上都偏移固定量。使用两个取值：
- **大偏移**（24px 24px）：标记和海报开关这类特色块 — `box-shadow: 24px 24px 0 {colors.orange}, 24px 24px 0 4px {colors.ink}`。第一层阴影是彩色偏移；第二层是围着它的墨色描边。
- **中偏移**（18px 18px）：图示里的叠放块 — `box-shadow: 18px 18px 0 {colors.ink}`。纯墨色阴影。

### 色块对比
纵深感来自表面并置：奶油上的 cream-2（表格）、奶油上的墨（kicker 块）、奶油上的绿（图示面板）。对比本身就能干活时，不需要阴影。

### 平面元素
顶栏、元信息页脚、图表轴线、图例色块：平面，无阴影，无圆角。

## 形状与处理

### 圆角
- **0px（直角）**：全部结构元素——统计格、步骤卡、表格单元格、图表柱、图示面板、叠放块。不圆。
- **50%（圆）**：图示里的装饰圆（黄圆）、顶栏胶囊点（幻灯片元信息分隔点）。
- **999px（胶囊）**：仅顶栏徽章胶囊。系统整体方形的唯一例外，读成标签芯片而不是卡片。
- **旋转元素**：对比徽章旋转 -4deg；收场印章旋转 -6deg。这是系统仅有的非正交摆放。

### 描边
- **4px solid `{colors.ink}`**：全部结构描边——统计格、步骤卡、图示面板、表格（外框）、海报块、标记块、开关块、印章。
- **3px solid `{colors.ink}`**：全部内部结构线——表格行、表格列、图表坐标轴、柱状图柱。
- **2px solid `{colors.ink}`**：顶栏胶囊徽章。
- **3px dashed `{colors.ink}`**：虚线水平规则，把流程页的顶栏与其流程卡分开。

### 装饰元素
- **拨动开关**：粉色方块，带杠杆形（倾斜的 div）和厚/暗底面，橙色偏移阴影加墨色描边。
- **叠放块**：四块重叠的绝对定位矩形，粉、黄、橙、cream-2，带 18px 墨色硬阴影。
- **圆形叠层**：绿色方块中央的黄圆——形状对比充当装饰图形。
- **印章**：粉色旋转方块，内有奶油色圆形内描边——充当封缄或批准印记。

## 该做与不该做

### 该做
- 每个结构元素都用 4px 墨色描边。更细显得软；更厚像网页组件。
- 硬偏移阴影只用两个尺寸：特色 hero 块 24px，图示叠放块 18px。不要混用尺寸。
- 所有 Archivo Black 用法保持全大写。句首大写的这套字读成另一个品牌。
- 每页用两到三种强调色。一页上四种全上是噪音。
- 把绿色背景留给单独一页主导页。稀缺才给它冲击力。
- 全部标签、元信息、索引、图注和坐标文字用 JetBrains Mono。永远不要用它做正文或标题。
- 全部展示文字保持行高 0.92。更松的行距会破坏紧编辑语域。
- 所有幻灯片一致维持 96px 内容边距和 64px 铬件边距。

### 不该做
- 不要给卡片圆角（顶栏胶囊除外）。圆角信号是「友好 SaaS」；尖角信号是「编辑精度」。
- 不要用渐变、带模糊的投影或光晕。全部纵深必须来自硬偏移或色彩对比。
- 不要用句首大写的 Archivo Black。永远不要把展示脸改成小写。
- 不要给 Archivo Black 加字距（-0.01em 除外，它已经编码进去）。额外 tracking 会破坏它的密度。
- 不要引入第五种强调色。四色色板就是品牌约束。
- 不要用纯白（#ffffff）做背景。奶油是画布；白读成空白。
- 不要用 Space Grotesk 做标签或元信息。那个角色属于 JetBrains Mono。
- 不要再加字体。三族栈已经完整。
- 不要居中对齐正文。全部正文左对齐；居中文字破坏网格纪律。
- 不要柔化印章或徽章的旋转。-4deg 和 -6deg 是故意的不完美信号。

## 响应式行为

本模板**专为 1920x1080 演示显示设计**。它不是网页，没有移动断点。`deck-stage` web 组件通过 CSS transform 处理视口缩放，因此 1920x1080 画布在任意屏幕尺寸上按比例缩放，版式不变。

### 触控 / 演示行为
- 幻灯片通过键盘方向键或演示翻页器前进（由 `deck-stage.js` 处理）。
- 没有定义、也不需要悬停状态。
- 不存在交互表单元素。

### 印刷 / 导出行为
- 在 96dpi 下，1920x1080 画布对应标准 20x11.25 英寸画幅。
- 导出 PDF 时，建议对 1920x1080 视口截取，或浏览器 100% 缩放打印到 PDF。
- 按 1pt = 1.333px，标题的有效印刷字号从 54pt（72px）到 165pt（220px）——对海报/标题卡是正确的。

## CJK 与国际内容

### 推荐中文搭配

| 角色 | 拉丁字体 | 推荐中文搭配 | 来源 |
|---|---|---|---|
| 展示 / 标题（Archivo Black 全大写 400） | Archivo Black | 思源宋体 Noto Serif SC 900 | Google Fonts |
| 正文（Space Grotesk 400） | Space Grotesk | 思源宋体 Noto Serif SC 400 | Google Fonts |
| 等宽 / 标签（JetBrains Mono 全大写） | JetBrains Mono | JetBrains Mono（仅拉丁/数字——铬件等宽保持拉丁） | Google Fonts |

### 混排策略

用 **策略 A——单一字体栈加回退**：在同一 `font-family` 栈里把 Noto Serif SC 声明在拉丁脸*之后*，这样拉丁字形以 Archivo Black / Space Grotesk 渲染，CJK 字形自动落到 NSC。JetBrains Mono 铬件保持仅拉丁/数字——顶栏标签、slide-meta、坐标刻度和图注不需要 CJK 回退（而且 JetBrains Mono 设计上没有 CJK 字形）。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Space+Grotesk:wght@300..700&family=JetBrains+Mono:wght@400..500&family=Noto+Serif+SC:wght@400;900&display=swap" rel="stylesheet">
```

```css
:root {
  --font-display: "Archivo Black", "Noto Serif SC", sans-serif;
  --font-body: "Space Grotesk", "Noto Serif SC", sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;
}
/* Display headlines use Noto Serif SC 900; body uses NSC 400. */
```

### 通用 CJK 调整

- **行高**：把 CJK 正文行高提到约 1.55（从 1.4）——汉字比拉丁小写需要更多纵向呼吸。展示用 NSC 900 在 100–220px 时，行高保持紧，约 1.0（NSC 重字重在展示尺寸上比 Archivo Black 需要更少行距）。
- **字距**：汉字跑句上把 `letter-spacing` 归零（讨好 Archivo Black 大写的负 tracking 会把汉字笔画挤在一起）。紧 tracking 只留在拉丁跨度上。
- **文字变换**：内容是汉字时，去掉任何展示/标签/等宽上的 `text-transform: uppercase`——中文没有大小写；强制大写对汉字无用，却会弄坏里面夹着的拉丁缩写渲染。
- **标点**：中文句子用中文全角标点（，。：；「」），拉丁用半角（`,.:;""`）。永远不要把半角标点混进中文句子。
- **标题不加句号**：中文标题惯例省略句末 。——从展示字符串里去掉。
- **盘古之白**：相邻汉字与拉丁/数字跑句之间插入细空格（或普通空格）（例如 `2026 年`、`AI 产品`）。改善混排可读性。
- **一句一字体**：不要在句中切换 CJK 字族。给定文本跑句只选一个字重的 Noto Serif SC，永远不要在一个短语里用两个。

### 审美说明

Creative Mode 的新粗野主义语域依赖 Archivo Black 在 100–220px 上的极端密度——没有汉字脸能精确匹配这种体量，所以字重 900 的 Noto Serif SC 是最接近的现成替代。NSC 900 的调制衬线笔画会比朋克 zine 的 Archivo Black 声线更文学，但四色块色板、4px 墨色描边和硬 24px 偏移阴影承担了大部分粗野主义工作——字体变成一套更响系统里的一个组件，而不是系统本身。Archivo Black 的「永远全大写」规则对汉字无意义（没有大小写），所以内容切到中文时同时丢掉 `text-transform: uppercase` 和 -0.01em tracking——NSC 900 只靠尺寸和颜色站得住。JetBrains Mono 铬件（顶栏胶囊、slide-meta、坐标刻度、kicker 块）故意保持仅拉丁/数字：用等宽渲染 `04 / 08` 页码，但元信息页脚里的任何中文描述标签用 NSC 400。四种强调色（绿 / 粉 / 橙 / 黄）、统计格色块、表格处理和装饰几何（印章、徽章、叠放块）都与内容无关。

### 已知 CJK 缺口

**重拉丁展示没有精确的 CJK 对等。** Archivo Black 在 220px 上的粗野密度是系统签名——Noto Serif SC 900 是常见可获得的最重汉字字重，但读成文学衬线而不是海报 grotesque。用 Creative Mode 做的中文 deck 会比拉丁原版少约 30%「朋克 zine」感；补偿办法是更用力压在强调色块、硬偏移阴影和旋转徽章 / 印章元素上。展示不要改用 `Smiley Sans Oblique`——它的斜切与系统严格正交矩形几何冲突。NSC 没有斜体轴，但系统任何地方都不用斜体——没有损失。等宽铬件的「技术规格」声线最好靠把全部 JetBrains Mono 内容保持拉丁/数字、把 NSC 只留给标题和正文角色来保住。

## 迭代指南

1. 新幻灯片版式必须尊重铬件外框：顶栏 top:48px left:64px，slide-meta bottom:40px left:64px。
2. 内容从每侧边缘 96px 处开始。
3. 加数据区块（图表、表格、网格）时，上方配展示标题，内部用 JetBrains Mono 标签。
4. 每页选两到三种强调填充。永远不要在单页混用全部四种。
5. 硬阴影只加在特色单一元素上（标记、特色块）。网格单元格不要各自加阴影。
6. 新步骤/统计卡遵循现有颜色序列模式：奶油与强调色交替，序列以绿色收尾。
7. 全部描边是 4px solid 墨。表格或坐标轴内的内部子描边是 3px solid 墨。
8. 旋转元素（徽章、印章）用单一固定角度（-4deg、-6deg）。不要引入其他角度。
9. 图标和图示是纯 CSS 几何形状（div、描边、伪元素）。不需要外部图片或 SVG。

## 已知缺口

- `deck-stage.js` 脚本（幻灯片前进、键盘导航）是此处未文档化的外部依赖。
- 幻灯片之间的动画和转场不在本模板范围内；所有幻灯片都是静态的。
- 标题页海报含一个由嵌套 div 构成的装饰拨动开关图示；它没有功能状态。
- 图表数据（柱高、数值、标签）写死为内联样式和占位内容——没有数据绑定层。
- 表格数据全是占位；不支持动态填充。
- `--rule` CSS 变量（#0F0F0F，与 `--ink` 相同）已定义但未显式使用——它留给水平规则元素，可视为 ink 的别名。
- Archivo Black 的字体回退是 `sans-serif`——设计要正确渲染，必须从 Google Fonts 加载该字体。
