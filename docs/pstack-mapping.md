# pstack 模块对应表

来源为固定 snapshot `ccb5507cec1546dc88135c1139c811e6c59115ba`。逐项覆盖上游 51 个主技能；“对应”表示意图和责任归属，不表示所有运行时功能等价。初版有意合并入口，并明确未实现的服务。

## 主技能（51）

| 上游 | Chestack 目标 | 状态 |
|---|---|---|
| `architect` | [references/design.md](../skills/chestack/references/design.md) | 结构候选与设计验证 |
| `arena` | [references/design.md](../skills/chestack/references/design.md) | 候选比较与验证后组合 |
| `automate-me` | [references/learning.md](../skills/chestack/references/learning.md) | 授权个人偏好技能 |
| `benchmark-checklist` | [references/measurement.md](../skills/chestack/references/measurement.md) | 七项测量证据 |
| `blast-radius` | [references/review.md](../skills/chestack/references/review.md) | 超出 diff 的调用影响 |
| `bro` | [references/explain.md](../skills/chestack/references/explain.md) | 普通语言重述 |
| `correct` | [references/learning.md](../skills/chestack/references/learning.md) | 结构化纠错 |
| `create-verification-skill` | [references/verification.md](../skills/chestack/references/verification.md) | 项目验证方法生成 |
| `figure-it-out` | [SKILL.md](../skills/chestack/SKILL.md) | 无匹配路线时构造有界工作流 |
| `how` | [references/explain.md](../skills/chestack/references/explain.md) | 结构与运行时解释 |
| `interrogate` | [references/review.md](../skills/chestack/references/review.md) | 对抗性评审；独立性如实标注 |
| `maintain-verification-skill` | [references/verification.md](../skills/chestack/references/verification.md) | 验证路径维护 |
| `make-bot-ui` | [references/issue-automation.md](../skills/chestack/references/issue-automation.md) | 设计指南；未实现 webhook 服务 |
| `no-comments` | [references/review.md](../skills/chestack/references/review.md) | 注释与结构评审 |
| `poteto-help` | [../../chestack-setup/SKILL.md](../skills/chestack-setup/SKILL.md) | 合并到环境与使用入口 |
| `poteto-mode` | [SKILL.md](../skills/chestack/SKILL.md) | 主入口重写 |
| `principle-attack-the-premise` | [references/principles/attack-the-premise.md](../skills/chestack/references/principles/attack-the-premise.md) | 保留名称，改写宿主无关规则 |
| `principle-boundary-discipline` | [references/principles/boundary-discipline.md](../skills/chestack/references/principles/boundary-discipline.md) | 保留名称，改写宿主无关规则 |
| `principle-build-the-lever` | [references/principles/build-the-lever.md](../skills/chestack/references/principles/build-the-lever.md) | 保留名称，改写宿主无关规则 |
| `principle-encode-lessons-in-structure` | [references/principles/encode-lessons-in-structure.md](../skills/chestack/references/principles/encode-lessons-in-structure.md) | 保留名称，改写宿主无关规则 |
| `principle-exhaust-the-design-space` | [references/principles/exhaust-the-design-space.md](../skills/chestack/references/principles/exhaust-the-design-space.md) | 保留名称，改写宿主无关规则 |
| `principle-experience-first` | [references/principles/experience-first.md](../skills/chestack/references/principles/experience-first.md) | 保留名称，改写宿主无关规则 |
| `principle-explain-the-number` | [references/principles/explain-the-number.md](../skills/chestack/references/principles/explain-the-number.md) | 保留名称，改写宿主无关规则 |
| `principle-fix-root-causes` | [references/principles/fix-root-causes.md](../skills/chestack/references/principles/fix-root-causes.md) | 保留名称，改写宿主无关规则 |
| `principle-foundational-thinking` | [references/principles/foundational-thinking.md](../skills/chestack/references/principles/foundational-thinking.md) | 保留名称，改写宿主无关规则 |
| `principle-guard-the-context-window` | [references/principles/guard-the-context-window.md](../skills/chestack/references/principles/guard-the-context-window.md) | 保留名称，改写宿主无关规则 |
| `principle-laziness-protocol` | [references/principles/laziness-protocol.md](../skills/chestack/references/principles/laziness-protocol.md) | 保留名称，改写宿主无关规则 |
| `principle-make-operations-idempotent` | [references/principles/make-operations-idempotent.md](../skills/chestack/references/principles/make-operations-idempotent.md) | 保留名称，改写宿主无关规则 |
| `principle-migrate-callers-then-delete-legacy-apis` | [references/principles/migrate-callers-then-delete-legacy-apis.md](../skills/chestack/references/principles/migrate-callers-then-delete-legacy-apis.md) | 保留名称，改写宿主无关规则 |
| `principle-minimize-reader-load` | [references/principles/minimize-reader-load.md](../skills/chestack/references/principles/minimize-reader-load.md) | 保留名称，改写宿主无关规则 |
| `principle-model-the-domain` | [references/principles/model-the-domain.md](../skills/chestack/references/principles/model-the-domain.md) | 保留名称，改写宿主无关规则 |
| `principle-never-block-on-the-human` | [references/principles/never-block-on-the-human.md](../skills/chestack/references/principles/never-block-on-the-human.md) | 保留名称，改写宿主无关规则 |
| `principle-outcome-oriented-execution` | [references/principles/outcome-oriented-execution.md](../skills/chestack/references/principles/outcome-oriented-execution.md) | 保留名称，改写宿主无关规则 |
| `principle-prove-it-works` | [references/principles/prove-it-works.md](../skills/chestack/references/principles/prove-it-works.md) | 保留名称，改写宿主无关规则 |
| `principle-redesign-from-first-principles` | [references/principles/redesign-from-first-principles.md](../skills/chestack/references/principles/redesign-from-first-principles.md) | 保留名称，改写宿主无关规则 |
| `principle-separate-before-serializing-shared-state` | [references/principles/separate-before-serializing-shared-state.md](../skills/chestack/references/principles/separate-before-serializing-shared-state.md) | 保留名称，改写宿主无关规则 |
| `principle-sequence-verifiable-units` | [references/principles/sequence-verifiable-units.md](../skills/chestack/references/principles/sequence-verifiable-units.md) | 保留名称，改写宿主无关规则 |
| `principle-subtract-before-you-add` | [references/principles/subtract-before-you-add.md](../skills/chestack/references/principles/subtract-before-you-add.md) | 保留名称，改写宿主无关规则 |
| `principle-test-behavior-not-implementation` | [references/principles/test-behavior-not-implementation.md](../skills/chestack/references/principles/test-behavior-not-implementation.md) | 保留名称，改写宿主无关规则 |
| `principle-type-system-discipline` | [references/principles/type-system-discipline.md](../skills/chestack/references/principles/type-system-discipline.md) | 保留名称，改写宿主无关规则 |
| `recall` | [references/explain.md](../skills/chestack/references/explain.md) | 授权历史与实时状态核对 |
| `reflect` | [references/learning.md](../skills/chestack/references/learning.md) | 证据驱动复盘 |
| `setup-pstack` | [../../chestack-setup/SKILL.md](../skills/chestack-setup/SKILL.md) | 能力探测；继承当前模型 |
| `show-me-your-work` | [references/operations.md](../skills/chestack/references/operations.md) | 决策日志与 checkpoint |
| `swarm` | [references/delegation.md](../skills/chestack/references/delegation.md) | 按能力与授权进行覆盖分工 |
| `tdd` | [references/verification.md](../skills/chestack/references/verification.md) | 明确请求或低成本复现时使用 |
| `teach` | [references/explain.md](../skills/chestack/references/explain.md) | how + why 教学 |
| `technical-writing` | [references/writing.md](../skills/chestack/references/writing.md) | 按读者任务组织文档 |
| `typescript-best-practices` | [references/review.md](../skills/chestack/references/review.md) | 类型边界通用规则；语言细节由项目补充 |
| `unslop` | [references/writing.md](../skills/chestack/references/writing.md) | 去掉无信息写作模式 |
| `why` | [references/explain.md](../skills/chestack/references/explain.md) | 设计动机与来源 |

