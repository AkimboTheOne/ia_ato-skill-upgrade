# Baseline v0.2 — ato-skill-upgrade

## 0. Control del Documento

| Campo | Valor |
|---|---|
| Nombre del skill | `ato-skill-upgrade` |
| Versión baseline | `v0.2` |
| Versión anterior | `v0.1` |
| Versión objetivo operacional | `v0.99.0` como pre-release candidate hacia `v1.0.0` |
| Comando de activación | `@skill-upgrade` |
| Dominio | Soporte inline a agentes de codificación para mejora controlada de skills existentes |
| Baseline mode | **A — Core CLI Skill** |
| Stack | Python |
| Servicios externos | No aplica en v0.2 |
| HTTPS | No aplica en v0.2 |
| MCP | Referenciado para evolución futura, no funcional en v0.2 |
| Formato primario | Markdown |
| Formato máquina | JSON |
| Naturaleza operativa | Análisis, diagnóstico, planificación, documentación post-ejecución y generación de charters locales |
| Decisión crítica | No implementa cambios de código automáticamente por defecto |
| Nueva capacidad v0.2 | Modo `document` para reconciliar documentación, memoria y harnesses después de un cambio ejecutado |

---

# 1. Resumen Ejecutivo

`ato-skill-upgrade` es un skill CLI en Python, activado por `@skill-upgrade`, diseñado para incorporarse dentro de cualquier repositorio de skill existente y asistir al agente principal de codificación en la identificación, evaluación, planificación y documentación controlada de oportunidades de mejora.

El skill opera **inline** dentro del mismo contexto del repositorio objetivo. Su función no es reemplazar al agente principal ni ejecutar por él, sino servir como soporte metodológico, contextual y verificable para:

- diagnosticar madurez,
- evaluar incorporación de features,
- proteger la atomicidad del skill objetivo,
- generar charters y planes,
- iterar por lenguaje natural antes de consolidar un plan,
- documentar cambios ejecutados por el agente principal,
- actualizar de forma gobernada README, SKILL.md, AGENTS.md, CHANGELOG.md, docs, memory y harnesses,
- producir evidencia Markdown y JSON.

El skill no es un mega-agente ni una plataforma multipropósito. Es un asistente especializado de evolución controlada de skills.

---

# 2. Propósito

Ayudar a un agente de codificación, humano o proceso local a analizar un repositorio de skill existente y producir planes verificables de evolución, maduración, incorporación de features compatibles o documentación post-ejecución, preservando el propósito atómico, la estructura, los contratos, la documentación, las validaciones, la memoria y los harnesses del skill objetivo.

---

# 3. Rol del Skill Frente al Agente Principal

`ato-skill-upgrade` debe entenderse como un **soporte al planner del agente principal**.

No es el ejecutor primario.

## 3.1 Responsabilidades del Agente Principal

El agente principal:

- recibe la solicitud del usuario,
- decide usar o no el skill,
- invoca el skill inline,
- interpreta el plan generado,
- ejecuta cambios dentro de sus propios guardrails,
- entrega evidencia de ejecución,
- solicita documentación post-ejecución cuando aplique.

## 3.2 Responsabilidades de `ato-skill-upgrade`

El skill:

- analiza contexto acotado,
- hace preguntas de delimitación si falta información,
- ayuda a iterar antes de consolidar un plan,
- genera charters,
- genera planes,
- clasifica madurez, feature fit o documentación,
- evalúa atomicidad,
- produce manifiestos,
- documenta cambios ejecutados con base en evidencia.

## 3.3 Responsabilidades que NO Debe Asumir

El skill no debe:

- implementar código directamente por defecto,
- hacer commits,
- abrir PRs,
- modificar código fuente,
- ejecutar comandos destructivos,
- decidir cambios de negocio,
- reemplazar al planner del agente principal,
- convertir una conversación de mejora en refactor sin aprobación.

---

# 4. Modos Principales del Skill

A partir de v0.2, `ato-skill-upgrade` tiene tres modos principales:

