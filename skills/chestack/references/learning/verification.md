# Replay, adopt, and revisit

## Replay before claiming improvement

Define success and cases before the edit. Keep the same inputs and environment across baseline and candidate where feasible. Preserve commands, outputs, and evaluator decisions in review evidence; product instructions should contain repeatable procedures rather than one-off validation diaries.

For a structural check, demonstrate that the bad behavior is possible on the baseline, that the candidate rejects it for the intended reason, and that a valid control still works. A syntax error, unavailable tool, or blanket rejection is not a successful correction.

For a skill or working convention, execute a representative task and inspect its artifact or action sequence. Separate these measurements:

- **Selection:** with the normal pointer and permitted invocation policy, is the intended reference selected? Include an unrelated negative case. Do not force-load the body and count that as selection success.
- **Execution:** once selected, does the procedure reach the expected outcome? Include the original failure and a legitimate alternative that should remain possible.
- **Enforcement:** does a type, check, or behavior test actually prevent the error? Passing documentation validation only proves package consistency.

Use a held-out comparable task when making generalization claims. Label synthetic examples, manual walkthroughs, and real tool executions separately. Record case counts and limits; a self-review or one successful task is not a measured long-term error reduction. If replay is unavailable, report the missing evidence and leave verification pending.

## Adopt at the actual destination

Track states separately: **proposed** (reviewable change), **applied** (written at the stated destination), **verified** (named checks passed), and **adopted** (the intended consumer actually uses that version). States can differ by candidate. A local edit or an open PR does not prove merge, installation, deployment, or future invocation. Verify the relevant consumer only when within the request; otherwise leave adoption pending.

## Review effectiveness

At the next authorized comparable task or user-requested review, inspect whether the owner was reached, the correction prevented recurrence, and valid behavior still worked. Record opportunities observed, repeated failures, false positives, and added effort. Compare against the recorded baseline only when conditions are comparable. For subjective preferences, include the user's feedback.

Keep changes that help; revise weak triggers separately from execution gaps; narrow or roll back checks that reject valid work. Retire guidance when structure makes it redundant. If there are no new opportunities, report effectiveness unknown. Save a checkpoint without creating a schedule unless scheduling was explicitly requested.

## Representative evaluation cases

Use these task shapes to evaluate edits to this workflow. Supply minimal evidence independently of the expected outcome; retain actual outputs in the review.

| Task | Observable acceptance |
|---|---|
| A loaded skill's clear instruction was skipped twice | Execution failure identified; no duplicate instruction; enforcement feasibility assessed |
| A relevant ordinary reference pointer was missed | Pointer ownership identified; selection and body replay reported separately |
| An explicit-only skill was not requested | No invented missed automatic trigger or discovery policy change |
| Two examples violate one repository invariant | One owner; baseline bad behavior reproduced; candidate rejects it and accepts a valid control |
| A single temporary sandbox error was resolved by existing guidance | No durable account rule or recurrence claim |
| A user states one precise working preference | Scoped draft can use that explicit statement; no unauthorized history mining |
| Authorized examples imply conflicting habits | Conflict remains visible; no invented universal preference |
| A retrospective requests analysis only | Candidate proposals delivered without persistent edits or scheduled follow-up |
