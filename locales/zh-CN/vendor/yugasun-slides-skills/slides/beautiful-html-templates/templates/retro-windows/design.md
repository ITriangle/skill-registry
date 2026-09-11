---
version: alpha
name: Retro Windows
description: A Windows 95 / 98 desktop-OS aesthetic rendered as a presentation system. Every slide is a window — beveled chrome, navy gradient title bar, MS Sans Serif body type, with chart areas, group boxes, and panels arranged as if they were software UI from 1995. The palette is the original Win9x system colors (gray button-face, navy title bars, white sunken inputs) with retro accent hues (DOS green, brick red, mustard yellow, teal cyan) reserved for status text and chart data. Pixel-font (Press Start 2P) and terminal-font (VT323) appear sparingly for nostalgic punctuation. The effect is half playful nostalgia, half functional dashboard — a deck that reads as a software product running on a CRT monitor.

colors:
  bg-gray: "#c0c0c0"
  bg-light: "#d4d0c8"
  bg-dark: "#808080"
  white: "#ffffff"
  black: "#000000"
  text-dark: "#222222"
  blue-navy: "#000080"
  blue-bright: "#0000a0"
  blue-light: "#1084d0"
  green-retro: "#008000"
  red-retro: "#800000"
  yellow-retro: "#808000"
  cyan-retro: "#008080"
  text-gray: "#555555"

color-aliases:
  btn-face: bg-light
  btn-highlight: white
  btn-shadow: "#404040"
  btn-dark-shadow: black

typography:
  body:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  text-xl:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
  text-lg:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
  text-md:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
  text-sm:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  text-xs:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
  metric-xl:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.1
  title-bar:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.5px
  group-box-title:
    fontFamily: "MS Sans Serif, Segoe UI, Tahoma, Geneva, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.0
  pixel-display:
    fontFamily: "'Press Start 2P', cursive"
    fontSize: "20–24px"
    fontWeight: 400
    lineHeight: 1.8
  terminal:
    fontFamily: "'VT323', monospace"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
  nav-hint:
    fontFamily: "'VT323', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.0

spacing:
  slide-pad: "24px 32px 44px 32px"
  win-body-pad: "20px 24px 24px 24px"
  panel-pad: 16px
  group-box-pad: "20px 18px 16px 18px"
  panel-sunken-pad: 12px
  gap-1: 6px
  gap-2: 10px
  gap-3: 16px
  gap-4: 24px

canvas:
  width: 100vw
  height: 100vh