```txt
ato-skill-upgrade
├── maturity   # Diagnostica brechas y maduración
├── feature    # Evalúa incorporación de nuevas capacidades
└── document   # Documenta cambios ejecutados con base en plan + evidencia
```

---

# 5. Modo `maturity`

## 5.1 Objetivo

Evaluar el estado de madurez de un skill existente y generar un plan para avanzar hacia v1.0 o un nivel superior de confiabilidad operacional.

## 5.2 Cuándo Usarlo

- “Qué le falta a este skill para v1.0”
- “Maduremos este repositorio”
- “Revisa brechas de CLI, docs, validaciones y seguridad”
- “Genera un plan de estabilización”

## 5.3 Salidas

- `maturity-report.md`
- `maturity-report.json`
- `maturity-plan.md`
- `release-candidate-checklist.md`

---

# 6. Modo `feature`

## 6.1 Objetivo

Evaluar si un requerimiento, ajuste o nueva capacidad debe incorporarse al skill existente, reformularse, postergarse, tratarse como refactor o separarse como skill complementario.

## 6.2 Cuándo Usarlo

- “Quiero agregar esta capacidad”
- “Evalúa si este feature encaja”
- “Esto parece útil, ¿va dentro del skill?”
- “Genera charter para este ajuste”

## 6.3 Salidas

- `feature-fit-report.md`
- `feature-fit-report.json`
- `feature-charter.md`
- `feature-decision.json`

---

# 7. Modo `document`

## 7.1 Objetivo

Documentar de forma consistente un cambio ya ejecutado por el agente principal, usando el plan generado, el charter, el manifiesto, el diff o evidencia de ejecución.

Este modo reconcilia:

- documentación raíz,
- documentación técnica,
- memoria,
- harnesses,
- changelog,
- conocimiento del skill.

## 7.2 Principio Central

```txt
El skill no documenta intenciones.
Documenta cambios ejecutados o evidencia verificable de ejecución.
```

## 7.3 Cuándo Usarlo

- Después de que el agente principal ejecutó un cambio.
- Después de aplicar un feature planificado.
- Después de madurar documentación, CLI, validaciones o estructura.
- Después de corregir el repositorio según un charter.
- Cuando se quiere actualizar memoria y harnesses de forma coherente.

## 7.4 Cuándo No Usarlo

No debe usarse para:

- inventar resultados,
- documentar cambios no ejecutados,
- reescribir documentación sin evidencia,
- modificar código,
- alterar contratos sin validación,
- crear narrativa falsa de avance.

## 7.5 Archivos que Puede Actualizar

Permitidos bajo `--write` explícito:

```txt
README.md
SKILL.md
AGENTS.md
CHANGELOG.md

docs/
  architecture.md
  activation.md
  cli.md
  validation.md
  configuration.md
  security.md
  context-discovery.md
  scope-governance.md
  maturity-model.md
  feature-fit.md

memory/
  knowledge.md
  decisions.md
  iteration-history.md

harnesses/
  restrictions.md
  behavior-limits.md
  safety-rules.md
  acceptance-checks.md
  atomicity-checks.md
  maturity-checks.md
  feature-fit-checks.md
```

## 7.6 Archivos que NO Puede Modificar en v0.2

```txt
cli/
src/
services/
server/
mcp/
contracts/
schemas/
tests/
scripts/
pyproject.toml
Makefile
```

Salvo una futura decisión explícita de evolución. En v0.2, el modo `document` es documental, no implementador.

---

# 8. Activación por Lenguaje Natural

El skill debe soportar activación por lenguaje natural, siempre dentro del contexto de uso del agente principal.

## 8.1 Activación Semántica de Madurez

Ejemplos:

- “Evalúa qué le falta a este skill para estar listo”
- “Llévalo hacia v1.0”
- “Revisa madurez del repo”
- “Haz diagnóstico del skill”
- “Qué brechas tiene este skill”

## 8.2 Activación Semántica de Feature

Ejemplos:

