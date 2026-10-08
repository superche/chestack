# Review a skill

1. Reconstruct the decision where the task diverged from its expected outcome. Review judgment, tool use, and a counterexample to the obvious lesson. Retain successful behavior that a proposed edit might break.
2. Locate the skill or reference actually used, or show that the relevant pointer was available and should have been followed under the existing invocation policy. A skill that was unavailable or intentionally explicit-only is not a missed automatic trigger.
3. Classify the failure before choosing an edit:

| Evidence | Diagnosis | Smallest response |
|---|---|---|
| An eligible pointer was visible but the required reference was never loaded | Trigger failure | Clarify the existing pointer or placement; preserve explicit invocation |
| The owner was loaded and followed, yet its steps produced the wrong outcome | Procedure gap | Change the step and its observable completion criterion |
| Clear applicable guidance was loaded but skipped | Execution failure | Identify why it was skipped; prefer enforcement or clearer placement, not a duplicate rule |
| Required tools or permissions were absent | Capability limitation | Check sandbox restrictions and document the actual fallback; do not invent an account fix |
| Guidance worked or another check already prevents the mistake | Already covered | Reject extra prose and retain the working behavior |

4. Patch the existing owner when authorized. Move branch-specific detail behind a precise pointer. Propose a new skill only when no existing owner fits a recurring workflow with a distinct invocation need; do not broaden discovery as a side effect of a body edit.
5. Replay both selection and execution where affected. A direct invocation can test the body, but cannot prove that the pointer selects it correctly. Use the [verification protocol](verification.md) and report that distinction.
