# CheStack

面向 **Codex / ChatGPT** 的工程工作流插件。将目标转化为可执行任务，通过实际代码、终端、界面和 GitHub 状态验证结果。默认继承当前会话模型。

## 使用

```text
$chestack 找出这个缺陷的根因，修复并验证实际行为。
$chestack-deslop 清理这个分支新增的冗余代码，保持行为不变。
$chestack-control-cli 验证交互式命令的输入、取消和退出行为。
$chestack-control-ui 验证这个页面的提交、错误提示和恢复流程。
$chestack-create-skill 把这套操作整理成可复用技能。
$chestack-babysit 处理这个 PR 的评审和 CI 阻塞，直到可以合并。
```

在 Codex 中显式选择 `$技能名`；在支持插件的 ChatGPT 环境中，通过技能选择器选择对应入口。

| 入口 | 结果 |
|---|---|
| `chestack` | 根据目标执行调查、规划、实现、调试、重构与交付工作流 |
| `chestack-setup` | 环境能力说明及可用工作流配置 |
| `chestack-explain` | 有来源的行为、架构与设计动机解释 |
| `chestack-review` | 可定位、可验证的缺陷与影响范围评审 |
| `chestack-verify` | 真实行为证据及可重复的验证方法 |
| `chestack-reflect` | 将重复问题转化为结构约束或可验证规则 |
| `chestack-deslop` | 保持行为的代码精简与风格统一 |
| `chestack-control-cli` | CLI/TUI 交互、输出、退出和性能验证 |
| `chestack-control-ui` | 浏览器、桌面及 Electron 的交互与视觉验证 |
| `chestack-create-skill` | 可安装、可调用、引用完整的技能包 |
| `chestack-babysit` | 当前 PR 的阻塞处理和合并就绪状态 |

所有入口默认显式调用。主入口按需读取 24 条原则和 23 类工作流。可以通过 `$chestack 应用 prove-it-works，展示实际结果` 点名规则。

## 安装

需要当前 GitHub 身份有权访问私有仓库。

```sh
codex plugin marketplace add superche/chestack --ref main
codex plugin add chestack@superche-chestack
```

桌面端也可从已添加的 marketplace 安装。安装后新开会话或刷新技能列表。

支持本地技能发现的环境可以复制完整技能包：

```sh
gh repo clone superche/chestack
cd chestack
python3 scripts/install_skills.py --dest /absolute/path/to/project/.agents/skills
```

个人安装可指定 `~/.agents/skills`。安装器保留已有同名目录，遇到冲突时整体停止。插件安装与本地复制二选一，避免重复入口。

## 执行与能力边界

- 默认模型、终端、浏览器、连接器、子代理和调度来自当前宿主；缺少能力时明确标注未执行部分。
- CLI/TUI 使用可观察的终端会话；UI 使用可用的浏览器、桌面控制或仓库测试工具。
- 创建技能优先使用可用的 `skill-creator`，同时提供独立的文件格式与验证步骤。
- PR 跟进由 CheStack 自己的工作流处理，通过 `gh` 或 GitHub 连接器操作。合并和未来调度需要相应授权。
- 安装不会启动后台服务、监听器或自动化。
- 本地验证、CI、评审、合并、部署和真实用户验收分别报告。

## 开发与检查

Python 3.10+，运行时和测试使用标准库：

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 skills/chestack/scripts/chestack.py doctor
```

辅助工具提供 `doctor`、`plan-check`、`log` 和 `pr-status`。PR 快照不代替完整的合并就绪检查。

参阅 [架构](docs/architecture.md)、[工作流路由](skills/chestack/references/routes.md)、[贡献约定](CONTRIBUTING.md) 和 [许可证](LICENSE)。