- “Quiero agregar este feature”
- “Evalúa si esta mejora encaja”
- “Esto debería ir en el skill o ser otro skill”
- “Convierte esta idea en charter”
- “Define el alcance de esta mejora”

## 8.3 Activación Semántica de Documentación

Ejemplos:

- “Documenta el cambio que acabamos de hacer”
- “Actualiza README, memoria y changelog según lo ejecutado”
- “Reconciliemos la documentación con el resultado”
- “Genera el registro de iteración”
- “Actualiza el conocimiento del skill después de este cambio”
- “Alinea la documentación con el plan y el diff”

## 8.4 Activación Ambigua

Si el usuario dice:

- “Actualiza el skill”
- “Mejóralo”
- “Hazlo más maduro”
- “Documenta esto”
- “Agrega esto”

El skill debe preguntar o inferir con límites:

```txt
¿Deseas operar en modo maturity, feature o document?
```

Si existe suficiente contexto reciente, puede proponer:

```txt
Por el contexto, esto parece modo document post-ejecución.
Procederé en dry-run salvo que indiques --write.
```

---

# 9. Iteración Inline Antes del Plan

## 9.1 Principio

`ato-skill-upgrade` debe permitir una fase conversacional iterativa antes de consolidar el plan o charter.

Esto es necesario porque el skill trabaja como soporte al planner del agente principal.

## 9.2 Comportamiento Esperado

Antes de generar un plan definitivo, el skill debe poder:

- analizar contexto parcial,
- detectar ambigüedades,
- formular preguntas de delimitación,
- proponer supuestos,
- clasificar riesgos,
- rechazar alcance peligroso,
- separar madurez, feature y documentación,
- construir un borrador de decisión,
- esperar confirmación o trabajar con supuestos si se exige avanzar.

## 9.3 Estados de Iteración

```txt
draft       -> análisis preliminar
questions   -> preguntas abiertas
assumptions -> supuestos declarados
proposal    -> propuesta de alcance
confirmed   -> listo para plan/charter
finalized   -> plan o charter generado
documented  -> documentación post-ejecución generada/aplicada
```

## 9.4 Comandos Relacionados

```bash
ato-skill-upgrade ask "quiero mejorar este skill, pero no sé si es feature o madurez"
ato-skill-upgrade iterate --repo . --mode auto
ato-skill-upgrade iterate --repo . --request request.md --state draft
ato-skill-upgrade plan --repo . --from-session workspace/skill-upgrade/sessions/session.json
```

## 9.5 Salida de Iteración

```txt
iteration-notes.md
iteration-state.json
open-questions.md
assumptions.md
scope-proposal.md
```

---

# 10. Activación Explícita

```txt
@skill-upgrade maturity
@skill-upgrade feature
@skill-upgrade document
@skill-upgrade plan
@skill-upgrade diagnosticar
@skill-upgrade v1
```

---

# 11. Activación por Máquina o Script

## 11.1 Madurez

```bash
ato-skill-upgrade analyze --repo . --mode maturity --format json
ato-skill-upgrade plan maturity --repo . --target v1.0 --out exports/skill-upgrade
```

## 11.2 Feature

```bash
ato-skill-upgrade analyze --repo . --mode feature --request request.md --format json
ato-skill-upgrade charter feature --repo . --request request.md --out exports/skill-upgrade
```

## 11.3 Documentación Post-Ejecución

```bash
ato-skill-upgrade document change \
  --repo . \
  --plan exports/skill-upgrade/plans/feature-plan.md \
  --summary execution-summary.md \
  --dry-run
```

```bash
ato-skill-upgrade document change \
  --repo . \
  --plan exports/skill-upgrade/plans/feature-plan.md \
  --manifest workspace/skill-upgrade/manifests/execution.json \
  --format json
```

```bash
ato-skill-upgrade document change \
  --repo . \
  --plan exports/skill-upgrade/plans/feature-plan.md \
  --summary execution-summary.md \
  --write \
  --yes
```

---

# 12. CLI Recomendada

## 12.1 Context Discovery

