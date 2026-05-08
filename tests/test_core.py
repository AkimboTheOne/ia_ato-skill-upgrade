from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from ato_skill_upgrade.core.feature_fit_evaluator import evaluate_feature
from ato_skill_upgrade.core.maturity_evaluator import evaluate_maturity
from ato_skill_upgrade.core.natural_language import classify_request
from ato_skill_upgrade.core.documentation_reconciler import document_change
from ato_skill_upgrade.core.external_review import review_external
from ato_skill_upgrade.core.run_contract import run_payload
from ato_skill_upgrade.errors import SkillUpgradeError


class CoreBehaviorTests(unittest.TestCase):
    def test_ambiguous_request_is_not_overclassified(self) -> None:
        result = classify_request("quiero mejorar este skill pero no se si es feature o madurez")
        self.assertEqual(result["status"], "ambiguous")

    def test_current_repo_reports_setup_as_maturity_strength(self) -> None:
        repo = Path(__file__).resolve().parents[1]
        result = evaluate_maturity(repo)
        self.assertIn("Local setup is a maturity strength and should be proposed as a reusable pattern for target skills.", result["strengths"])
        self.assertIn("setup_onboarding", result["categories"])

    def test_setup_feature_fit_is_accepted_when_signals_exist(self) -> None:
        repo = Path(__file__).resolve().parents[1]
        result = evaluate_feature(repo, "mejorar setup local con .venv y PEP 668")
        self.assertEqual(result["decision"], "accepted-for-charter")
        self.assertTrue(result["fit"])

    def test_document_change_requires_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(SkillUpgradeError) as ctx:
                document_change(Path(tmp))
        self.assertEqual(ctx.exception.exit_code, 10)

    def test_external_review_is_read_only_and_writes_workspace_outputs(self) -> None:
        repo = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as workspace:
            result = review_external(Path(workspace), repo, read_only=True)
        self.assertTrue(result["read_only"])
        self.assertIn("external-review-report.json", result["outputs"]["external_review_report_json"])

    def test_run_payload_context(self) -> None:
        repo = Path(__file__).resolve().parents[1]
        result = run_payload(repo, repo / "examples" / "inputs" / "run-context.json")
        self.assertEqual(result["operation"], "context")

    def test_fixture_weak_setup_has_maturity_gaps(self) -> None:
        repo = Path(__file__).resolve().parents[1] / "examples" / "sample-skills" / "weak-setup-skill"
        result = evaluate_maturity(repo)
        self.assertEqual(result["status"], "needs-work")
        self.assertTrue(result["gaps"])

    def test_self_review_blocks_write(self) -> None:
        repo = Path(__file__).resolve().parents[1]
        with self.assertRaises(SkillUpgradeError) as ctx:
            document_change(repo, summary="examples/inputs/execution-summary.md", write=True, yes=True, self_review=True)
        self.assertEqual(ctx.exception.exit_code, 11)

    def test_review_report_is_detected_evidence(self) -> None:
        repo = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as workspace:
            review = review_external(Path(workspace), repo, read_only=True)
            result = document_change(Path(workspace), review_report=review["outputs"]["external_review_report_json"], self_review=True)
        self.assertIn("external review report detected", result["evidence_status"]["detected"])


if __name__ == "__main__":
    unittest.main()
