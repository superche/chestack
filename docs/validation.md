# 验证记录

日期：2026-10-08。版本：0.1.0。

## 已完成的本地验证

| 检查 | 实际结果 | 证据边界 |
|---|---|---|
| `python3 scripts/validate.py` | 通过 | 清单、6 个技能元数据、相对链接、宿主依赖扫描 |
| `python3 -m unittest discover -s tests -v` | 20 项通过 | Python 3.14.6 本地；下列失败路径与安装行为 |
| 系统 skill-creator `quick_validate.py` | 6 个技能通过 | 使用隔离的 PyYAML 验证环境；产品运行时不依赖该包 |
| Codex CLI 0.142.5 marketplace add | `superche-chestack` 被识别 | 本地 marketplace 源，隔离配置 |
| Codex CLI plugin add / list | `chestack@superche-chestack` 已安装且 enabled | 真实 CLI 安装，不修改用户主配置 |
| 安装缓存中的 `scripts/validate.py` | 通过 | 打包后相对引用仍完整 |
| `doctor` | 正确返回本地 git / gh / codex 路径 | 只验证可执行文件存在，不验证账号权限或会话工具 |

工具测试覆盖：真实安装复制、已有文件冲突保留、相对依赖完整性、计划缺失字段、代码块模板误判、阶段顺序、占位符、非零退出、JSONL 多条追加和转义、损坏日志保留、空证据拒绝、GitHub 只读命令、失败/等待检查、错误 JSON 形状、超时和无效仓库参数。

## 独立工作流评估

一个独立验证代理读取实际技能包，以六个场景推演路线、操作及可声明结果，未提供预期答案。它同时运行了结构验证。这是工作流推演，不是六次真实业务执行。

| 场景 | 观察结果 |
|---|---|
| 调查导出缺行，要求不改代码 | 选择 investigation；只读解释和有界探针 |
| 跟进 PR 到绿色，无代理或调度工具 | 选择 babysit/drive；顺序执行；不合并、不承诺未来监控 |
| ChatGPT 只有源码文本，要求实现按钮并展示结果 | 产出可审阅补丁；明确未应用、未运行和未完成 UI 验收 |
| 仓库禁止子代理的评审 | 使用顺序评审；不声称独立评审 |
| 暂停工作并保存进度，存在所属自动化 | 使用 pause-safely；暂停并验证所属调度，保存恢复说明 |
| 点名 prove-it-works | 读取规则正文和验证指南；匹配目标与真实观察 |

验证发现 GitHub pending/failing 检查的合法非零退出码被混为采集失败。已修复：保留退出码与 bucket，单独判断数据是否成功采集；新增 pending 和错误数据形状回归测试。工具始终返回 `readiness: not-evaluated`。

## 尚未覆盖

- ChatGPT 网页、移动端及组织插件分发的真实安装验收。
- 在不同项目中长期执行后的质量和成本对比。
- 原生调度、真实桌面控制、独立代理执行及外部 issue 自动化端到端验收。
- GitHub PR helper 的真实有权限 PR 读取；当前通过模拟的失败、等待和错误路径测试。

GitHub Actions 在每次 push / PR 上运行 Python 3.10 和 3.13 检查。当前 CI 结果以仓库 Actions 页面为准；写入工作流配置不等于已经通过 CI。
