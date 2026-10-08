# 架构与适配决策

Chestack 把工作流内容和宿主工具分开。核心只要求知道目标、选择步骤、读取规则和验证结果，不依赖特定产品的后台代理、模型 ID、命令或全局配置。

## 分层

| 层 | 文件 | 职责 |
|---|---|---|
| 分发 | [plugin.json](../plugin.json)、[marketplace](../.agents/plugins/marketplace.json) | OpenAI 插件声明、私有 GitHub marketplace |
| 入口 | [skills](../skills) | 6 个显式调用技能及 `agents/openai.yaml` |
| 路由 | [routes.md](../skills/chestack/references/routes.md) | 23 类任务与 playbook 对应 |
| 决策 | [principles.md](../skills/chestack/references/principles.md) | 24 条规则的触发索引和正文 |
| 宿主 | [hosts.md](../skills/chestack/references/hosts.md) | 工具发现、模型继承、缺失能力处理、权限边界 |
| 过程 | [references](../skills/chestack/references) | 设计、解释、评审、验证、学习和交付指南 |
| 工具 | [chestack.py](../skills/chestack/scripts/chestack.py) | 有界、可复查的辅助操作 |
| 维护 | [validate.py](../scripts/validate.py)、[tests](../tests) | 清单、链接、可移植性和失败行为检查 |

## 加载模型

安装包提供 6 个 `SKILL.md`。`policy.allow_implicit_invocation: false` 放在 OpenAI 的 `agents/openai.yaml` 中。主入口被调用后，通过索引读取普通参考文件。这避免把大量原则注册成用户命令，也避免把“禁止隐式调用”误当成“禁止读取文件”。

主入口不保证永久留在对话上下文。需要跨任务持久行为时，使用用户授权的仓库 `AGENTS.md` 指针，不模拟其他产品的 Custom Mode。

## 能力降级

有终端时执行脚本；只有内容访问时产出有来源的解释、评审或方案。没有真实浏览器时不声称 UI 验收；没有子代理时使用顺序检查，不声称独立评审；没有调度工具时只保留 checkpoint，不声称未来会执行。

权限是宿主与用户会话提供的约束。技能和第三方资料不能自行扩展权限。遇到访问失败，先排查沙盒和网络，再判断是否需要人工处理账户。

## 与 pstack 的取舍

保留原则、按任务路由、结构优先、真实验证、短反馈循环和可复查决策。将 51 个上游技能合并为 6 个入口及按需指南，保留逐项 [迁移对应表](pstack-mapping.md)。

不携带上游默认模型、命名代理注册、专用控制插件、自动常驻权限或外部消息发送惯例。两个上游代理的意图分别落入协作契约和评审指南。

确定性工具采用 Python 标准库。当前 `pr-status` 是一次快照，不是上游 watcher 的等价实现。长期协调采用任务内记录和可选原生调度，没有把文字 playbook 描述为独立自治系统。

## 依据

- pstack snapshot: `ccb5507cec1546dc88135c1139c811e6c59115ba`，版本 `0.15.15`。
- [OpenAI Build plugins](https://developers.openai.com/plugins/build/plugins)：根目录插件声明、marketplace 和 OpenAI 元数据。
- [OpenAI Build skills](https://developers.openai.com/plugins/build/skills)：技能格式、发现路径和调用策略。
- 本地 CLI `codex 0.142.5` 的 `plugin` 命令帮助：实际安装命令形态。

文档核对日期：2026-10-08。当前客户端可用工具优先于对其他客户端的假设。
