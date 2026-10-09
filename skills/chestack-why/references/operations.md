# Investigate operational evidence

Use for runtime constraints, defensive behavior, unexplained thresholds or data-backed decisions. Identify the service/project, environment, release and decision period before querying. Adapt to authorized tools and inspect their schema rather than inventing endpoints, tables or fields.

## Runtime and incidents

Locate the relevant service and dashboard/monitor, inspect query, units and tags, then narrow logs/traces to the target error or request. Capture the bounded time window and release mapping. For an incident lead, read its timeline, mitigation and action items and follow the linked implementation. Separate immediate mitigation, later repair and the original design choice. A monitor with the same numeric threshold does not establish which came first or why.

## Error tracking

Search exception text, stack symbols and affected releases. Open representative events to verify that their stack/environment reaches the target. Record first/last seen, sample coverage, release and resolution notes. Check regrouping, sampling and retention before interpreting disappearance. A manually resolved issue or an automated root-cause summary does not prove a fix; use original events and linked changes.

## Analytics and experiments

Inspect available schemas and metric definitions before querying. Bound the query to a relevant period and cohort; report denominator, units, deduplication, exposure and outcome definitions. Prefer aggregate summaries over raw user rows. For a threshold, examine the distribution available when it was chosen, not only today's percentile. For an experiment, distinguish exposure, observed effect and recorded ship decision.

Check instrumentation changes, refresh lag, retention and schema drift before interpreting a jump or zero rows. Save query, table/metric identifier and compact result sufficient to reproduce the claim. If historical data expired, report unavailable coverage, not evidence of zero activity.

## Causal limits

A drop after a release supports temporal association; check other changes, upstream behavior and measurement changes before attributing it to one patch. Operational evidence can establish a pressure or outcome without establishing author intent. Pair it with a contemporaneous decision record for that claim, or keep the motivation qualified. Stop once the question is settled or the missing discriminating evidence is named; do not scan unrelated production data.