components:
  crt-overlay:
    backgroundImage: "repeating-linear-gradient(0deg, rgba(0,0,0,0.03) 0px, rgba(0,0,0,0.03) 1px, transparent 1px, transparent 3px)"
    zIndex: 9999
    description: "Fixed, full-viewport scanline overlay at 3% black opacity that sits above all content. Imitates the horizontal phosphor lines of a CRT monitor. Pointer-events disabled."
  win-window:
    background: "{colors.bg-light}"
    border: "2px solid {colors.white} (top/left) + 2px solid {colors.black} (right/bottom)"
    boxShadow: "inset 1px 1px 0 {colors.white}, inset -1px -1px 0 #404040"
    description: "The signature framing element. Every slide is one (or more) win-window. The asymmetric border + double inset shadow creates the Win9x beveled raised effect — top-left highlighted, bottom-right shadowed."
  win-titlebar:
    background: "linear-gradient(90deg, {colors.blue-navy} 0%, {colors.blue-bright} 100%)"
    color: "{colors.white}"
    padding: "4px 8px"
    fontSize: 14px
    fontWeight: 700
    description: "Navy-blue gradient bar at the top of every window. Contains a left lockup (icon + filename in caps) and a right cluster of three minimize/maximize/close buttons (_, [], X)."
  win-titlebar-inactive:
    background: "linear-gradient(90deg, #808080 0%, #a0a0a0 100%)"
    description: "Grayed-out title bar variant for inactive/secondary windows (used when a slide contains multiple stacked windows representing different states)."
  win-btn:
    width: 20px
    height: 18px
    background: "{colors.bg-light}"
    border: "2px solid {colors.white} (top/left) + 2px solid {colors.black} (right/bottom)"
    description: "Beveled-raised mini button used inside the title bar (_, [], X) and elsewhere. Active state inverts the bevel."
  btn-retro:
    background: "{colors.bg-light}"
    border: "2px solid {colors.white} (top/left) + 2px solid {colors.black} (right/bottom)"
    padding: "6px 24px"
    fontSize: 14px
    description: "Standard Win9x command button. Beveled raised; active state inverts the bevel so the button appears pressed in."
  group-box:
    border: "2px solid #404040 (top/left) + 2px solid {colors.white} (right/bottom)"
    padding: "20px 18px 16px 18px"
    background: "{colors.bg-light}"
    description: "Sunken-bevel framed container with a title label that breaks the top border (the title sits in a small background-painted notch at top-left). The Win9x equivalent of a fieldset/legend."
  group-box-title:
    position: absolute
    top: -10px
    left: 12px
    background: "{colors.bg-light}"
    padding: "0 8px"
    fontSize: 13px
    fontWeight: 700
    description: "The title label that sits on top of a group-box's upper border, painted with the parent background to mask the border behind it."
  panel-raised:
    background: "{colors.bg-light}"
    border: "2px solid {colors.white} (top/left) + 2px solid {colors.black} (right/bottom)"
    padding: 16px
    description: "Raised-bevel panel. Used for tool palettes, button strips, and elevated content regions inside a window body."
  panel-sunken:
    background: "{colors.white}"
    border: "2px solid #404040 (top/left) + 2px solid {colors.white} (right/bottom)"
    padding: 12px
    description: "Sunken-bevel panel with a white interior. Used for text input fields, read-only data displays, and status regions. The white interior is the system's signal for 'this is content, not chrome.'"
  progress-bar:
    width: "100%"
    height: 24px
    background: "{colors.white}"
    border: "2px solid #404040 (top/left) + 2px solid {colors.white} (right/bottom)"
    padding: 2px
    description: "Sunken white well containing a solid navy fill div whose width represents the data value. The fill is `{colors.blue-navy}` solid — no gradient, no animation beyond width transition."
  retro-list:
    listStyle: none
    marker: "> (chevron)"
    markerColor: "{colors.blue-navy}"
    description: "Custom-bullet list where each item is prefixed with a navy '>' character. The chevron is set via ::before, never via list-style."
  retro-check:
    checkBoxSize: "16px"
    checkBoxBorder: "2px solid {colors.black} (top/left) + 2px solid {colors.white} (right/bottom)"
    checkMarker: "x"
    description: "Sunken white square checkbox with a literal lowercase 'x' character as the checked-state marker. Inset-beveled the opposite direction from buttons."
  retro-table:
    borderCollapse: collapse
    fontSize: 14px
    headerBackground: "{colors.bg-gray}"
    headerBorder: "1px solid #404040"
    cellBackground: "{colors.white}"
    cellBorder: "1px solid {colors.bg-gray}"
    zebraRowBackground: "#f0f0f0"
    description: "Pixel-flat data table with gray headers, white cells, light-gray border lines, and a barely-different zebra fill on alternate rows."
  marquee:
    background: "{colors.white}"
    border: "1px inset {colors.bg-gray}"
    padding: "3px 0"
    animation: "marquee 14s linear infinite"
    description: "Scrolling text inside a sunken white well. The animation translates the text from 100% right to -100% left over 14 seconds. The original Win marquee element re-implemented in CSS."
  win-icon:
    width: 18px
    height: 18px
    background: "{colors.white}"
    border: "1px solid {colors.black}"
    fontSize: 11px
    color: "{colors.blue-navy}"
    fontWeight: 700
    description: "Tiny 18px square icon next to a title-bar filename — a navy-on-white letter glyph that imitates an application icon. The glyph is a 1-character mnemonic of the window's role (P for Presentation, R for README, D for Dataview, etc.)."
  tree-item:
    fontSize: 14px
    indent: "24px per level"
    folderGlyph: "📁 (U+1F4C1)"
    fileGlyph: "📄 (U+1F4C4)"
    expandedMarker: "-"
    collapsedMarker: "+"
    description: "Explorer-style hierarchical tree view. Each row carries an expand marker (+/−), a folder or file emoji glyph, and the label text. Indentation steps by 24px per nesting level."
  separator-vertical:
    width: 2px
    background: "#404040"
    borderLeft: "1px solid {colors.white}"
    margin: "0 12px"
    description: "Beveled vertical separator between inline elements — the Win9x equivalent of a vertical rule."
  hr-retro:
    borderTop: "1px solid #404040"
    borderBottom: "1px solid {colors.white}"
    margin: "14px 0"
    description: "Beveled horizontal rule. Two stacked 1px lines (dark on top, white on bottom) create the engraved-in look."
  nav-dot:
    width: 12px
    height: 12px
    background: "{colors.bg-gray}"
    border: "2px solid {colors.white} (top/left) + 2px solid {colors.black} (right/bottom)"
    activeBackground: "{colors.blue-navy}"
    description: "Beveled square mini-dot used as a slide-indicator chip. Active state fills navy with a 4px white center square."
  chart-canvas-host:
    background: "{colors.bg-light}"
    description: "Chart.js canvas embedded inside a panel-raised. Chart colors use {colors.blue-navy}, {colors.blue-bright}, {colors.blue-light}, {colors.green-retro}, {colors.cyan-retro}, {colors.yellow-retro}. Axis labels use MS Sans Serif at 11–12px in {colors.text-dark}. Gridlines in {colors.bg-gray}."
  scrollbar:
    width: 16px
    trackBackground: "{colors.bg-gray}"
    thumbBackground: "{colors.bg-gray}"
    thumbBorder: "2px solid {colors.white} (top/left) + 2px solid {colors.black} (right/bottom)"
    description: "Custom webkit scrollbar styled as a beveled-raised gray thumb on a flat gray track. Width is fixed 16px to match Win9x default."
---

## 概览

Retro Windows 是一套渲染成幻灯片模板的 **Windows 95 / 98 桌面操作系统审美**。每一页都结构化成一个 `win-window` ——带斜切 chrome 的矩形，海军渐变标题栏，右上三个按钮图标（`_`、`[]`、`X`），以及装着应用式内容的主体区域。构图是「这一页是跑在 1995 年桌面上的软件，内容就是软件显示的东西」。伪装是彻底的：没有现代演示意义上的幻灯片标题，只有做成文件名样式的窗口标题（`README.DOC`、`DATAVIEW.CSV`、`METRICS.LOG`）。

字体栈是 **MS Sans Serif**（及其现代回退 Segoe UI / Tahoma / Verdana）作为几乎全部内容的系统字体，**Press Start 2P**（8-bit 像素展示脸）和 **VT323**（块状 CRT 终端等宽）留给怀旧标点——闪屏标题、导航提示、跑马灯文字。正文字号按现代标准偏小（默认 16px，多数干活文字 14px），这是 OS-UI 审美的一部分：那个时代的软件 UI 跑在固定像素字号上，片子继承了这个约束。

