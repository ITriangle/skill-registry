# 可视化 Companion 指南

基于浏览器的可视化 brainstorming 辅助工具，用于展示模型图、示意图和选项。

## 何时使用

按问题判断，而不是按整场会话判断。标准是：**用户通过观看是否会比阅读理解得更好？**

当内容本身具有视觉性时，**使用浏览器**：

- **UI 模型图**——线框图、布局、导航结构、组件设计
- **架构图**——系统组件、数据流、关系图
- **并排视觉比较**——比较两种布局、两套配色或两个设计方向
- **视觉打磨**——问题涉及外观感受、间距或视觉层级
- **空间关系**——以图形呈现的状态机、流程图和实体关系

当内容是文字或表格时，**使用终端**：

- **需求与范围问题**——“X 是什么意思？”“哪些功能在范围内？”
- **概念型 A/B/C 选择**——在文字描述的方案中选择
- **权衡列表**——优缺点、对比表
- **技术决策**——API 设计、数据建模、架构方案选择
- **澄清问题**——答案是文字而非视觉偏好的任何问题

一个问题与 UI 有关，并不自动意味着它是视觉问题。“你想要哪种向导？”属于概念问题，应使用终端。“这些向导布局中哪种感觉更合适？”属于视觉问题，应使用浏览器。

## 工作原理

服务器监视一个目录中的 HTML 文件，并在浏览器中提供最新文件。你把 HTML 内容写入 `screen_dir`，用户会在浏览器中看到并可点击选择。选择会记录到 `state_dir/events`，供你在下一轮读取。

**内容片段与完整文档：** 如果 HTML 文件以 `<!DOCTYPE` 或 `<html` 开头，服务器会原样提供，只注入辅助脚本。否则，服务器会自动用 frame template 包装内容，加入标题栏、CSS 主题、连接状态和全部交互基础设施。**默认编写内容片段。** 只有需要完全控制页面时才写完整文档。

## 启动会话

```bash
# 仅在用户同意使用 companion 后启动。--open 会在第一屏出现时自动打开浏览器；
# --project-dir 会持久化模型图，并允许重启时复用端口。
scripts/start-server.sh --project-dir /path/to/project --open

# 返回：{"type":"server-started","port":52341,
#           "url":"http://localhost:52341/?key=ab12…",
#           "screen_dir":"/path/to/project/.superpowers/brainstorm/12345-1706000000/content",
#           "state_dir":"/path/to/project/.superpowers/brainstorm/12345-1706000000/state"}
```

保存返回结果中的 `screen_dir` 和 `state_dir`。使用 `--open` 后，推送第一屏时浏览器会自行打开，无需再请用户手动打开；但仍应分享 URL 作为备用，因为无界面或远程环境可能无法自动打开。

**URL 包含会话密钥（`?key=…`）。** 服务器会拒绝所有不带密钥的请求，因此必须把 `url` 字段中的**完整** URL 提供给用户。不要删掉查询字符串，也不要只给出 `http://host:port`。该密钥会限制 HTTP 和 WebSocket 访问，防止无关浏览器标签页或网络中的其他设备读取画面或注入事件。首次载入后，浏览器会通过 cookie 记住密钥，因此刷新和访问 `/files/*` 资源时无需重复传递。

**查找连接信息：** 服务器会将启动 JSON 写入 `$STATE_DIR/server-info`。若服务器在后台启动且未捕获标准输出，可读取此文件取得 URL 和端口。使用 `--project-dir` 时，在 `<project>/.superpowers/brainstorm/` 下查找会话目录。

**注意：** 将项目根目录传给 `--project-dir`，让模型图保存在 `.superpowers/brainstorm/` 中并在服务器重启后继续存在。不传时，文件会进入 `/tmp` 并被清理。如果 `.gitignore` 尚未包含 `.superpowers/`，提醒用户添加。

**按平台启动服务器：**

**Claude Code：**

```bash
# 默认模式即可——脚本会自行将服务器放到后台。
scripts/start-server.sh --project-dir /path/to/project --open
```

在 Windows 上，脚本会自动检测并切换到前台模式，从而阻塞工具调用。对 Bash 工具调用设置 `run_in_background: true`，使服务器能跨对话轮次存活；下一轮再读取 `$STATE_DIR/server-info` 获取 URL 和端口。

**Codex：**