```bash
ato-skill-upgrade context
ato-skill-upgrade context --json
ato-skill-upgrade capabilities
ato-skill-upgrade capabilities --json
ato-skill-upgrade usage
ato-skill-upgrade examples
ato-skill-upgrade schema
```

## 12.2 Diagnóstico y Validación

```bash
ato-skill-upgrade doctor
ato-skill-upgrade validate
ato-skill-upgrade validate --format json
```

## 12.3 Lenguaje Natural

```bash
ato-skill-upgrade ask "qué le falta a este skill para v1.0"
ato-skill-upgrade ask "evalúa si este feature encaja"
ato-skill-upgrade ask "documenta el cambio ejecutado según este plan"
```

## 12.4 Iteración Inline

```bash
ato-skill-upgrade iterate --repo . --mode auto
ato-skill-upgrade iterate --repo . --request request.md
ato-skill-upgrade iterate --repo . --from-session session.json
```

## 12.5 Planificación

```bash
ato-skill-upgrade plan maturity --repo . --target v1.0
ato-skill-upgrade plan feature --repo . --request request.md
```

## 12.6 Charter

```bash
ato-skill-upgrade charter maturity --repo . --target v1.0 --out exports/skill-upgrade
ato-skill-upgrade charter feature --repo . --request request.md --out exports/skill-upgrade
```

## 12.7 Documentación

```bash
ato-skill-upgrade document change --repo . --plan plan.md --summary summary.md --dry-run
ato-skill-upgrade document change --repo . --plan plan.md --manifest execution.json --dry-run
ato-skill-upgrade document change --repo . --plan plan.md --summary summary.md --write --yes
```

---

# 13. Reglas de Escritura del Modo `document`

## 13.1 Por Defecto

Todo opera en modo `dry-run`.

## 13.2 Para Escribir

Requiere:

```txt
--write
--yes
```

y al menos una fuente de evidencia:

- `--plan`
- `--charter`
- `--summary`
- `--manifest`
- `--diff`
- `--validation-report`

## 13.3 Nunca Debe Escribir

- código fuente,
- tests,
- scripts,
- configuración sensible,
- archivos locales,
- secretos,
- binarios,
- locks,
- artefactos de build.

---

# 14. Evidencia Requerida para Documentar

El modo `document` debe distinguir entre:

| Tipo | Definición |
|---|---|
| Detectado | Evidencia observada en archivos/diff |
| Reportado | Declaración del agente principal o usuario |
| Inferido | Supuesto razonable, marcado explícitamente |
| Pendiente | Falta evidencia |

No debe mezclar estos estados.

---

# 15. Salidas del Modo `document`

```txt
documentation-update-plan.md
documentation-diff-preview.md
documentation-update-manifest.json
documentation-validation-report.json
updated-files-manifest.json
```

## 15.1 `documentation-update-manifest.json`

Debe contener:

```json
{
  "mode": "document",
  "repo": ".",
  "inputs": {
    "plan": "plan.md",
    "summary": "execution-summary.md",
    "manifest": "execution.json",
    "diff": "git.diff"
  },
  "evidence_status": {
    "detected": [],
    "reported": [],
    "inferred": [],
    "pending": []
  },
  "files_planned": [],
  "files_updated": [],
  "write_enabled": false,
  "dry_run": true,
  "risks": [],
  "warnings": [],
  "acceptance": []
}
```

---

# 16. Estructura Recomendada del Repositorio