色板是**原版 Win9x 系统色集**：按钮面灰色（`{colors.bg-light}` #d4d0c8）、高光白、阴影深灰，以及留给活动标题栏和主数据填色的海军/蓝渐变（`{colors.blue-navy}` → `{colors.blue-bright}`）。第二簇「复古强调」色相——DOS 绿（#008000）、砖红（#800000）、芥末黄（#808000）、青绿（#008080）——是系统的状态色板：绿表示 OK / 成功 / 直播，红表示警告，黄表示「中等」风险，青用于第三档图表数据。图表从这套状态色板加上海军阶梯取色。没有现代高饱和色相。

层次通过**斜切错觉**达成——每个表面要么凸起（左上高光、右下阴影），要么凹陷（反过来）。系统不用模糊投影；两色不对称描边加内嵌 box-shadow 做出斜切错觉。这是根基层次语法：按钮凸起，文本输入凹陷，group-box 凹陷并带着缺口安装的标题，活动按下状态反转斜切。

**密度哲学：高。** Win9x 应用 UI 是密的——每个像素都有用途，group-box 塞满控件，状态栏带着多项读数，对话框构图紧。片子审美依赖那种密度。一页只有一个居中标题和大量空白，读成坏掉或没做完。正确密度是窗口主体塞满叠放的面板、group-box、表格、图表、按钮条和状态页脚——每一页都应感觉像一块应用屏幕，多个区域同时干活。CRT 扫描线叠层强化这一点：只有底下有密内容时，纹理才读得出来。

**关键特征：**
- 每一页都是 `{components.win-window}` ——带海军渐变标题栏和三个系统按钮（`_`、`[]`、`X`）的斜切 chrome。
- 固定 3px 周期的 CRT 扫描线叠层（`{components.crt-overlay}`）以 3% 不透明度坐在全部内容之上。
- 基于斜切的层次：凸起（`{components.panel-raised}`、`{components.btn-retro}`）和凹陷（`{components.panel-sunken}`、`{components.group-box}`）——没有模糊阴影。
- 字体栈是 MS Sans Serif / Segoe UI / Tahoma 回退，Press Start 2P 和 VT323 当怀旧强调。
- 状态色（绿 / 红 / 黄 / 青）带着语义：绿 = OK，红 = 警告，黄 = 中等，青 = 第三档数据。
- 海军 `{colors.blue-navy}` 是主数据色——进度条、图表柱、关键标题、活动导航点。
- 列表用海军 `>` chevron 前缀；复选框用字面 `x` 字符；树视图用 `📁` / `📄` emoji 字形。
- 窗口标题文字读成带扩展名的全大写文件名（`AGENDA.TXT`、`METRICS.LOG`、`EXPLORER.EXE`）。

## 颜色

### 色板
- **Button Face Light**（`{colors.bg-light}` — #d4d0c8）：窗口、面板、group box、按钮的基础 chrome 色。Win9x「3D Objects」系统色。略暖的灰。任何非内容区域的默认填色。
- **Background Gray**（`{colors.bg-gray}` — #c0c0c0）：略深的灰。用于表头、滚动条轨道、导航点非活动填色。「Gray Background」系统色。
- **Background Dark**（`{colors.bg-dark}` — #808080）：窗口外桌面填色和非活动标题栏起点的深灰。「Inactive Title Bar」色。
- **White**（`{colors.white}` — #ffffff）：内容填色——用在凹陷面板、文本输入、表格单元格、进度条井、以及标题栏文字色里。白色信号是「这是内容，不是 chrome。」
- **Black**（`{colors.black}` — #000000）：斜切描边里最深的阴影色，也是最强的文字色。凸起斜切右/底边的按钮描边也用它。
- **Text Dark**（`{colors.text-dark}` — #222222）：默认正文字色。比纯黑略软，这样正文字不会跟斜切深阴影抢。
- **Text Gray**（`{colors.text-gray}` — #555555）：闷灰，用于次级文字、图注和状态提示。
- **Navy**（`{colors.blue-navy}` — #000080）：主品牌色——标题栏起点、图表柱、进度填色、标题文字、活动导航点、retro-list chevron 标记。系统的「主」色。
- **Blue Bright**（`{colors.blue-bright}` — #0000a0）：标题栏渐变终点。比海军略亮、略更蓝。用作第二档图表柱变体。
- **Blue Light**（`{colors.blue-light}` — #1084d0）：更浅的蓝，用作第三档图表柱变体。
- **Green Retro**（`{colors.green-retro}` — #008000）：DOS 绿。留给 OK 状态、成功消息、增长百分比、「READY」 / 「LIVE」徽章、「On Track」标签。
- **Red Retro**（`{colors.red-retro}` — #800000）：砖红。留给错误/警告文字和砖红状态家族。
- **Yellow Retro**（`{colors.yellow-retro}` — #808000）：芥末黄。留给「中等」风险标签和警告图表分段。
- **Cyan Retro**（`{colors.cyan-retro}` — #008080）：青绿。留给第三档图表分段和次级状态强调。

