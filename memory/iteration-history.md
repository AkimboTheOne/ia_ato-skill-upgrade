# Iteration History

## 0.2.0 Scaffold

Created the baseline repository structure and CLI scaffold from the v0.2 requirement document.

## 0.2.0 Local Setup Maturity Update

Updated onboarding based on the reference `ia_ato-skill-ado-cli` setup improvement:

- root `setup-skill.sh`,
- `.venv`-only install path,
- host prerequisite checks,
- PEP 668 avoidance,
- explicit dependency boundary between Python packages and system binaries.

## 0.3.0 External Review Cut

- Added read-only external review for local skill repositories.
- Added read manifests for files observed during review.
- Added category-based maturity scoring.
- Split recommendations into maturity and feature suggestion outputs.

## 0.4.0 Run Contract And Fixtures Cut

- Added `run --payload-file`.
- Added request and response schemas for machine invocation.
- Added sample skill fixtures for mature, weak setup, and scope-inflated repositories.
- Added tests for run payloads and fixture-based maturity gaps.

## 0.5.0 Self Review And Document Reconciler Cut

- Added `--review-report` evidence input to document change.
- Added self-review guardrails.
- Blocked writes during self-review.
- Capped self-review recursion depth at 1.

## 0.7.0 Validation And Scoring Cut

- Added lightweight contract validation.
- Added richer maturity statuses.
- Completed mature fixture examples for cleaner smoke testing.

## 0.8.0 CI And Release Governance Cut

- Added GitHub Actions CI.
- Added release governance documentation.
- Synchronized version metadata.
- Added version validation.