```txt
repo/
  AGENTS.md
  README.md
  SKILL.md
  CHANGELOG.md
  Makefile
  .env.example
  .gitignore
  pyproject.toml

  docs/
    architecture.md
    activation.md
    cli.md
    validation.md
    security.md
    configuration.md
    context-discovery.md
    scope-governance.md
    maturity-model.md
    feature-fit.md
    document-change.md
    inline-iteration.md

  cli/
    README.md
    ato_skill_upgrade/
      __init__.py
      main.py
      commands/
        analyze.py
        ask.py
        iterate.py
        plan.py
        charter.py
        document.py
        context.py
        capabilities.py
        validate.py
        doctor.py
      core/
        repository_scanner.py
        maturity_evaluator.py
        feature_fit_evaluator.py
        documentation_reconciler.py
        inline_iteration_manager.py
        atomicity_guard.py
        charter_generator.py
        manifest_writer.py
        safe_command_runner.py
      models/
        repository_profile.py
        maturity_report.py
        feature_decision.py
        documentation_update.py
        iteration_session.py
        charter.py
      templates/
        maturity-charter.md.j2
        feature-charter.md.j2
        baseline-upgrade-plan.md.j2
        documentation-update-plan.md.j2
        documentation-diff-preview.md.j2
        manifest.json.j2

  bin/
    ato-skill-upgrade

  scripts/
    install.sh
    bootstrap.sh
    validate.sh
    doctor.sh

  examples/
    invocation.md
    natural-language.md
    inline-iteration.md
    document-change.md
    machine-cli.md
    context-discovery.md
    inputs/
      feature-request.md
      maturity-request.md
      execution-summary.md
    outputs/
      maturity-report.md
      feature-decision.md
      charter.md
      documentation-update-plan.md
      manifest.json

  memory/
    knowledge.md
    decisions.md
    iteration-history.md

  harnesses/
    restrictions.md
    behavior-limits.md
    safety-rules.md
    acceptance-checks.md
    atomicity-checks.md
    maturity-checks.md
    feature-fit-checks.md
    document-change-checks.md
    inline-iteration-checks.md

  workspace/
    skill-upgrade/
      scans/
      reports/
      manifests/
      sessions/
      doctor/
      document/

  exports/
    skill-upgrade/
      charters/
      reports/
      plans/
      documentation/

  logs/
    skill-upgrade/
      .gitkeep

  tmp/
    skill-upgrade/
      .gitkeep

  .github/
    copilot-instructions.md

  .agents/
    skills/
      ato-skill-upgrade/
        SKILL.md
        scripts/
        examples/
```

---

# 17. Variables de Entorno y Configuración

## 17.1 `.env.example`

```bash
ATO_SKILL_UPGRADE_DEFAULT_REPO=.
ATO_SKILL_UPGRADE_WORKSPACE_DIR=workspace/skill-upgrade
ATO_SKILL_UPGRADE_EXPORT_DIR=exports/skill-upgrade
ATO_SKILL_UPGRADE_LOG_LEVEL=info
ATO_SKILL_UPGRADE_ALLOW_LOCAL_COMMANDS=false
ATO_SKILL_UPGRADE_MAX_SCAN_FILES=2000
ATO_SKILL_UPGRADE_MAX_FILE_SIZE_KB=512
ATO_SKILL_UPGRADE_DEFAULT_OUTPUT=md
ATO_SKILL_UPGRADE_DOCUMENT_DEFAULT_DRY_RUN=true
ATO_SKILL_UPGRADE_INLINE_ITERATION_ENABLED=true
```

## 17.2 `config.example.yaml`

```yaml
defaults:
  repo: "."
  workspace_dir: "workspace/skill-upgrade"
  export_dir: "exports/skill-upgrade"
  output: "md"
  allow_local_commands: false
  max_scan_files: 2000
  max_file_size_kb: 512

inline_iteration:
  enabled: true
  persist_sessions: true
  require_confirmation_before_plan: true

document_change:
  default_dry_run: true
  require_evidence: true
  require_write_confirmation: true
  allowed_files:
    - README.md
    - SKILL.md
    - AGENTS.md
    - CHANGELOG.md
    - docs/**
    - memory/**
    - harnesses/**
  denied_files:
    - cli/**
    - src/**
    - services/**
    - server/**
    - mcp/**
    - contracts/**
    - schemas/**
    - tests/**
    - scripts/**
    - pyproject.toml
    - Makefile

analysis:
  read_files:
    - README.md
    - SKILL.md
    - AGENTS.md
    - CHANGELOG.md
  scan_dirs:
    - docs
    - memory
    - harnesses
    - examples
    - scripts
    - cli
    - tests

security:
  deny_globs:
    - ".env"
    - ".env.*"
    - "*.pem"
    - "*.key"
    - "*.pfx"
    - "secrets.*"
  redact_patterns:
    - "token"
    - "secret"
    - "password"
    - "pat"
    - "api_key"

commands:
  allowlist:
    - "git status --short"
    - "git ls-files"
    - "python -m pytest --collect-only"
    - "make -n validate"
```