### 默认值
- **默认表面背景**：窗口后的桌面区域用 `{colors.bg-dark}`，窗口主体用 `{colors.bg-light}`。
- **默认标题 / 主文字色**：`{colors.blue-navy}`。这套系统里标题是海军，不是黑——那是仪表盘 / 应用标题声线。
- **默认正文字色**：`{colors.text-dark}`（#222222），不是纯黑。
- **默认次级 / 图注文字色**：`{colors.text-gray}`（#555555）。
- **默认图表主色**：`{colors.blue-navy}`。次级柱先用 `{colors.blue-bright}` 和 `{colors.blue-light}`；分类分段图再拉 `{colors.green-retro}`、`{colors.cyan-retro}`、`{colors.yellow-retro}`。
- **默认进度条填色**：`{colors.blue-navy}`（实心，无渐变）。
- **默认状态-OK 色**：`{colors.green-retro}` ——用在 `READY`、`LIVE`、`Approved`、增长百分比，以及任何「事情很好」徽章上。
- **默认状态-警告色**：`{colors.red-retro}` 或 `{colors.yellow-retro}` ——硬错误用红，中等关切用黄。
- **默认标题栏背景**：活动窗口上海军 → blue-bright 水平渐变；片子叠多个窗口时，非活动窗口用灰（`{colors.bg-dark}` → `#a0a0a0`）。
- **海军标题栏内的默认文字色**：`{colors.white}` ——标题栏里始终白压海军。
- **凹陷白面板内的默认文字色**：`{colors.text-dark}` ——内容文字深压白。

强调色板（绿 / 红 / 黄 / 青）有固定语义——不要用绿做随意装饰，不要用红做非警告文字。强调是状态信号，不是油漆。

## 字体

### 字族
系统有三张脸，各自角色分明：

- **MS Sans Serif / Segoe UI / Tahoma / Geneva / Verdana 栈**（系统正文）：几乎全部文字的默认。回退链在任何 OS 上都成立——macOS 落到 Geneva 或 Verdana，Windows 落到 Segoe UI 或 MS Sans Serif，Linux 落到无衬线回退。审美是「1995 年软件 UI 长什么样」，系统字体栈对此至关重要——绝不要换成自定义展示无衬线。
- **Press Start 2P**（像素展示）：8-bit 像素展示脸，省着用。留给闪屏标题、收束页的送别消息，以及任何超大怀旧标题瞬间。始终渲成 `{colors.blue-navy}`，始终居中。每套片子用一两次，不要每页都用。
- **VT323**（CRT 终端等宽）：模仿 CRT 终端的块状等宽脸。留给底边导航提示（`<-- ARROW KEYS to navigate -->`）以及任何「终端输出」正文区域。可选——片子没有它也能转。

不用斜体。不用下划线（交互链接可以下划，但没有装饰性下划）。强调靠字重（400 → 700）和换色（默认 → 海军，或默认 → 绿/红）。

### 字号阶梯

| Token | 字号 | 字族 | 字重 | 用途 |
|---|---|---|---|---|
| `{typography.text-xl}` | 32px | MS Sans Serif | 700 | 窗口主体内的主幻灯片标题 |
| `{typography.metric-xl}` | 30px | MS Sans Serif | 700 | KPI 砖里的 hero 指标值 |
| `{typography.text-lg}` | 22px | MS Sans Serif | 700 | 窗口主体内的区块标题 / 副标题 |
| `{typography.text-md}` | 18px | MS Sans Serif | 400 | 标准正文段落 |
| `{typography.body}` | 16px | MS Sans Serif | 400 | 默认干活正文 |
| `{typography.text-sm}` | 14px | MS Sans Serif | 400 | 图注、列表项、按钮标签、表格单元格 |
| `{typography.text-xs}` | 12px | MS Sans Serif | 400 | 细字、状态提示、页码计数 |
| `{typography.title-bar}` | 14px | MS Sans Serif | 700 | 窗口标题栏文件名——始终全大写 |
| `{typography.group-box-title}` | 13px | MS Sans Serif | 700 | 缺口安装的 group-box 标题标签 |
| `{typography.pixel-display}` | 20–24px | Press Start 2P | 400 | 怀旧闪屏或收束展示标题 |
| `{typography.terminal}` | 22px | VT323 | 400 | 终端风格正文或跑马灯文字 |
| `{typography.nav-hint}` | 16px | VT323 | 400 | 底边键盘提示文字 |

### 默认值
- **窗口主体内主幻灯片标题的默认字号**：`{typography.text-lg}`（22px），`{colors.blue-navy}` 字重 700 ——应用标题声线。超大 hero 标题用 `{typography.text-xl}`（32px）。
- **正文段落的默认字号**：散文段落用 `{typography.text-md}`（18px）；干活文字和列表行用 `{typography.text-sm}`（14px）。
- **窗口标题栏文件名的默认字号**：`{typography.title-bar}`（14px 字重 700），始终全大写，始终 `{colors.white}`。
- **指标或 hero 数字的默认字号**：`{typography.metric-xl}`（30px 字重 700），`{colors.blue-navy}`。
- **窗口内区块标题的默认字号**：`{typography.text-lg}`（22px 字重 700），`{colors.blue-navy}`。
- **任何图注、细字或状态提示的默认字号**：`{typography.text-xs}`（12px），`{colors.text-gray}`。
- **任何应抓住注意力的标题或标签的默认字重**：700。
- **正文的默认字重**：400。

当一页带着多个叠放窗口或面板时，主幻灯片信息放进第一个窗口的主体，用 `{typography.text-lg}`-字重-700-海军。除非是明确的 hero / 闪屏瞬间，不要伸手去拿更大字号。

### 标志性处理
这些处理在**对应元素类型被使用时不可省略**：

