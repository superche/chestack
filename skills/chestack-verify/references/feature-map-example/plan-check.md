# Plan structure validation

A user submits a Markdown plan and receives a structural verdict without the input file being changed. This does not establish the plan's feasibility or execution success.

## Sub-features

- `plan-valid`: complete required structure returns a positive verdict and exit 0.
- `plan-incomplete`: missing acceptance criteria return a negative verdict and exit 1.
- `plan-readonly`: either verdict preserves the submitted file.

## User entry points

- `plan-cli`: `python3 skills/chestack/scripts/chestack.py plan-check PATH` from the repository root.

## Drive and observe

Preconditions: complete the [baseline](README.md); retain its environment variables. Both cases use `plan-cli`. Run:

```sh
python3 - <<'CHECK'
import json, os, subprocess
from pathlib import Path
repo = Path(os.environ['CHESTACK_VERIFY_REPO'])
run = Path(os.environ['CHESTACK_VERIFY_RUN'])
plan = """# Goal
Validate a local plan.
# Scope
A disposable fixture only.
# Constraints
No network.
# Phases
## Phase 1: Check structure
Scope: fixture file.
Dependencies: none.
Acceptance: structured verdict is returned.
Verification: invoke plan-check.
# Risks
The check is structural only.
# Recovery
Remove the disposable fixture.
"""
for case, content, code in [('plan-valid', plan, 0),
        ('plan-incomplete', plan.replace('Acceptance: structured verdict is returned.\n', ''), 1)]:
    path = run / 'state' / (case + '.md')
    path.write_text(content)
    before = path.read_bytes()
    argv = ['python3', str(repo / 'skills/chestack/scripts/chestack.py'), 'plan-check', str(path)]
    result = subprocess.run(argv, capture_output=True, text=True, timeout=10, cwd=repo)
    (run / 'evidence' / (case + '.json')).write_text(json.dumps(dict(
        entry='plan-cli', case=case, argv=argv, exit_code=result.returncode,
        stdout=result.stdout, stderr=result.stderr), indent=2))
    assert result.returncode == code
    verdict = json.loads(result.stdout)
    assert verdict['valid_structure'] == (code == 0)
    if code:
        assert 'Phase 1: missing or empty Acceptance' in verdict['errors']
    assert path.read_bytes() == before, 'plan-readonly failed'
print('Passed: plan-valid, plan-incomplete, plan-readonly via plan-cli')
CHECK
```

The two JSON artifacts capture the action and result; the assertions check both expected exit codes and file preservation. On failure, retain them and report the assertion or timeout. Follow the index cleanup after the run, including failed attempts.

## Gotchas

- Exit 1 is expected for the deliberately incomplete fixture; exit 2 indicates a different error.
- A positive structural verdict is not proof that the proposed work was executed.
- This sample does not cover every parser edge case or the other CLI commands.
