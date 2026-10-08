# encode-lessons-in-structure

**Trigger:** A repeated correction exposes an invariant the repository does not enforce.

Choose the highest effective mechanism:

1. Architecture: one state owner, one supported path, inaccessible invalid operations.
2. Types: make invalid states or combinations unrepresentable.
3. Focused lint or runtime checks: reject the violation and name the supported fix.
4. Behavior tests: exercise the observable failure and the legitimate alternative.
5. Guidance: preserve judgment that cannot be encoded reliably in an existing owner.

Explain why a higher level cannot solve the class before adding a lower-level rule. Reuse enforcement already present; prune obsolete instructions once the mechanism owns the invariant. Keep exceptions narrow and accountable.

**Evidence:** Replay the original failing behavior and a valid control before and after the change. A check that rejects both has not improved the system. Follow [structural correction](../learning/correction.md) for ownership and [verification](../learning/verification.md) for adoption and effect review.