---

# 18. Harnesses Nuevos v0.2

```txt
harnesses/
  document-change-checks.md
  inline-iteration-checks.md
```

## 18.1 `document-change-checks.md`

Debe validar:

- existe evidencia,
- el cambio fue ejecutado o reportado,
- la documentación no inventa resultados,
- los archivos objetivo están permitidos,
- se genera preview antes de write,
- se actualiza changelog si aplica,
- se actualiza memoria si aplica,
- se actualizan harnesses si cambian límites,
- no se modifica código.

## 18.2 `inline-iteration-checks.md`

Debe validar:

- preguntas abiertas registradas,
- supuestos marcados,
- modo elegido,
- alcance confirmado,
- riesgos identificados,
- plan no generado prematuramente,
- decisión final trazable.

---

# 19. Reglas de Seguridad

1. No leer archivos fuera del repo salvo autorización explícita.
2. No imprimir secretos.
3. No ejecutar comandos arbitrarios.
4. No modificar archivos por defecto.
5. No modificar código en modo `document`.
6. No documentar cambios sin evidencia suficiente.
7. No generar planes definitivos si hay ambigüedad crítica no resuelta, salvo instrucción explícita de avanzar con supuestos.
8. No hacer red por defecto.
9. No hacer commits.
10. No abrir PRs.
11. No ejecutar `git push`.
12. No convertir recomendaciones en cambios automáticos.
13. No ocultar supuestos.
14. No ampliar alcance del skill objetivo sin aprobación humana.

---

# 20. Validaciones Verificables

## 20.1 Comandos

```bash
make install
make bootstrap
make doctor
make validate
make test

ato-skill-upgrade doctor
ato-skill-upgrade validate --format json
ato-skill-upgrade analyze --repo examples/sample-skill --mode maturity --format json
ato-skill-upgrade analyze --repo examples/sample-skill --mode feature --request examples/inputs/feature-request.md --format json
ato-skill-upgrade iterate --repo examples/sample-skill --request examples/inputs/feature-request.md
ato-skill-upgrade document change --repo examples/sample-skill --plan examples/outputs/charter.md --summary examples/inputs/execution-summary.md --dry-run
```

## 20.2 Evidencia Esperada

- exit code,
- JSON report,
- Markdown report,
- logs,
- manifest,
- checklist,
- warnings,
- errores accionables,
- preview documental,
- session state de iteración.

---

# 21. Códigos de Salida

| Código | Significado |
|---|---|
| 0 | OK |
| 1 | Error general |
| 2 | Configuración inválida |
| 3 | Repositorio no detectado |
| 4 | No parece un skill |
| 5 | Riesgo de atomicidad detectado |
| 6 | Solicitud ambigua |
| 7 | Validación fallida |
| 8 | Comando local bloqueado |
| 9 | Archivo sensible bloqueado |
| 10 | Evidencia insuficiente para documentar |
| 11 | Escritura bloqueada por política |
| 12 | Iteración pendiente de confirmación |

---

# 22. Criterios de Aceptación v0.2

El skill será aceptable como baseline v0.2 si:

- conserva los criterios v0.1,
- agrega modo `document`,
- agrega soporte explícito de iteración inline,
- soporta activación por lenguaje natural para `maturity`, `feature` y `document`,
- genera sesión de iteración,
- genera plan desde sesión confirmada,
- genera preview documental,
- genera manifest de documentación,
- no modifica documentación sin `--write --yes`,
- no modifica código en modo `document`,
- exige evidencia para documentar,
- actualiza memoria/harnesses sugeridos,
- distingue detectado, reportado, inferido y pendiente,
- produce salidas Markdown y JSON.

