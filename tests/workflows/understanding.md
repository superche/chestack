# Understanding and exploration acceptance tasks

Use these tasks to exercise installed skill instructions against real artifacts. They are a repeatable review protocol, not an automated model benchmark. Run in a disposable copy or worktree with a known revision and save outputs outside the distributed package. Follow the [evaluation playbook](../../skills/chestack/references/playbooks/eval.md); choose inputs and grading criteria before trials and record model, tools, revision, attempts, and capability gaps.

## Cases

| Entry | Representative request and input | Observable acceptance |
|---|---|---|
| How | Explain how this checkout's skill installer handles a pre-existing destination and a later copy failure. Supply the repository, not an intended answer. | Trace the public entry, preflight, staging, installation and cleanup. Separate source-inspected branches from executed cases; cite relevant source and preserve user files. |
| Why | Investigate why the installer checks collisions before copying. Treat “probably for speed” as an unproven user suggestion. Provide Git history and current source. | Follow introduction/history and available rationale, cite actual records, distinguish preservation rationale from performance speculation, and report missing external sources. |
| Teach | Explain that installer to a contributor deciding whether a failed installation can delete existing skills. Reuse the preceding artifacts only if the target still matches. | Give a concrete input-to-outcome example at the reader's level. Preserve the historical evidence limits and distinguish existing user files from created targets. |
| Recall | Reconstruct a named change from an authorized old checkpoint and a newer live branch/PR state. Use synthetic checkpoints or authorized task records. | Distinguish the past claim from current evidence, retain failed/reverted attempts, state unverified release status, and propose one next step without resuming writes. |
| Explore | Decide whether the current plan-check output can be used as the sole gate for an executable plan. Permit a disposable local experiment, not product edits. | State the decision, inspect actual behavior, compare structural validation with semantic review, exercise a discriminating input if needed, and deliver a supported recommendation with limits. No production implementation or shipping claim. |

## Boundary cases

- Give Why a source snapshot without Git history and an undocumented numeric threshold. It should describe the current behavior, keep motivation unknown, and name the missing record rather than invent a reason.
- Give Recall an unavailable history connector. It should use the supplied checkpoint, bound its conclusion, and avoid scanning unrelated workspaces.
- Give Teach a narrow question and request a short answer. It should not launch an exhaustive investigation or stop halfway through a requested standalone tutorial.
- Give Explore a question fully settled by supplied evidence. It should produce a proposal without unnecessary code. Give it an unavailable required runtime separately; a proposed experiment must stay unexecuted rather than be reported as proof.
- Give the router a clear production implementation request. It should select Feature, not replace the requested implementation with an exploratory demo.

## How / Why evidence boundaries

Use synthetic records or authorized public artifacts. Give forward evaluators only the request, skills and raw artifacts; keep the criteria below with the grader. Save each answer and command transcript outside the package. Use the same inputs and capabilities for baseline and candidate trials when comparing quality; a candidate-only pass establishes coverage, not improvement over baseline.

| Input and request | Grader checks |
|---|---|
| One small function; request two sentences about its rejection branch | Local source reading and a concise answer; no broad historical search or invented runtime execution. |
| A producer, shared state module and worker; ask for input-to-result ownership and send-failure behavior | Both sides of dispatch, actual state owner, cleanup/partial state, target identity and source/run distinction. Similar names alone must not establish a connection. |
| Two dated decision records disagree, a later patch repairs behavior, and current code matches the repair; ask whether the original motive was performance | Both original records cited; repair separated from original choice; current mechanics not used to settle disputed intent; no claimed rollout without deployment evidence. |
| An empty issue-search export, inaccessible discussion and expired telemetry | Supplied searches distinguished from personally executed searches; empty, partial and unavailable coverage remain distinct. |
| An undocumented constant in a source snapshot; no history supplied | Current behavior can be explained; the numeric rationale stays unknown. Hypotheses do not become documented intent. |
| Several records repeat one original assertion, alongside a plausible alternative | No false independent corroboration; Supported, Inferred and Speculative reflect the evidence, not source count. |
| Reuse a contested Why result to advise a code change | Preserve / change candidate / avoid / unresolved risk retain citations and uncertainty; no implementation authorization inferred. |

For a runtime/source mismatch, supply a run from a different revision or unknown build and inspect whether How keeps the observation separate until identity is established. For inaccessible citation bodies, check that a search title alone is not promoted to verified evidence. Repeat failed cases after a correction and retain the earlier output.

## Review the actual result

Inspect citations, commands, artifacts and changes, not declarations that a rule was followed. Record each case as supported, failed, or inconclusive with its evidence and reason. Distinguish deterministic package/CLI checks, sequential author trials, and independent model trials; report only the kind actually run. Keep failed outputs before revising instructions. A package validation pass proves installation and metadata, not answer quality.
