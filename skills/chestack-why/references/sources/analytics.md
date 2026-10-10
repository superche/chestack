# Analytics and experiments

**Use when:** investigating thresholds, workload/cost decisions, product behavior or experiment-driven changes.

**Seed:** decision period, feature/experiment ID, metric and cohort, linked analysis or dataset.

## Search and read

1. Inspect available schemas and metric definitions using the authorized tool. With SQL access, use supported catalog inspection (for example `SHOW TABLES` / `DESCRIBE`) before choosing real table and column names. A connector's existence does not establish access to notebooks or every dataset.
2. Define a bounded query: period/time zone, population, exposure, denominator, units and deduplication. Prefer aggregates; retain the exact executed query and compact result, not raw private rows.
3. For a threshold, inspect the distribution available before the choice. For an experiment, distinguish assignment/exposure, outcome analysis and the recorded ship decision. For cost/migration questions, follow relevant query history or data-model lineage where accessible.
4. Check refresh lag, sampling, schema/retention boundaries and instrumentation changes. Compare equivalent periods and cohorts before interpreting a jump or zero rows.

A percentile matching a constant is circumstantial evidence, not recorded intent. An observed effect does not establish who decided to ship or whether the analysis preceded the choice. Duplicated raw events and missing exposure denominators can invalidate comparisons.

## Return

Dataset/metric and schema version when available, exact query/filter, period/cohort, denominator, deduplication and units, compact numeric summary and analysis locator. Separate measured association, recorded decision and unknown causal link. Mark expired history or inaccessible notebooks unavailable; mark truncated results partial.
