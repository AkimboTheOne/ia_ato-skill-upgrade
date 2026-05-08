# Changelog

## 0.2.0

- Added baseline v0.2 repository scaffold.
- Added installable Python package with `ato-skill-upgrade` console script.
- Added CLI commands for context discovery, capabilities, doctor, validate, ask, and iterate.
- Added placeholders for analyze, plan, charter, and document change.
- Added baseline documentation, memory, harnesses, examples, and setup scripts.
- Added root `setup-skill.sh` and local setup maturity guidance based on the reference setup improvement.
- Implemented maturity and feature analysis with local setup detected as a strength.
- Implemented plan and charter generation for maturity and feature modes.
- Implemented document-change dry-run reconciliation with evidence classification, preview, manifest, and validation output.
- Added baseline JSON schemas under `contracts/`.
- Added stdlib unittest coverage for request classification, setup maturity detection, feature fit, and evidence enforcement.
- Added external read-only review with read manifest and separated maturity/feature suggestions.
- Added maturity scoring categories for setup, CLI, contracts, tests, docs, memory, harnesses, security, and evidence.
- Added `run --payload-file` contract and request/response schemas.
- Added sample skill fixtures for mature, weak setup, and scope-inflated cases.
- Added document reconciler support for external review reports.
- Added self-review guardrails that block writes and cap recursion depth.