---

# 23. Riesgos y Mitigaciones

| Riesgo | Mitigación |
|---|---|
| Convertirse en mega-skill | Mantener solo `maturity`, `feature`, `document` |
| Ejecutar shell peligroso | Allowlist y comandos bloqueados por defecto |
| Documentar cambios no hechos | Evidencia obligatoria |
| Cambiar documentación sin control | `dry-run` por defecto |
| Modificar código accidentalmente | Denylist estricta en modo `document` |
| Generar plan prematuro | Estado de iteración y confirmación |
| Confundir feature con madurez | Clasificación obligatoria |
| Sobredimensionar v0.2 | Sin red, sin HTTPS, sin MCP funcional |
| Diluir rol del agente principal | El skill soporta planificación, no reemplaza ejecución |

---

# 24. Decisiones Fuera de Alcance v0.2

- Implementar código automáticamente.
- Refactorizar repositorios.
- Ejecutar cambios de arquitectura.
- Hacer commits.
- Abrir pull requests.
- Integrarse con GitHub/Azure DevOps APIs.
- Exponer HTTPS.
- Implementar MCP funcional.
- Coordinar múltiples skills por red.
- Convertirse en catálogo de skills.
- Ejecutar análisis remoto.
- Modificar scripts, tests o código en modo `document`.

---

# 25. Roadmap Sugerido

## v0.1

- Baseline inicial.
- CLI básica.
- Modos `maturity` y `feature`.
- Markdown + JSON.
- Harnesses y memoria.

## v0.2

- Modo `document`.
- Iteración inline.
- Activación natural ampliada.
- Preview documental.
- Manifest de documentación.
- Guardrails de escritura documental.

## v0.3

- Score de madurez ponderado.
- Mejor análisis de CLI.
- Mejor detección de contratos.
- Mejor análisis de cambios por git diff local.
- Sugerencias de patches documentales no aplicados.

## v0.99.0

- Release candidate interno.
- Validaciones completas.
- Contratos estables.
- Documentación final.
- Checklist v1.0.

## v1.0.0

- CLI estable.
- Documentación coherente.
- Tests suficientes.
- Seguridad revisada.
- Release governance.

---

# 26. Historial de Iteraciones

| Versión | Cambio | Motivo | Impacto | Decisiones |
|---|---|---|---|---|
| v0.1 | Creación baseline `ato-skill-upgrade` | Incorporar madurez y feature fit inline en repositorios de skills | Define CLI, alcance y límites | Baseline A, sin red, sin HTTPS, sin MCP funcional |
| v0.2 | Incorporación de modo `document` e iteración inline | Cerrar ciclo plan → ejecución por agente principal → documentación consistente | Agrega documentación post-ejecución y sesiones iterativas | Escritura documental con evidencia, dry-run por defecto, sin modificación de código |

---

# 27. Próximos Pasos para Agente Constructor

1. Actualizar baseline v0.1 a v0.2.
2. Crear comando `ask`.
3. Crear comando `iterate`.
4. Crear comando `document change`.
5. Implementar `inline_iteration_manager.py`.
6. Implementar `documentation_reconciler.py`.
7. Crear plantillas de documentación.
8. Crear manifests JSON.
9. Crear harnesses nuevos.
10. Actualizar `SKILL.md`, `README.md`, `AGENTS.md`, `CHANGELOG.md`.
11. Añadir ejemplos de lenguaje natural.
12. Añadir ejemplos máquina.
13. Añadir validaciones para evidencia insuficiente.
14. Probar `dry-run`.
15. Probar bloqueo de escritura en archivos no permitidos.

---

# 28. Regla de Oro v0.2

```txt
ato-skill-upgrade ayuda al agente principal a pensar, planear y documentar mejor.
No lo reemplaza, no ejecuta por él y no convierte un skill especializado en una hidra con README.
```
