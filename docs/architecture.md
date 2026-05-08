# Architecture

The skill is a local Python CLI package under `cli/ato_skill_upgrade`.
The main entrypoint is `ato_skill_upgrade.main:run`.

The baseline keeps implementation local and deterministic:

- no network by default,
- no external services,
- no MCP server in v0.2,
- JSON and Markdown outputs as primary evidence formats.

