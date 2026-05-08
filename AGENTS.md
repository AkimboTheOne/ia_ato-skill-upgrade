# Agent Instructions

`ato-skill-upgrade` is a support skill for controlled evolution of other skills.

Agents should:

- inspect repository context before planning,
- classify requests as `maturity`, `feature`, or `document`,
- ask delimiting questions when the mode or scope is ambiguous,
- preserve the atomic purpose of the target skill,
- produce Markdown and JSON evidence,
- keep write operations explicit and documented.
- use the Spanish canonical memory terminology in `memory/terminology-es.md` for durable definitions, decisions, and history.

Agents must not:

- treat recommendations as implemented changes,
- modify source code through `document` mode,
- expand the target skill scope without approval,
- commit, push, or open PRs unless the user separately asks for repository publishing work.
