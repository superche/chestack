# CheStack

面向 **Codex / ChatGPT** 的原子能力与工具组合。原子能力完成职责明确、可独立检验的工作；工具组合围绕用户目标组织这些能力。CheStack 继承当前会话的模型，通过宿主实际提供的工具工作。

[![CheStack 完整架构：18 个技能入口、23 个工作流、24 条原则与宿主能力](docs/images/chestack-architecture.png)](docs/images/chestack-architecture.png)

英文架构图可点击放大，覆盖全部技能入口、工作流、原则、共享契约、验证生命周期和辅助工具。模块职责与组合关系见[架构说明](docs/architecture.md)。

## 安装

```sh
codex plugin marketplace add superche/chestack --ref main
codex plugin add chestack@superche-chestack
```

也可以在桌面应用添加 marketplace 后安装。安装后新建会话或刷新技能列表。

支持本地技能发现的宿主，可以将完整技能包复制到项目目录：

```sh
gh repo clone superche/chestack
cd chestack
python3 scripts/install_skills.py --dest /absolute/path/to/project/.agents/skills
```

个人安装可以使用 `~/.agents/skills`。安装器遇到同名目录会停止整次安装并保留原有文件；它不会清理或覆盖已有安装。插件安装和本地复制选择一种，避免重复入口。

## 常用使用方式

安装后，在目标项目的会话里输入提示词。用 `$chestack` 描述目标即可按任务路由；已知道要做什么时，可以直接选择专用技能。把示例中的模块、分支、错误和目标替换成实际对象，并附上相关文件或链接。

| 场景 | 可直接复制的提示词 | 主要产出 |
|---|---|---|
| 开发功能 | `$chestack 为任务列表增加状态筛选，保留现有排序；实现后验证筛选、清空和空结果。` | 实现、验收证据与未覆盖范围 |
| 修复问题 | `$chestack 修复保存后重新打开内容丢失的问题，先复现和定位根因，再验证修复与回归。` | 复现条件、根因、修复及回归结果 |
| 梳理代码 | `$chestack-how 追踪这个请求从入口到持久化的过程，解释状态归属和失败路径。` | 机制说明与源码依据 |
| 设计方案 | `$chestack-architect 为批量导出设计调用接口、任务状态和取消机制，给出可实施的设计包。` | 调用示例、接口、所有权、取舍与验收条件 |
| 探索方向 | `$chestack-explore 比较这两个方向，必要时做最小 demo，先不要做生产实现。` | 有依据的方案、实验或 demo，以及生产验证缺口 |
| 审查改动 | `$chestack-review 审查当前分支相对 main 的改动，重点检查状态一致性、失败恢复和测试缺口。` | 有位置、影响和验证方法的发现 |
| 验收功能 | `$chestack-verify 验证这次改动的成功、失败和恢复路径，区分实际执行与尚未验证的部分。` | 真实行为证据与覆盖边界 |
| 操作界面 | `$chestack-control-ui 在当前应用验证新建、保存和重新打开流程，保留对应状态的截图。` | 目标实例、交互结果与视觉证据 |
| 操作终端 | `$chestack-control-cli 验证这个交互式命令的选择、取消、重试和退出行为。` | 真实进程或 PTY 的交互、输出与退出证据 |
| 清理代码 | `$chestack-deslop-code 清理当前改动中多余的抽象和防御逻辑，保持对外行为并验证。` | 精简后的代码与行为保持证据 |
| 改进文档 | `$chestack-deslop-document 改写这份文档，明确使用步骤和限制，保留事实与不确定性。` | 清晰、可核对的文档 |
| 恢复上下文 | `$chestack-recall 回顾最近一周这项工作的决定，核对当前状态和下一步。` | 授权历史、实时状态与待办摘要 |
| 检查 PR | `$chestack-babysit check：检查这个 PR 的评审、CI 和未解决阻塞，报告当前 head 的状态。` | 当前快照、阻塞与就绪状态；不会自动合并 |

需要多步工作时，可以在同一条请求中明确范围与验收目标：

