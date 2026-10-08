import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


tools = load("chestack_tools", ROOT / "skills/chestack/scripts/chestack.py")
installer = load("installer", ROOT / "scripts/install_skills.py")
validator = load("validator", ROOT / "scripts/validate.py")

PLAN = """# Goal
Export a valid report.
# Scope
CLI export only.
# Constraints
Existing text output stays stable.
# Phases
## Phase 1: Export
Scope: CLI writer.
Dependencies: none.
Acceptance: JSON parses and contains the expected rows.
Verification: Run the real export on a fixture and compare parsed values.
# Risks
Encoding differences.
# Recovery
Revert the owned commit and restore the fixture.
"""


class PlanTests(unittest.TestCase):
    def test_complete_plan(self):
        self.assertEqual(tools.plan_errors(PLAN), [])

    def test_missing_acceptance(self):
        bad = PLAN.replace("Acceptance: JSON parses and contains the expected rows.", "Acceptance:")
        self.assertIn("Phase 1: missing or empty Acceptance", tools.plan_errors(bad))

    def test_fenced_template_does_not_count(self):
        self.assertTrue(tools.plan_errors("```markdown\n" + PLAN + "```"))

    def test_placeholders_fail(self):
        self.assertTrue(tools.plan_errors(PLAN.replace("CLI writer.", "TBD")))

    def test_duplicate_section(self):
        self.assertIn("Duplicate section: goal", tools.plan_errors(PLAN + "\n# Goal\nAgain."))

    def test_phase_order(self):
        self.assertTrue(tools.plan_errors(PLAN.replace("Phase 1:", "Phase 2:")))

    def test_cli_failure_exit(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "plan.md"
            path.write_text("# Goal\nOnly a goal.")
            result = subprocess.run([sys.executable, str(ROOT / "skills/chestack/scripts/chestack.py"),
                                     "plan-check", str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertFalse(json.loads(result.stdout)["valid_structure"])


class LogTests(unittest.TestCase):
    def test_append_preserves_values_and_prior_record(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "decisions.jsonl"
            for value in ['first', 'quote " and newline\n中文']:
                tools.append_log(path, value, "observed", "test.log", "pass")
            entries = [json.loads(line) for line in path.read_text().splitlines()]
            self.assertEqual([e["decision"] for e in entries], ['first', 'quote " and newline\n中文'])

    def test_corrupt_log_is_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "log"
            path.write_text("not json\n")
            with self.assertRaises(ValueError):
                tools.append_log(path, "d", "r", "e", "pass")
            self.assertEqual(path.read_text(), "not json\n")

    def test_empty_evidence_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "log"
            with self.assertRaises(ValueError):
                tools.append_log(path, "d", "r", " ", "pass")
            self.assertFalse(path.exists())


class GitHubTests(unittest.TestCase):
    def test_only_read_commands_and_no_readiness_claim(self):
        calls = []
        def runner(argv, **kwargs):
            calls.append(argv)
            return subprocess.CompletedProcess(argv, 0, '{"state":"OPEN"}' if "view" in argv else '[]', '')
        result = tools.pr_status("superche/chestack", 1, runner)
        self.assertEqual([c[1:3] for c in calls], [["pr", "view"], ["pr", "checks"]])
        self.assertEqual(result["readiness"], "not-evaluated")
        self.assertIn("unresolved-review-threads", result["remaining_evidence"])

    def test_failed_checks_are_collected_without_claiming_readiness(self):
        def runner(argv, **kwargs):
            return subprocess.CompletedProcess(argv, 1, '[{"bucket":"fail"}]', 'private token')
        result = tools.pr_status("owner/repo", 1, runner)
        self.assertTrue(result["required_checks"]["ok"])
        self.assertEqual(result["required_checks"]["data"][0]["bucket"], "fail")
        self.assertEqual(result["readiness"], "not-evaluated")
        self.assertNotIn("private token", json.dumps(result))

    def test_pending_checks_are_valid_observations(self):
        def runner(argv, **kwargs):
            return subprocess.CompletedProcess(argv, 8, '[{"bucket":"pending"}]', '')
        result = tools.pr_status("owner/repo", 1, runner)
        self.assertTrue(result["required_checks"]["ok"])
        self.assertEqual(result["required_checks"]["data"][0]["bucket"], "pending")

    def test_error_payload_is_not_a_check_list(self):
        def runner(argv, **kwargs):
            return subprocess.CompletedProcess(argv, 1, '{"message":"forbidden"}', '')
        self.assertFalse(tools.pr_status("owner/repo", 1, runner)["required_checks"]["ok"])

    def test_timeout_is_bounded_gap(self):
        def runner(argv, **kwargs):
            raise subprocess.TimeoutExpired(argv, 30)
        self.assertEqual(tools.run_json(["gh"], runner)["error"], "TimeoutExpired")

    def test_invalid_json(self):
        def runner(argv, **kwargs):
            return subprocess.CompletedProcess(argv, 0, 'bad', '')
        self.assertFalse(tools.run_json(["gh"], runner)["ok"])

    def test_invalid_repo_does_not_run(self):
        with self.assertRaises(ValueError):
            tools.pr_status("--help", 1)


class PackageTests(unittest.TestCase):
    def test_package(self):
        self.assertEqual(validator.validate(), [])

    def test_unintended_implicit_entry_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            copy = Path(directory) / "package"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            metadata = copy / "skills/chestack/agents/openai.yaml"
            metadata.write_text(metadata.read_text().replace("invocation: false", "invocation: true"))
            self.assertIn("Missing invocation policy or prompt: chestack", validator.validate(copy))

    def test_disabled_discoverable_skill_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            copy = Path(directory) / "package"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            metadata = copy / "skills/chestack-control-ui/agents/openai.yaml"
            metadata.write_text(metadata.read_text().replace("invocation: true", "invocation: false"))
            self.assertIn("Missing invocation policy or prompt: chestack-control-ui", validator.validate(copy))

    def test_full_install_and_relative_dependencies(self):
        with tempfile.TemporaryDirectory() as directory:
            result = installer.install(Path(directory) / ".agents/skills")
            self.assertEqual(len(result), len(json.loads((ROOT / "catalog.json").read_text())["skills"]))
            review = Path(result[0]).parent / "chestack-review"
            self.assertTrue((review / "../chestack/references/review.md").is_file())
            self.assertTrue((review / "../chestack/scripts/chestack.py").is_file())

    def test_understanding_bundle_installs_with_resolvable_composition_links(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / ".agents/skills"
            installer.install(destination)
            for name in ("how", "why", "teach", "recall", "explore"):
                self.assertTrue((destination / ("chestack-" + name) / "SKILL.md").is_file())
            self.assertFalse((destination / "chestack-explain").exists())
            for document in destination.rglob("*.md"):
                for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", document.read_text()):
                    if re.match(r"^[a-z]+://|^#", target):
                        continue
                    relative = target.split("#", 1)[0]
                    if not relative:
                        continue
                    resolved = (document.parent / relative).resolve()
                    self.assertTrue(resolved.is_relative_to(destination.resolve()), (document, target))
                    self.assertTrue(resolved.exists(), (document, target))

    def test_collision_preserves_existing_and_avoids_partial_install(self):
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory)
            existing = dest / "chestack-review"
            existing.mkdir()
            (existing / "mine").write_text("keep")
            with self.assertRaises(ValueError):
                installer.install(dest)
            self.assertEqual((existing / "mine").read_text(), "keep")
            self.assertFalse((dest / "chestack").exists())


if __name__ == "__main__":
    unittest.main()