```bash
# Codex 会清理后台进程。脚本会自动检测 CODEX_CI 并切换到前台模式。
# 正常运行即可，无需额外参数。
scripts/start-server.sh --project-dir /path/to/project --open
```

**Gemini CLI：**

```bash
# 使用 --foreground，并在 shell 工具调用中设置 is_background: true，
# 使进程能跨轮次存活。
scripts/start-server.sh --project-dir /path/to/project --open --foreground
```

**Copilot CLI：**

```bash
# 使用 --foreground，并通过 mode: "async" 的 bash 工具启动服务器，
# 使进程能跨轮次存活。保存返回的 shellId，供 read_bash / stop_bash 使用。
scripts/start-server.sh --project-dir /path/to/project --open --foreground
```

**其他环境：** 服务器必须在后台持续运行并跨对话轮次存活。如果环境会清理脱离终端的进程，请使用 `--foreground`，并通过该平台的后台执行机制启动命令。

如果浏览器无法访问 URL（远程或容器环境中很常见），请绑定非 loopback 地址：

```bash
scripts/start-server.sh \
  --project-dir /path/to/project \
  --host 0.0.0.0 \
  --url-host localhost
```

用 `--url-host` 控制返回的 URL JSON 中打印哪个主机名。

## 交互循环

1. **确认服务器存活**，然后把 HTML 写到 `screen_dir` 中的新文件：
   - **必须先确认服务器存活，才能引用 URL 或推送画面。** 检查 `$STATE_DIR/server-info` 存在，并且 `$STATE_DIR/server-stopped` 不存在。如果服务器已停止，使用**相同的 `--project-dir`** 通过 `start-server.sh` 重启；它会复用端口，因此用户已打开的标签页会自动重连（服务器离线时显示“已暂停”遮罩），无需发送新 URL。服务器空闲 4 小时后自动退出，可通过 `--idle-timeout-minutes` 配置
   - 使用语义化文件名，如 `platform.html`、`visual-style.html`、`layout.html`
   - **绝不重复使用文件名**——每个画面都用新文件
   - 使用文件创建工具，**不要使用 cat/heredoc**，避免终端输出噪声
   - 服务器会自动提供最新文件

2. **告诉用户将看到什么，然后结束本轮：**
   - 每一步都提醒 URL，而不只是第一次
   - 简短说明画面内容，例如“正在展示首页的三种布局方案”
   - 请用户在终端回应：“请查看并告诉我你的想法；也可以点击选择一个选项。”

3. **下一轮中**——用户在终端回应后：
   - 若 `$STATE_DIR/events` 存在，则读取它，其中包含用户浏览器交互的 JSON 行
   - 将这些事件与用户的终端文字合并，获得完整反馈
   - 终端消息是主要反馈；`state_dir/events` 提供结构化交互数据

4. **迭代或前进**——如果反馈改变了当前画面，写入新文件（如 `layout-v2.html`）。当前步骤验证完成后才能进入下一个问题。

5. **返回终端时卸载画面**——如果下一步不需要浏览器（如澄清问题或权衡讨论），推送等待画面以清除过时内容：

   ```html
   <!-- 文件名：waiting.html（后续可用 waiting-2.html 等） -->
   <div style="display:flex;align-items:center;justify-content:center;min-height:60vh">
     <p class="subtitle">正在终端中继续……</p>
   </div>
   ```

   这样可避免对话已经前进，用户却仍看到已完成选择的旧画面。下一次出现视觉问题时，再正常推送新内容。

6. 重复上述步骤直至完成。

## 编写内容片段

只写页面内部的内容。服务器会自动使用 frame template 包装它，添加标题栏、主题 CSS、连接状态及全部交互设施。

**最小示例：**

```html
<h2>哪种布局更合适？</h2>
<p class="subtitle">请考虑可读性和视觉层级</p>

<div class="options">
  <div class="option" data-choice="a" onclick="toggleSelect(this)">
    <div class="letter">A</div>
    <div class="content">
      <h3>单栏</h3>
      <p>整洁、专注的阅读体验</p>
    </div>
  </div>
  <div class="option" data-choice="b" onclick="toggleSelect(this)">
    <div class="letter">B</div>
    <div class="content">
      <h3>双栏</h3>
      <p>侧边导航加主要内容区</p>
    </div>
  </div>
</div>
```