## Playbooks（23）

所有名称保留为路由标签，步骤重新适配。

- [authoring-a-skill](../skills/chestack/references/playbooks/authoring-a-skill.md)
- [autonomous-run](../skills/chestack/references/playbooks/autonomous-run.md)
- [autopilot-full](../skills/chestack/references/playbooks/autopilot-full.md)
- [autopilot-stack](../skills/chestack/references/playbooks/autopilot-stack.md)
- [babysit](../skills/chestack/references/playbooks/babysit.md)
- [bug-fix](../skills/chestack/references/playbooks/bug-fix.md)
- [eval](../skills/chestack/references/playbooks/eval.md)
- [feature](../skills/chestack/references/playbooks/feature.md)
- [hillclimb](../skills/chestack/references/playbooks/hillclimb.md)
- [investigation](../skills/chestack/references/playbooks/investigation.md)
- [multi-phase-plan](../skills/chestack/references/playbooks/multi-phase-plan.md)
- [opening-a-pr](../skills/chestack/references/playbooks/opening-a-pr.md)
- [orchestrate](../skills/chestack/references/playbooks/orchestrate.md)
- [pause-safely](../skills/chestack/references/playbooks/pause-safely.md)
- [perf-issue](../skills/chestack/references/playbooks/perf-issue.md)
- [prototype](../skills/chestack/references/playbooks/prototype.md)
- [refactoring](../skills/chestack/references/playbooks/refactoring.md)
- [runtime-forensics](../skills/chestack/references/playbooks/runtime-forensics.md)
- [session-pickup](../skills/chestack/references/playbooks/session-pickup.md)
- [shipping](../skills/chestack/references/playbooks/shipping.md)
- [trace-forensics](../skills/chestack/references/playbooks/trace-forensics.md)
- [visual-parity](../skills/chestack/references/playbooks/visual-parity.md)
- [worktree-cleanup](../skills/chestack/references/playbooks/worktree-cleanup.md)

## 代理、工具及自动化

| 上游模块 | Chestack 处理 | 状态 |
|---|---|---|
| poteto-agent | delegation 指南与宿主原生子代理 | 不注册虚构的 named agent |
| comment-sicko | review 指南的 comments lens | 保留可核实约束，去除人格表演 |
| bootstrap.ts / Bun dependencies | Python 3.10+ 标准库 | 替换，无额外运行时包 |
| orch/orch.ts + store.ts | operations 指南与 task-local ledger | 未移植状态机 / CLI 功能对等实现 |
| watch-pr | `pr-status` 一次只读快照 + GitHub 指南 | 未移植持续 watcher |
| check-plan.mjs | `plan-check` | 新实现，明确仅验证结构 |
| worktree-audit.sh | worktree-cleanup playbook | 未移植审计脚本；依靠 live git 和宿主状态 |
| log.sh | `log` JSONL | 新实现，显式路径、单写者 |
| Benny setup / triage / reproduce | issue-automation 指南 | 可配置设计，未实现运行服务 |
| 模型与预算规则 | 当前模型继承；用户显式选择优先 | 无全局配置写入 |
| 子代理与证据 references | explanation / design / review / learning / verification guides | 按职责合并；不保留旧宿主 prompt 模板 |
| docs / README / license | 本仓库文档及上游许可 | 重写文档并保留归属 |