```text
$chestack 重构这个模块，保持公开接口和现有行为；先梳理调用方，再分步修改、审查并验证。
$chestack 排查列表首屏变慢的问题；建立可复现基线，定位瓶颈，用相同条件比较修改前后。
$chestack 继续这项未完成的任务，先核对当前分支、已有产物和检查结果，再完成剩余工作。
$chestack-verify 为这个项目创建可复用的验证技能和 feature map，覆盖启动、交互、取证与清理。
$chestack-compare-and-combine 比较这几个候选，综合有价值的部分并验证最终方案。
$chestack-why 当时为什么选这个设计？区分历史记录和你的推断。
$chestack-teach 我准备修改这个模块，帮我理解它的机制和取舍。
```

Codex 使用 `$skill-name`，支持插件和技能的 ChatGPT 环境使用宿主的选择入口。独立选择技能不要求先经过主入口。

## 全部技能入口

| 类型 | 入口 | 产出 |
|---|---|---|
| 原子能力 | `chestack-how` | 当前机制、数据与状态流、责任归属、失败路径和源码依据 |
| 原子能力 | `chestack-why` | 历史动机、约束、取舍、竞争解释和证据缺口 |
| 原子能力 | `chestack-architect` | 调用方契约、类型与状态归属、设计包及实施偏离反馈 |
| 原子能力 | `chestack-compare-and-combine` | 统一评价、基础候选、综合决策及最终产物验证 |
| 原子能力 | `chestack-review` | 有位置、影响和验证方法的可执行审阅发现 |
| 原子能力 | `chestack-verify` | 行为证据，或可运行的项目验证技能与功能地图 |
| 原子能力 | `chestack-deslop-code` | 清理代码复杂性，并保留已验证行为 |
| 原子能力 | `chestack-deslop-document` | 审校或改写文档，保留原意、事实与不确定性 |
| 原子能力 | `chestack-control-cli` | 真实 CLI/TUI 操作、输出、退出与相关性能证据 |
| 原子能力 | `chestack-control-ui` | 真实浏览器、桌面或 Electron 交互及视觉证据 |
| 原子能力 | `chestack-create-skill` | 引用完整、元数据有效的技能包 |
| 原子能力 | `chestack-setup` | 宿主能力检查和工作流配置 |
| 工具组合 | `chestack` | 按目标选择能力或具体工作流 |
| 工具组合 | `chestack-teach` | 基于 how、why 的分层讲解与具体例子 |
| 工具组合 | `chestack-recall` | 授权历史与实时状态核对后的工作摘要和下一步 |
| 工具组合 | `chestack-explore` | 有依据的方案、实验或 demo，以及生产验证缺口 |
| 工具组合 | `chestack-reflect` | 根据实际纠错形成可验证的结构或流程改进 |
| 工具组合 | `chestack-babysit` | 处理授权范围内的 PR 阻塞并核对当前就绪状态 |

setup、deslop、control-cli、control-ui 支持宿主按描述隐式选择，也可以显式调用。其余入口保持显式选择；已启动的组合可以按路径读取依赖的技能文件，不要求宿主支持嵌套技能调用。

原子能力可以包含多个内部步骤。两类入口以产出职责区分；宿主契约、原则和参考文件是共享实现，不是额外的用户入口。详见[架构](docs/architecture.md)和[路由](skills/chestack/references/routes.md)。

## 结果与边界

- how、why、teach、recall 默认只读。历史来源必须在授权范围内；不可访问的记录会保留为缺口。
- explore 先解决方向问题。资料足够时只交付方案，需要实验时才构建隔离的最小产物；demo 不等于生产实现。
- 终端、浏览器、连接器、代理和调度由当前宿主提供。缺少能力时明确说明未执行或未验证部分，不使用固定模型或替代宿主假设。
- 多代理只在宿主支持且已获授权时使用。顺序审查不会被报告为独立审阅。
- 合并、部署、外发消息和后续调度遵循用户授权。安装不会启动后台服务或自动任务。
- 源码分析、本地执行、CI、合并、部署与真实环境验收分别报告。

## 开发与验证

工具与测试需要 Python 3.10+，只使用标准库：

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 skills/chestack/scripts/chestack.py doctor
```

内置命令为 `doctor`、`plan-check`、`log` 和 `pr-status`。结构校验不会判断计划语义，PR 快照不会认证合并就绪。[工作流验收案例](tests/workflows/understanding.md)用于检查五个能力的实际产出；包测试不等于代理行为评测。

参见[贡献约定](CONTRIBUTING.md)、[许可证](LICENSE)和[第三方声明](NOTICE.md)。
