# Project Memory

- 本项目交流、计划、总结和面向用户的说明优先使用中文；代码、命令、文件名、错误信息和上游原文可保留原语言。
- 注册或添加同名 skill 时，先比较不同来源的差异，给出推荐默认来源；必要时把多个来源合并为一个默认组，同时保留 `--source` 或精确 ID 指定来源的能力。
- 添加或安装 skill 时，需要分析 `SKILL.md` 中显式引用的其他 skill 依赖，并在 `skill-groups.yaml` 的对应 group 中维护 `dependencies` 字段，记录依赖的其他 skill 名称；无依赖时写 `none`。
- 为项目安装或同步 skill 时，需要更新 `projects/<project>.yaml` 记录本地激活清单；这些 `projects/` 下的本地项目配置不执行 `git add`、不提交，保持为本机规则，避免影响 Git 同步。
