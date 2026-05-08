from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .natural_language import classify_request


@dataclass
class IterationSession:
    state: str
    mode: str
    request: str
    open_questions: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


def create_session(repo: Path, request: str, mode: str = "auto") -> dict:
    classification = classify_request(request) if mode == "auto" else {"status": "classified", "mode": mode}
    chosen_mode = classification["mode"]
    open_questions: list[str] = []
    state = "draft"
    if classification["status"] == "ambiguous":
        state = "questions"
        open_questions.append(classification["question"])
    else:
        state = "proposal"

    session = IterationSession(
        state=state,
        mode=chosen_mode,
        request=request,
        open_questions=open_questions,
        assumptions=["Repo local usado como fuente primaria de contexto."],
        risks=["No generar plan definitivo si hay ambiguedad critica."],
    )
    out_dir = repo / "workspace" / "skill-upgrade" / "sessions"
    out_dir.mkdir(parents=True, exist_ok=True)
    session_path = out_dir / "iteration-state.json"
    notes_path = out_dir / "iteration-notes.md"
    session_path.write_text(json.dumps(asdict(session), indent=2), encoding="utf-8")
    notes_path.write_text(render_iteration_notes(session), encoding="utf-8")
    data = asdict(session)
    data["session_path"] = str(session_path)
    data["notes_path"] = str(notes_path)
    return data


def render_iteration_notes(session: IterationSession) -> str:
    questions = "\n".join(f"- {item}" for item in session.open_questions) or "- Ninguna"
    assumptions = "\n".join(f"- {item}" for item in session.assumptions) or "- Ninguno"
    risks = "\n".join(f"- {item}" for item in session.risks) or "- Ninguno"
    return (
        "# Iteration Notes\n\n"
        f"- State: {session.state}\n"
        f"- Mode: {session.mode}\n\n"
        "## Request\n\n"
        f"{session.request}\n\n"
        "## Open Questions\n\n"
        f"{questions}\n\n"
        "## Assumptions\n\n"
        f"{assumptions}\n\n"
        "## Risks\n\n"
        f"{risks}\n"
    )

