from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from ato_skill_upgrade.core.feature_fit_evaluator import evaluate_feature
from ato_skill_upgrade.core.maturity_evaluator import evaluate_maturity
from ato_skill_upgrade.core.natural_language import classify_request
from ato_skill_upgrade.core.documentation_reconciler import document_change
from ato_skill_upgrade.errors import SkillUpgradeError


class CoreBehaviorTests(unittest.TestCase):
    def test_ambiguous_request_is_not_overclassified(self) -> None:
        result = classify_request("quiero mejorar este skill pero no se si es feature o madurez")
        self.assertEqual(result["status"], "ambiguous")

    def test_current_repo_reports_setup_as_maturity_strength(self) -> None:
        repo = Path(__file__).resolve().parents[1]
        result = evaluate_maturity(repo)
        self.assertIn("Local setup is a maturity strength and should be proposed as a reusable pattern for target skills.", result["strengths"])

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


if __name__ == "__main__":
    unittest.main()

