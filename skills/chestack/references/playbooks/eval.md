# eval

**Use for:** Evaluate an agent workflow or artifact.

Read [host capabilities](../hosts.md) and the relevant [principles](../principles.md) before acting.

1. Specify the task distribution, observable success criteria, baseline, and failure categories before running.
2. Use held-out realistic inputs and avoid expected-answer leakage. Grade behavior and artifacts, not rule-name self-report.
3. Run comparable trials within a stated budget; preserve raw outputs, environment, and evaluator decisions.
4. Report denominators, errors, variance, and limits. Separate deterministic validation from model behavior evaluation.

**Principles:** [explain-the-number](../principles/explain-the-number.md), [test-behavior-not-implementation](../principles/test-behavior-not-implementation.md).

**Done:** The result is reproducible enough to challenge and supports only the measured claim.