- **每个窗口标题栏文字都是全大写，并做成文件名样式**（带扩展名）：`PRESENTATION.EXE`、`README.DOC`、`METRICS.LOG`、`AGENDA.TXT`、`DATAVIEW.CSV`、`FEATURES.INI`、`EXPLORER.EXE`、`TIMELINE.PRJ`。文件名约定是审美的一部分——绝不要用现代标题大小写的窗口名。
- **每个标题栏都带着三按钮簇**（`_` 最小化、`[]` 最大化、`X` 关闭）在右上。按钮是装饰的，不是交互的，但必须始终在场。
- **每个标题栏左侧都带着 `{components.win-icon}` lockup** ——18px 白底黑边方块，里面一个海军字母，助记识别窗口（P、A、R、D、F、G、M、E、T）。
- **每个窗口都用凸起斜切 chrome 处理**（上/左白 + 下/右黑描边 + 双内嵌阴影）。拿掉斜切会彻底打断 Windows 审美。
- **窗口内每个正文标题都是 `{colors.blue-navy}` 字重 700。** 海军是应用标题声线；黑标题读成「错时代」。
- **状态文字用指定状态色**加字重 700：绿表示 OK/成功/增长，红表示错误，黄表示中等。默认字重的绿色状态词读成顺便出现，而不是标签。
- **Group-box 标题坐在上边框上 0–8px padding 的缺口里。** 标题背景用 `{colors.bg-light}`（父填色）画，遮住后面的描边——绝不要让描边穿过标题。

### 排印原则
审美依赖**固定像素字号**，不是流体字号。系统设计给 Win9x 96-DPI 渲染环境，片子用整数像素字号（12、13、14、16、18、22、30、32）保住那种手感。正文不要用 `rem`/`em`/`clamp` ——亚像素渲染的字号会打断 OS-UI 错觉。

像素字体（Press Start 2P）和终端字体（VT323）是怀旧强调，不是干活的。用 Press Start 2P 跑正文很快就不可读；用 VT323 做标题读成过度制作。每套片子各留给一两个瞬间。

## 版式

### 画布系统
系统目标是 `100vw × 100vh`，每页定位为 `position: fixed; top: 0; left: 0`。只有 `.active` 页是 `display: flex`；其余是 `display: none`。每页内部，单个 `{components.win-window}`（或几个叠放窗口）提供框住 chrome。窗口是 `max-width: 1200px` 和 `max-height: calc(100vh - 68px)`，这样 chrome 周围始终能看见桌面灰边。

幻灯片外边距是 `24px 32px 44px 32px` ——额外底 padding 清开持续导航 chrome（视口底边的导航点和页码计数）。

### 窗口解剖
每个窗口有三个竖直叠放的区域：
1. **标题栏**（`{components.win-titlebar}`）——固定 4px-8px padding，海军渐变，装着左图标-lockup + 文件名和右三按钮簇。
2. **主体**（`{components.win-body}`）——20px 24px 24px 24px padding，填满剩余高度，装着幻灯片的内容构图。
3. **可选状态面板**在主体底部——一条 `{components.panel-raised}` 或 `{components.panel-sunken}` 条，带着元信息（数据源、最后更新、计数、状态徽章）。

一页可以并排放多个窗口（典型用于时间线季度或多屏对比）。多个窗口出现时，只有一个带着活动海军标题栏；其余带着非活动灰渐变。

### 内边距阶梯
| Token | 值 | 用途 |
|---|---|---|
| `{spacing.slide-pad}` | 24px 32px 44px 32px | 幻灯片外边距 |
| `{spacing.win-body-pad}` | 20px 24px 24px 24px | 窗口主体内部 |
| `{spacing.group-box-pad}` | 20px 18px 16px 18px | group-box 内部（顶部额外空间清开缺口标题） |
| `{spacing.panel-pad}` | 16px | 凸起面板内部 |
| `{spacing.panel-sunken-pad}` | 12px | 凹陷白面板内部 |

### 持续页框
三个持续元素活在幻灯片构图之外：
- **导航点**在底部居中——斜切方形指示器，每页一个，活动的填海军并带着 4px 白中心方块。
- **页码计数**在右下——凹陷斜切芯片，`N / TOTAL` 文字 12px。
- **导航提示**在左下——VT323 16px 文字，读成 `<-- ARROW KEYS to navigate -->`。

CRT 扫描线叠层以 z-index 9999 坐在一切之上——每一页、每个 chrome 元素、每张图表画布都渲在它下面。

## 层次与抬升

### 斜切错觉（主手法）
系统用**两色不对称描边**加**内嵌 box-shadow** 来模拟 Windows 95 斜切 UI。有两种状态：

- **凸起**：上 + 左 2px solid 白，右 + 底 2px solid 黑，再加 `inset 1px 1px 0 white, inset -1px -1px 0 #404040`。读成从表面抬起的按钮或面板。用在窗口、凸起面板、按钮、导航点上。
- **凹陷**：上 + 左 2px solid `#404040`，右 + 底 2px solid 白。读成凹进去的输入框或内容井。用在 group-box、凹陷面板、文本输入、进度条轨道、复选框、滚动条轨道上。

活动按钮按下状态反转斜切——「按进去」的按钮交换高光/阴影描边方向。没有悬停状态；OS 审美早于普遍的悬停可供性。

### 没有现代阴影
系统使用**没有模糊 `box-shadow` 值**、没有 `drop-shadow` 滤镜、没有 rgba 阴影着色。每个层次线索都来自斜切描边手法。给窗口或按钮加柔软现代阴影会立刻打断时代。

