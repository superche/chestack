# Write reference documentation

Use [Diátaxis reference](https://diataxis.fr/reference/) as the structural basis. Organize entries like the interface so a working reader can locate a fact without reading the page sequentially. State the version and scope. Prefer maintained generated signatures or schemas where available, then check the result.

For each scoped item, establish required inputs, types, defaults, outputs, errors, side effects, and limits from source, schema, help, or authoritative records. Distinguish omitted, empty, and invalid values. Keep facts separate from advice and advocacy; use examples to illustrate an established contract, not to invent one.

Exercise meaningful boundary cases and compare the actual output. Run the [editorial workflow](revision.md), including completeness and lookup checks.

**Done:** each scoped entry is findable and source-backed, with unknown behavior and untested platforms identified.

## Worked example

This sample describes the actual CheStack CLI. Revalidate its contract when the interface changes.

### `plan-check` 命令参考

范围：CheStack 的计划结构检查器。下表描述该命令，不覆盖其他子命令。

```text
python3 skills/chestack/scripts/chestack.py plan-check PATH
```

| 项目 | 契约 |
|---|---|
| `PATH` | 必填的位置参数，指向 UTF-8 文本文件；没有默认路径 |
| 工作目录 | 相对路径以进程当前工作目录为基准 |
| 必需一级标题 | `Goal`、`Scope`、`Constraints`、`Phases`、`Risks`、`Recovery`；各节必须有内容 |
| 阶段 | `Phases` 内至少有一个 `## Phase N: title`；编号从 1 连续递增 |
| 阶段字段 | `Scope:`、`Dependencies:`、`Acceptance:`、`Verification:`；各字段的同行值必须非空 |
| 代码块 | 代码块中的模板不作为已填写的计划内容；未闭合代码块属于结构错误 |
| 占位符 | 代码块外的 `TODO`、`TBD`、`FIXME` 单词或尖括号占位内容会触发错误 |
| 标准输出 | 可读取的输入返回 JSON，包含 `valid_structure`、`errors`、`scope` |
| 退出码 `0` | 结构检查通过 |
| 退出码 `1` | 文件已读取，但结构检查失败 |
| 退出码 `2` | 参数解析错误，或文件读取/解码等处理失败；参数错误为终端诊断，捕获的文件错误为标准错误上的 JSON |
| 副作用 | 此命令不执行计划，不创建计划中的产物，也不改写计划文件 |
| 限制 | 不判断验收条件是否合理、计划能否执行或实现是否正确 |

空文件产生结构错误，不等于缺少 `PATH` 参数。不存在的文件产生读取错误，不等于计划的结构错误。

Author review: compare entries against the current CLI parser and checker implementation. Exercise valid, empty, missing-file, and missing-argument inputs. Do not infer all exit-code behavior from one successful run.
