---
name: git-guardrails-claude-code
description: 设置 Claude Code hook，在危险 Git 命令（push、reset --hard、clean、branch -D 等）执行前阻止它们。当用户希望防止破坏性 Git 操作、添加 Git 安全 hook，或在 Claude Code 中阻止 git push/reset 时使用。
---

# 设置 Git 防护栏

设置一个 PreToolUse hook，在 Claude 执行危险 Git 命令前拦截并阻止它们。

## 会阻止什么

- `git push`（所有变体，包括 `--force`）
- `git reset --hard`
- `git clean -f` / `git clean -fd`
- `git branch -D`
- `git checkout .` / `git restore .`

命令被阻止时，Claude 会看到一条消息，说明它无权使用这些命令。

## 步骤

### 1. 询问作用域

询问用户：只为**当前项目**（`.claude/settings.json`）安装，还是为**所有项目**（`~/.claude/settings.json`）安装？

### 2. 复制 hook 脚本

内置脚本位于：[scripts/block-dangerous-git.sh](scripts/block-dangerous-git.sh)

根据作用域将其复制到目标位置：

- **项目**：`.claude/hooks/block-dangerous-git.sh`
- **全局**：`~/.claude/hooks/block-dangerous-git.sh`

使用 `chmod +x` 让它可执行。

### 3. 将 hook 添加到设置

添加到相应的设置文件：

**项目**（`.claude/settings.json`）：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

**全局**（`~/.claude/settings.json`）：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

如果设置文件已存在，将 hook 合并进已有的 `hooks.PreToolUse` 数组——不要覆盖其他设置。

### 4. 询问是否定制

询问用户是否希望在阻止列表中添加或删除任何模式。相应编辑复制后的脚本。

### 5. 验证

运行快速测试：

```bash
echo '{"tool_input":{"command":"git push origin main"}}' | <path-to-script>
```

应该以代码 2 退出，并将 BLOCKED 消息打印到 stderr。