### 色块层次
斜切之外，**白 vs 灰对比**提供区域层次：白面板在视觉上凸出为「内容 / 数据」，灰面板退成「chrome / 结构」。一页的层级从白井坐在哪里自然长出来。

### CRT 扫描线叠层
系统带着一层大气：CRT 扫描线叠层。3px 周期的水平重复渐变，3% 黑不透明度，盖在每一页上。叠层不加层次，但加**纹理**——片子里每个表面读成「渲在 1995 CRT 显示器上」，而不是「渲在平面屏幕上」。拿掉叠层可以，但会丢掉审美里有意义的一块。

## 形状与处理

### 圆角
系统**任何地方都没有圆角**。每个盒子、按钮、面板、窗口、表格单元格、复选框、导航点、进度条——严格矩形。Border-radius 全系统 `0`。

### 描边粗细与样式
- **2px solid** ——窗口、面板、按钮、导航点上的通用斜切描边粗细。用在做出斜切错觉的两色不对称模式里（白+黑 或 深灰+白）。
- **1px solid** ——更细的元素描边（表格单元格描边、win-icon 轮廓、hr-retro 叠线）。
- **`1px inset`** ——用在跑马灯容器描边上。

描边从不着色（没有海军描边，没有绿描边）；斜切两色模式（白 + 黑/深灰）是唯一的描边词汇。

### 装饰元素类型

**窗口**（`{components.win-window}`）— 框住原语。凸起斜切矩形，海军标题栏装着图标 + 文件名 + 三个系统按钮，以及装着内容的主体区域。每一页至少是一个窗口。

**Group box**（`{components.group-box}`）— 凹陷斜切容器，左上带着缺口安装的标题。标题坐在 0–8px padding、用背景画过的区域里，遮住后面的描边，模仿原生 HTML 表单的 `<fieldset><legend>` 模式。用于在窗口内把相关控件或内容块聚在一起。

**凸起面板**（`{components.panel-raised}`）— 凸起斜切灰面板。用于工具调色板、按钮条、状态页脚和抬升的内容区域。

**凹陷面板**（`{components.panel-sunken}`）— 凹陷斜切白面板。用于文本输入、KPI 显示、状态读数和只读数据。白内部是线索。

**复古按钮**（`{components.btn-retro}`）— 凸起斜切灰按钮，6px × 24px padding。始终带着 text-md（14px）MS Sans Serif 字重 400。活动状态反转斜切。

**进度条**（`{components.progress-bar}`）— 凹陷白井，里面一个实心海军填色 div。填色宽度代表数值；除宽度过渡外没有动画。始终 24px 高（嵌在功能卡片里时 16px）。

**复古表格**（`{components.retro-table}`）— 像素平的数据表，灰表头、白单元格、浅灰格线，交替行上几乎看不出差别的斑马填色。单元格 padding 是 6px × 10px。

**复古列表**（`{components.retro-list}`）— 无样式列表，每行海军 `>` chevron 前缀。Chevron 通过 `::before` 设置，从不走 list-style。

**复古复选**（`{components.retro-check}`）— 16px 凹陷斜切白方块，勾选时装着字面小写 `x` 字符。斜切相对按钮是反的（上/左黑，下/右白）。

**树视图**（`{components.tree-item}`）— 资源管理器风格层级列表。每行带着展开标记（+/−）、文件夹（`📁`）或文件（`📄`）emoji 字形，以及标签。每层缩进 24px。

**KPI 砖（group-box 变体）** — 方形 group-box，带着标题标签（`Revenue`、`Customers`、`Retention`、`NPS Score`）、一个大 30px 海军指标、一条绿 delta 线（`▲ +18.3%`），以及一条 12px 灰上下文线（`vs previous quarter`）。用于仪表盘的 4-up 行。

**跑马灯**（`{components.marquee}`）— 凹陷白井，装着水平滚动文字。动画跑 14s linear infinite；没有实现悬停暂停。用在闪屏和收束页。

**Win icon**（`{components.win-icon}`）— 18px 方形白底黑边微型，单个海军字母字形。用在标题栏当 lockup 记号。

**分隔符**（竖直或 hr-retro）— 斜切线。竖直：2px 深灰 + 1px 白左边框，12px 水平外边距。水平：叠 1px 上深灰 + 1px 下白线，14px 竖直外边距。

**沙漏 / 睡眠字形**（`⌛` 或 `💤`）— 用作闪屏 / 收束页上单个超大字符（40–52px），当怀旧 OS 感线索。

## 该做与不该做

### 该做
- 每一页都包进 `{components.win-window}`，海军标题栏带着文件名式标题（例如 `METRICS.LOG`）和三按钮簇（`_`、`[]`、`X`）。
- 每个面板、按钮和窗口都用斜切描边手法（上/左白 + 下/右黑 + 凸起用内嵌阴影；凹陷反过来）。这是系统的身份。
- 主标题设成 `{colors.blue-navy}` 字重 700。海军是应用标题声线——黑标题读成错时代。
- 把每一页装密。多个 group box、叠放面板、KPI 条、图表和状态页脚都应在一个窗口主体里共存。空白读成坏掉。
- 语义地用状态色：绿表示 OK / 直播 / 增长，红表示警告 / 错误，黄表示中等关切，青表示第三档数据。每种颜色带着含义——不要拿它们重新装饰。
- 图表先用海军阶梯渲染（`{colors.blue-navy}`、`{colors.blue-bright}`、`{colors.blue-light}`），再从状态色板拉分类分段分化。
- 项目符号列表用 `>` chevron retro-list 模式，复选框用字面-`x` retro-check。原生浏览器项目符号和表单控件会打断审美。
- 施加整数像素字号（12、13、14、16、18、22、30、32）。固定像素尺寸是 OS-UI 错觉的一部分。
- 每一页都保留 CRT 扫描线叠层（`{components.crt-overlay}`）。它是把片子绑到 CRT 显示器隐喻上的纹理。
- 窗口标题做成带扩展名的全大写文件名（`PRESENTATION.EXE`、`AGENDA.TXT`）。标题大小写的窗口名会打断伪装。

