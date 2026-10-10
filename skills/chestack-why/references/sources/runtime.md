# Runtime and incidents

**Use when:** investigating operational pressure, defensive code or an incident-driven change.

**Seed:** owning service, environment, release/build, decision window and known trace/incident IDs.

## Search and read

1. Confirm the target service and environment. Inspect relevant monitor/dashboard queries, units and tags before interpreting charts or thresholds.
2. Bound logs, metrics and traces to the target condition and period; inspect representative traces and aggregate where raw volume is large. Record time zone and coverage.
3. For an incident lead, read the timeline, immediate mitigation, postmortem and action items. Connect the action item to the patch, then separately check deployment and observed outcome.
4. For defensive code, follow incident links across available issue, document, discussion and error sources. Reuse their category templates; track leads with no assigned reader or unavailable destination explicitly.

A matching monitor threshold does not establish which came first. A post-release drop may reflect another patch, upstream change or measurement change. Missing historical retention is unavailable coverage, not zero incidents. Stop at the missing release/causal link rather than claiming the patch worked.

## Return

Service/environment/build, query and time window, units/tags, trace/monitor/incident locators, compact observations and retention limits. Separate incident onset, mitigation, repair, deployment and measured effect. Name competing changes and the decision record needed to connect operational pressure to intent.