仅此而已。不需要 `<html>`、CSS 或 `<script>` 标签，服务器会提供这些内容。

## 可用 CSS 类

frame template 为内容提供以下 CSS 类。

### 选项（A/B/C 选择）

```html
<div class="options">
  <div class="option" data-choice="a" onclick="toggleSelect(this)">
    <div class="letter">A</div>
    <div class="content">
      <h3>标题</h3>
      <p>说明</p>
    </div>
  </div>
</div>
```

**多选：** 在容器上添加 `data-multiselect`，允许用户选择多个选项。每次点击都会切换该项目的选中样式。

```html
<div class="options" data-multiselect>
  <!-- 选项标记相同，用户可以选择或取消多个项目 -->
</div>
```

### 卡片（视觉设计）

```html
<div class="cards">
  <div class="card" data-choice="design1" onclick="toggleSelect(this)">
    <div class="card-image"><!-- 模型图内容 --></div>
    <div class="card-body">
      <h3>名称</h3>
      <p>说明</p>
    </div>
  </div>
</div>
```

### 模型图容器

```html
<div class="mockup">
  <div class="mockup-header">预览：仪表盘布局</div>
  <div class="mockup-body"><!-- 模型图 HTML --></div>
</div>
```

### 分栏视图（并排）

```html
<div class="split">
  <div class="mockup"><!-- 左侧 --></div>
  <div class="mockup"><!-- 右侧 --></div>
</div>
```

### 优缺点

```html
<div class="pros-cons">
  <div class="pros"><h4>优点</h4><ul><li>收益</li></ul></div>
  <div class="cons"><h4>缺点</h4><ul><li>不足</li></ul></div>
</div>
```

### 模拟元素（线框图构建块）

```html
<div class="mock-nav">标志 | 首页 | 关于 | 联系</div>
<div style="display: flex;">
  <div class="mock-sidebar">导航</div>
  <div class="mock-content">主要内容区</div>
</div>
<button class="mock-button">操作按钮</button>
<input class="mock-input" placeholder="输入字段">
<div class="placeholder">占位区域</div>
```

### 排版和区块

- `h2`——页面标题
- `h3`——区块标题
- `.subtitle`——标题下方的辅助文字
- `.section`——带底部间距的内容块
- `.label`——小号大写标签文字

## 浏览器事件格式

用户点击浏览器中的选项时，交互会逐行以 JSON 对象记录到 `$STATE_DIR/events`。推送新画面时，该文件会自动清空。

```jsonl
{"type":"click","choice":"a","text":"选项 A - 简单布局","timestamp":1706000101}
{"type":"click","choice":"c","text":"选项 C - 复杂网格","timestamp":1706000108}
{"type":"click","choice":"b","text":"选项 B - 混合布局","timestamp":1706000115}
```

完整事件流会显示用户的探索路径：他们可能在最终决定前点击多个选项。最后一个 `choice` 事件通常是最终选择，但点击模式也可能揭示犹豫或偏好，值得进一步询问。

如果 `$STATE_DIR/events` 不存在，说明用户未与浏览器交互；此时只使用终端文字。

## 设计提示

- **保真度应与问题匹配**——布局问题用线框图，视觉打磨问题才使用精细画面
- **在每页解释问题**——写“哪种布局更显专业？”，而不是只写“选一个”
- **先迭代，再前进**——如果反馈改变当前画面，先生成新版本
- 每屏最多 **2–4 个选项**
- **在有意义时使用真实内容**——例如摄影作品集应使用真实图片（Unsplash）。占位内容会掩盖设计问题
- **保持模型图简单**——聚焦布局和结构，而非像素级完美

## 文件命名

- 使用语义化名称：`platform.html`、`visual-style.html`、`layout.html`
- 不得重复使用文件名，每个画面都必须是新文件
- 迭代时追加版本后缀，如 `layout-v2.html`、`layout-v3.html`
- 服务器按修改时间提供最新文件

## 清理

```bash
scripts/stop-server.sh $SESSION_DIR
```

如果会话使用了 `--project-dir`，模型图文件会保留在 `.superpowers/brainstorm/` 中，供后续参考。只有 `/tmp` 会话会在停止时被删除。

## 参考

- Frame template（CSS 参考）：`scripts/frame-template.html`
- 辅助脚本（客户端）：`scripts/helper.js`