### 不该做
- 不要圆任何角。每个形状都是严格矩形。除图表画布里微小的圆细节外，border-radius 全系统 0。
- 不要用模糊 `box-shadow` 或 `drop-shadow`。所有层次都基于斜切。
- 不要引入现代品牌色（饱和紫、橙、品红）。色板限于 Win9x 系统灰、海军，以及四种复古强调。
- 不要在描边上用颜色。描边两色是白 + 黑或深灰 + 白——绝不要海军描边，绝不要绿描边。
- 不要用 `rem`/`em`/`clamp` 做正文字号。固定整数像素尺寸保住 OS-UI 错觉。
- 不要用 Press Start 2P 或 VT323 跑正文。它们是怀旧强调——每套片子留给一两个瞬间。
- 不要用现代标题大小写或句首大写窗口标题。窗口标题是带扩展名的全大写文件名。
- 不要让窗口没有三按钮簇（`_`、`[]`、`X`）。即便是装饰，簇也是每个窗口签名的一部分。
- 不要给按钮引入悬停状态视觉变化。Win9x 时代早于普遍悬停；活动状态斜切反转是唯一的状态变化。
- 不要构图稀疏页：一个居中标题加大量空白。系统感觉不像密的应用 UI 时，读成坏掉。

## 响应式行为

系统是**视口流体**但**固定像素**：窗口 chrome 和主体尺寸随视口伸缩（`max-width: 1200px`，`max-height: calc(100vh - 68px)`），但字号是整数像素，不是 clamp。唯一一条媒体查询在 `max-width: 900px`：幻灯片 padding 减到 15px-20px，4 列网格收成 2 列。

### 缩放行为
- 窗口增长填满视口直到 1200×(100vh-68px)，然后停止缩放。
- 所有字号保持固定：14px 标签在任何屏幕尺寸上都是 14px。
- CRT 扫描线叠层的 3px 周期不论视口都恒定。

### 演示行为
- 前进：`ArrowRight`、`ArrowDown` 或 `Space`。
- 后退：`ArrowLeft` 或 `ArrowUp`。
- `Home` 跳到第一页，`End` 跳到最后一页。
- 底部导航点可点。
- 默认没有实现触控滑动支持。

### 打印行为
没有定义 `@media print` 规则。打印只会渲出活动页。

### 图表渲染
图表用从 CDN 加载的 Chart.js。图表颜色直接映射到系统 token（`{colors.blue-navy}`、`{colors.blue-bright}`、`{colors.blue-light}`、`{colors.green-retro}`、`{colors.cyan-retro}`、`{colors.yellow-retro}`）。坐标轴标签用 MS Sans Serif 11–12px，`{colors.text-dark}`。网格线是 1px `{colors.bg-gray}`。图表在对应页变为活动时惰性渲染。

## 中日韩与国际内容

### 推荐中文搭配

| 角色 | 拉丁 | 中文 | 字重映射 |
|---|---|---|---|
| 标题栏 / 标题 / 指标 / 区块标题 | MS Sans Serif → Segoe UI (700) | **思源黑体 Noto Sans SC** | 700 |
| 正文 / 图注 / 列表 / 表格单元格 | MS Sans Serif → Segoe UI (400) | **思源黑体 Noto Sans SC** | 400 |
| 像素展示（Press Start 2P）——仅拉丁 | Press Start 2P | *（无 CJK 替代）* | n/a |
| 终端 / 导航提示（VT323）——仅拉丁 | VT323 | *（无 CJK 替代）* | n/a |

### 混排策略

**策略 A ——所有拉丁系统角色共用单一 CJK 字族。** Retro Windows 是系统字体片子（MS Sans Serif / Segoe UI / Tahoma）。把每个拉丁角色配对到单一 CJK 字族——Noto Sans SC——保住「这是软件 UI」档：Win9x 应用会用单一系统 CJK 脸（MS YaHei / SimSun）渲简体中文本地化，而不是多字族展示 + 正文配对。两款怀旧强调字体（Press Start 2P、VT323）按设计是仅拉丁；绝不要尝试像素字体 CJK 替代——没有可接受的对等能保住时代。

