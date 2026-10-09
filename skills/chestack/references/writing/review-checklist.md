# Editorial review checklist

Read the draft, reader brief, and relevant sources before changing wording. Inspect every applicable row; mark a dimension not applicable only with a reason when keeping a substantial review record. This is a house checklist, not a formal external-standard conformance test. Resolve findings through the [revision workflow](revision.md#close-the-review).

| Dimension | Inspect | Check or correction |
|---|---|---|
| Meaning | Actor, object, quantity, unit, condition, exception, negation, permission, obligation, confidence | Compare source and revision; preserve may/must distinctions and uncertainty |
| Ambiguity | Pronouns, only/not placement, and/or grouping, omitted subjects, noun chains | Identify exactly one referent and grouping; repeat the noun or split the clause; flag unresolved source ambiguity |
| Evidence | Defaults, counts, dates, performance claims, guarantees, vague attribution | Locate the source at the relevant version; name the evidence or qualify/remove the unsupported claim |
| Scope | Tested platform, version, input range, observed versus planned work | Keep the claim inside the evidence; distinguish planned, run, passed, approved, and released |
| Terminology | Identifier spelling, one name per concept, one meaning per term | Preserve interface names; define unfamiliar terms; replace decorative jargon only when meaning survives |
| Procedure | Prerequisites, working directory, placeholders, action order, branch conditions, hazard placement | Walk from the stated initial state; put conditions and consequences before the affected action |
| Execution | Commands, expected output, exit status, side effects, retry and recovery | Execute the authorized safe path and meaningful failure boundary; inspect files/state; label unrun checks |
| Learning | Early observable success, unexplained choices, excessive background, missing checkpoint | Follow as a first-time reader; keep a viable learning path and link optional depth |
| Reference | Required/optional inputs, defaults, omitted/empty/invalid cases, output, errors, limits | Compare each scoped entry with schema/help/source; distinguish missing information from unsupported behavior |
| Explanation | Causal connections, alternatives, historical claims, analogy limits | Trace one input and one relevant edge; source the reason or label it inference |
| Decisions | Final diff, proposal status, alternatives, approval, rollback implications | Compare with actual change or decision records; do not convert a recommendation into agreement |
| Substance | Generic praise, filler, vague attribution, stock openings, repeated summaries | Delete content that adds no meaning; replace claims with supplied facts, never invented numbers |
| Readability | Dense noun phrases, over-compression, awkward fragments, forced symmetry or lists | Restore necessary subjects/connectors; use the natural number of points; keep purposeful sentence variety |
| Presentation | Heading hierarchy, descriptive links, numbered sequence, code/UI distinction, table readability | Inspect the rendered artifact when relevant; open links and verify targets; keep identifiers copyable |
| Standards | Required edition, dictionary/terminology, local template, language | Apply the requested standard's actual checks; list unverified requirements instead of claiming compliance |

## Correction examples

These are invented examples. The supplied context governs any added specificity.

| Source or draft | Review finding | Safe revision or disposition |
|---|---|---|
| “仅管理员可以重试失败任务；重试不会删除草稿。” | Both the role restriction and negation must survive | “只有管理员能重试失败任务。重试不会删除草稿。” |
| “服务通知客户端它已失效。” | The referent of “它” is unknown | Ask or flag which object expired; do not guess during polishing |
| “如果缓存损坏，删除缓存并重启服务。” | Condition applies to both actions | Keep the condition above both ordered steps; do not make deletion unconditional |
| “据业内反馈，这项更改让速度提升一倍。” | Attribution and measurement lack evidence | Request the source and metric; do not turn this into an unqualified claim |
| “校验通过，计划可以上线。” | Structural validation does not establish execution or release readiness | State only the validation result supported by the checker |
| “测试将覆盖回滚。” | A planned check is not completed evidence | Keep future status; never revise to “回滚已验证” |
| “为了能够进一步有效地进行配置的修改……” | Filler obscures the action | “修改配置……” if this preserves the source instruction |

Style rules serve meaning. Do not delete uncertainty as filler, technical precision as jargon, or necessary warnings as verbosity. Preserve legal and safety wording controlled by an authoritative source; flag conflicts instead of silently rewriting it.
