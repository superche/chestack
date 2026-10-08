# CheStack 架构

CheStack 的用户入口只有原子能力与工具组合两类。原子能力提供明确的工作产出，工具组合负责围绕目标选择和组织能力。原则、参考指南和宿主适配是共享实现，按需读取。

| 层 | 内容 | 职责 |
|---|---|---|
| 分发 | [plugin.json](../plugin.json)、[marketplace](../.agents/plugins/marketplace.json) | 插件身份、展示信息与安装来源 |
| 入口 | [skills](../skills) | 原子能力与工具组合入口，4 个支持隐式调用 |
| 路由 | [routes.md](../skills/chestack/references/routes.md) | 将目标匹配到独立能力或工作流 |
| 原则 | [principles.md](../skills/chestack/references/principles.md) | 24 条按需读取的决策约束 |
| 宿主 | [hosts.md](../skills/chestack/references/hosts.md) | 能力发现、模型继承、权限和缺失能力处理 |
| 工具 | [chestack.py](../skills/chestack/scripts/chestack.py) | 环境检查、计划结构校验、日志和 PR 快照 |

## 架构总览

[![CheStack 架构：原子能力、工具组合、共享实现与宿主能力](images/chestack-architecture.png)](images/chestack-architecture.png)

图中逐项列出 15 个技能入口、24 条原则、23 个工作流，以及共享契约、辅助命令、宿主能力和分发验证设施。图内使用英文标识，点击图片查看原图；下方关系图提供可复制的组合结构。

## 理解与探索的组合关系

```mermaid
flowchart LR
    entry[CheStack 按目标路由] --> how[How：当前机制]
    entry --> why[Why：历史理由]
    entry --> teach[Teach：帮助理解]
    entry --> recall[Recall：恢复上下文]
    entry --> explore[Explore：方案探索]
    teach --> how
    teach --> why
    recall --> history[授权历史与实时核对]
    recall --> why
    explore --> how
    explore --> why
    explore --> prototype[按需实验与取证]
```

箭头表示按任务需要读取和复用，不表示固定执行顺序或强制启动子代理。how、why 可以独立使用；teach 按读者需要组合两者；recall 只在主题需要时调查共享记录；explore 在关键未知点消除后交付方案、实验或 demo。已明确的实现请求走 feature，不经探索入口降级成交付 demo。

五个入口共用[需求与验收契约](../skills/chestack/references/requirements/contract.md)，只在任务复杂度需要时展开。理解类产物保留目标、来源和不确定性，组合复用时不能把推断升级成事实。探索产物说明已运行路径和生产验证缺口。

## 技能发现与按需加载

`agents/openai.yaml` 中的 `policy.allow_implicit_invocation` 控制隐式选择。setup、deslop、control-cli、control-ui 设置为 `true`；主入口与其他工作流设置为 `false`。开启后由宿主根据技能描述判断相关性，不保证每次匹配。`catalog.json` 的 `implicit_skills` 记录允许自动选择的集合，校验器检查配置是否一致。入口已被选择后，引用文件由明确路径加载；原则本身无需注册为技能。仓库内的相对引用必须随完整技能包一起安装。

## 专用能力

- **Deslop：**检查当前变更新增的复杂性，用周边代码和实际契约判断可删除内容，并验证行为保持。
- **Control CLI：**绑定真实进程或 PTY，按提示状态逐步输入，检查输出与退出状态，清理自建会话。
- **Control UI：**绑定正确应用和页面，基于新鲜快照定位目标，逐步验证交互，保留匹配状态的视觉证据。
- **Create Skill：**使用宿主可用的技能创建指导，或直接按包契约生成和校验文件；不依赖特定内置命令。
- **Babysit：**提供 check、threads-only 和 drive 模式；读取当前 PR 状态并处理授权范围内的阻塞；合并使用独立的 shipping 工作流。

## 状态与结果

代码执行依赖当前工具能力，不由 Markdown 自行提供。没有终端时可交付补丁但不能声称已执行；没有界面控制时保留 UI 验收缺口；没有调度工具时不能承诺未来运行。

`pr-status` 提供只读观察。完整就绪判断还需核对评审线程、保护规则、依赖和当前 head。决策记录用于长任务恢复，不会自动创建调度或启动代理。

结果报告说明已完成的行为、支持结论的证据和未覆盖边界。实施历史与一次性操作流水不属于产品文档。

## 验证技能生命周期

`chestack-verify` 按请求选择执行验证、创建验证技能或维护现有技能。创建流程产出项目内的启动、实例检查、驱动、取证和清理指令，以及按功能与入口组织的 feature map；交付时说明实际跑过的案例及未验证范围。维护流程核对索引、源码和真实行为，分别处理文档漂移、验证工具缺口、产品回归和环境阻塞。产品回归不能通过降低预期结果来消除。

详细契约见 [Create](../skills/chestack-verify/references/create.md)、[Maintain](../skills/chestack-verify/references/maintain.md) 和 [Feature map](../skills/chestack-verify/references/feature-map.md)。[可运行示例](../skills/chestack-verify/references/feature-map-example/README.md) 展示成功与失败路径、持久化回读，以及清理后保留证据。