### 加载

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap" rel="stylesheet">
```

然后把 `'Noto Sans SC'` 接到正文字体栈：
```css
font-family: 'MS Sans Serif', 'Segoe UI', Tahoma, Geneva, Verdana, 'Noto Sans SC', sans-serif;
```

### 通用中日韩调整

- 行高：正文 1.75–1.85，展示 1.15–1.25
- 字距：CJK 上为 0
- 文字变换：CJK 上不要全大写
- 全角标点
- 展示标题不加句号
- 盘古之白：`使用 Claude` 而不是 `使用Claude`
- 一句一字体

### 本系统的审美说明

- **窗口标题栏变成翻译谜题。** `FILENAME.EXT` 约定是仅拉丁——`METRICS.LOG` 没有地道中文对等。选项：(1) 文件名保持拉丁（`METRICS.LOG`、`AGENDA.TXT`）以求系统 UI 怀旧，让幻灯片主体承载中文内容；(2) 用中文描述符 + 拉丁扩展名（`季度指标.LOG`、`议程.TXT`），读成本地化应用。选项 (1) 对 Win9x 时代更真；(2) 对中文观众更可读。
- **`title-bar` 排印上的 0.5px 字距在标题栏含 CJK 字符时必须降到 0。**
- **状态徽章（READY、LIVE、OK、WARNING）干净地译成短 CJK 词**（就绪、在线、通过、警告），字重 700，指定状态色——语义绿/红/黄/青信号会穿过。
- **Group-box 缺口标题在中文里同样成立** —— `客户数据`、`销售指标`。缺口遮罩依赖背景绘制，不依赖字形度量。
- **CRT 扫描线叠层与字形无关**，给中文排印加上与拉丁相同的怀旧纹理。
- **图表坐标轴标签和芯片文字**应落到 Noto Sans SC 400、11–12px；固定像素尺寸约定同等适用于 CJK。

### 已知中日韩缺口

两款怀旧强调字体（Press Start 2P、VT323）根本上是仅拉丁——它们作为 8-bit 像素和 CRT 终端回调用那个时代，当时 CJK 渲染需要专门的点阵字体，现代网页没有对等。如果片子需要中文像素展示瞬间，唯一诚实的选项是大字号用 Noto Sans SC，放下像素字体性格；不要换成另一款「像素风」中文字体（会读成错时代和坏掉）。把 Press Start 2P / VT323 留给仅拉丁瞬间（闪屏上的 `LOADING...`，页脚上的 `ARROW KEYS to navigate`），让 CJK 页全程用 Noto Sans SC。

## 迭代指南

1. 任何新页都包进 `{components.win-window}`，海军标题栏装着 `{components.win-icon}`（单字母字形）、全大写文件名式标题（扩展名如 `.EXE`、`.DOC`、`.LOG`、`.TXT`、`.CSV`、`.INI`、`.PRJ`、`.BMP`），以及三按钮簇（`_`、`[]`、`X`）。
2. 窗口内任何新内容区域：相关项成簇用 `{components.group-box}`（凹陷加缺口标题），工具条和仪表盘用 `{components.panel-raised}`，白井内容显示用 `{components.panel-sunken}`。
3. 任何新主标题用 `{typography.text-lg}`（22px），`{colors.blue-navy}` 字重 700。Hero / 闪屏标题用 `{typography.text-xl}`（32px）或 Press Start 2P（20–24px）。
4. 任何新指标砖用 `{components.group-box}` + `{typography.metric-xl}` 海军-700 + 绿 delta + 12px 灰上下文模式。
5. 任何新图表用 Chart.js，主数据走海军阶梯，分类分段走复古状态色。始终把画布包进 `{components.panel-raised}`。
6. 任何新项目符号列表用 `{components.retro-list}` chevron 模式；任何复选框用 `{components.retro-check}` 模式；任何层级树用 `{components.tree-item}` 文件夹/文件 emoji 模式。
7. 任何新按钮都是 `{components.btn-retro}` ——斜切灰，6px × 24px padding，14px MS Sans Serif。按钮成簇出现（OK / Cancel / Help，或 Export / Print）。
8. 任何新状态徽章：OK 用 `{colors.green-retro}` 字重 700，错误用 `{colors.red-retro}`，中等用 `{colors.yellow-retro}`。始终字重 700；从不装饰。
9. 状态页脚（窗口主体底部的 panel-raised 条）带着三或四个数据点，用 `•` 项目符号分开——数据源、最后更新、计数、分类。
10. 每一页必须视觉密——多个面板叠放，底部状态页脚，空间允许时还有按钮条或导航簇装饰。稀疏会打断审美。

## 已知缺口

- 系统从 CDN 加载两款 Google Fonts（Press Start 2P、VT323）。它们是可选怀旧强调；正文字体栈（MS Sans Serif、Segoe UI、Tahoma、Geneva、Verdana、sans-serif）没有任何外部依赖也能正确渲染，两款 Google 字体都加载失败时片子在审美上仍连贯。
- 从 CDN 加载的 Chart.js（4.4.7）提供图表引擎。Chart.js 加载失败时图表不会渲染。幻灯片仍会渲染，但画布区域是空的。
- CRT 扫描线叠层是风格选择，跟演示投影仪输出不太匹配——在实际投影屏幕上，叠层可能读成图像噪点而不是怀旧纹理。投影时考虑关掉叠层。
- Win9x 斜切错觉依赖正确缩放级别渲染——斜切宽 1–2px，在极端缩放或很高 DPI、浏览器没有亚像素渲染的显示器上，可能看起来像实心描边或完全消失。
- 悬停状态按设计缺席（审美早于普遍悬停）。期待悬停可供性的现代观众，可能觉得片子在鼠标交互上反应迟钝。
- retro-list 的 `>` chevron、retro-check 的 `x`，以及树视图 emoji 字形是基于字符的，不是矢量——它们会用运行时为 `>`、`x`、`📁`、`📄` 提供的默认字体度量渲染。
- 跑马灯动画持续跑，无法暂停。有些无障碍审计会把它标成 `prefers-reduced-motion` 违规。
- `lib-cabinets` 设在 CSS 里由 `bgImage` 派生的内联 SVG 噪点 / 影线图案——这些是内联 data URI，渲染外观会在浏览器之间略有差异。
