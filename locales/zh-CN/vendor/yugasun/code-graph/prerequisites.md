# graphify 前置条件

必须安装 graphify，才能以确定性方式提取代码图谱。它是一个使用 Tree-sitter 解析 20 多种语言的 Python 工具，无需依靠手工 grep 猜测。

**如果用户尚未安装 graphify**，请按以下优先顺序提供选项：

```bash
# 选项 1：uv（推荐——环境隔离，不会产生冲突）
# 如果尚未安装 uv，先执行：curl -LsSf https://astral.sh/uv/install.sh | sh
uv tool install graphifyy

# 选项 2：pipx（同样隔离）
pipx install graphifyy

# 选项 3：pip（最简单，但可能与其他软件包冲突）
pip install graphifyy
```

安装后运行 `graphify --version` 验证。如果通过 uv 安装后找不到命令，建议执行 `uv tool update-shell`。

PyPI 软件包名为 `graphifyy`（两个 y），CLI 命令则是 `graphify`。

**如果用户拒绝安装**，请告知：“代码图谱功能跳过，其他 skill 正常使用。”随后在没有图谱的情况下继续。不要阻断流程或报错。
