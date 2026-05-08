# Decisions

- Use stdlib `argparse` for the first implementation cut to avoid dependency installation as a blocker.
- Keep `analyze`, `plan`, `charter`, and `document change` scaffolded until the core logic lands.
- Follow the local `.venv` setup pattern observed in `ia_ato-skill-ado-cli`.
- Add root `setup-skill.sh` as the preferred onboarding command after clone/download.
- Treat installation robustness as a maturity concern: detect host prerequisites, install into `.venv`, and never vendor binaries or compilers.
- Add `review external` as the first productive path for evaluating other skills without modifying them.
- Separate external review recommendations into maturity suggestions and feature suggestions.
- Add `run` contracts before deeper document reconciliation so downstream agents can call stable operations.
- Keep sample skills local and synthetic for deterministic smoke tests.
- Block write operations during self-review to prevent recursive self-modification.
- Let document reconciliation consume external review reports as detected evidence.
- Keep JSON schema validation dependency-free until a stronger validator is justified.
- Use `ready-with-notes` for high-scoring skills with small evidence gaps.
