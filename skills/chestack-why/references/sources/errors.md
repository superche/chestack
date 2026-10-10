# Error tracking

**Use when:** investigating the exceptions or failure trajectories behind a guard, retry or repair.

**Seed:** organization/project/environment, exception text, stack symbol, target release and period.

## Search and read

1. Confirm project scope; search exact errors and stack symbols, then narrow by release and environment. Check tool filters and pagination before treating the result as complete.
2. Open representative original events. Verify that stack, tags and breadcrumbs actually reach the target; a matching title alone is insufficient.
3. Read first/last seen, event counts, affected releases and author/resolution notes. Check changed fingerprints, new groups, sampling and retention before interpreting disappearance.
4. Follow the linked patch and release record. Compare with other changes in that release or upstream fixes before attributing an outcome.

A manually resolved issue is a workflow marker. An automated root-cause narrative is a hypothesis source; return to original events to support a claim. A stack proves involvement in an event, not why the author chose a design.

## Return

Project/environment, issue and representative event locators, relevant stack excerpt, first/last-seen period, counts and sampling/retention limits, release mapping and attributed notes. Separate observed errors, proposed explanation and verified outcome; flag regrouping and missing release evidence.
