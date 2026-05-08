# Baseline v0.1 — `ato-skill-po`

> Charter técnico, operativo y fundacional para construir el skill **Product Owner / Technical Product Owner** activado por `@po`.

---

## 1. Identidad del Skill

| Campo | Valor |
|---|---|
| Nombre del skill | `ato-skill-po` |
| Versión baseline | `v0.1` |
| Baseline mode | **Baseline B — CLI Skill with External Skill Services** |
| Comando/binario principal | `ato-skill-po` |
| Activación explícita corta | `@po` |
| Stack objetivo | Python |
| Modo operativo | Local-first |
| Especialidad | Product Owner / Technical Product Owner de negocio |
| Perfil arquitectónico | TPO Engine acotado |
| Formato primario | Markdown (`.md`) |
| Formato máquina | JSON manifests |
| Memoria | Contextual de negocio, local al proyecto asistido |
| Política de memoria | Append-only por defecto |
| Mutación de memoria | Solo bajo instrucción explícita del usuario |
| Servicios externos | Delegados a otros skills CLI/MCP |
| Integración ADO inicial | Delegada a `ato-skill-ado-cli` |
| Integración Jira | Diferida a skill futuro |
| HTTPS | No incluido en v0.1 |
| MCP | Referenciado para evolución futura |
| Publicación directa en herramientas externas | Fuera de alcance v0.1 |

---

## 2. Propósito

`ato-skill-po` es un skill local-first especializado en **Product Ownership** y **Technical Product Ownership**.

Su propósito es asistir en la construcción, mantenimiento y uso de una **memoria contextual de negocio** dentro del repositorio o proyecto donde sea invocado, para generar artefactos estructurados de definición de producto.

El skill parte de una especialidad agnóstica, pero al trabajar sobre un proyecto concreto debe evolucionar hacia una comprensión específica del dominio, manteniendo trazabilidad, memoria, decisiones, supuestos y coherencia documental.

El skill produce principalmente:

- épicas,
- features,
- historias de usuario,
- criterios de aceptación,
- planes de trabajo,
- wikis funcionales,
- documentación de negocio,
- mapas de dominio,
- roadmaps,
- releases,
- milestones,
- dependencias,
- bounded contexts,
- matrices de trazabilidad,
- estructuras base de documentación de negocio.

---

## 3. Fórmula del Skill

El skill cumple la fórmula mínima:

```txt
Skill = tarea repetible + conocimiento contextual + procedimiento verificable + salida estándar
```

| Elemento | Definición |
|---|---|
| Tarea repetible | Construir, mantener y usar memoria contextual de producto para generar artefactos PO/TPO |
| Conocimiento contextual | Dominio de negocio, reglas, stakeholders, roadmap, decisiones, supuestos, historias, documentación, fuentes externas delegadas |
| Procedimiento verificable | CLI, plantillas, manifests JSON, logs, memoria append-only, validaciones, harnesses |
| Salida estándar | Markdown + JSON manifests |

---

## 4. Definición Operacional

`ato-skill-po` es un skill Python CLI, activado por `@po`, que opera localmente sobre el proyecto donde asiste, usando lenguaje natural, modelos LLM y artefactos disponibles para construir una memoria contextual de negocio y generar contenido de producto.

El skill no administra plataformas externas por sí mismo. Cuando se requiera interactuar con Azure DevOps, Jira u otros sistemas, debe apoyarse en skills especializados, inicialmente:

```txt
Azure DevOps → ato-skill-ado-cli
Jira → skill futuro
```

El skill no debe convertirse en un super-skill. Su responsabilidad principal es:

```txt
Generar contenido PO/TPO coherente, trazable y contextualizado.
```

---

## 5. Criterio de Decisión del Skill

El skill debe activarse cuando la intención del usuario sea:

- descubrir o refinar contexto de negocio,
- generar una épica,
- generar una feature,
- generar una historia de usuario,
- generar criterios de aceptación,
- generar un plan de trabajo,
- generar documentación funcional,
- crear o actualizar memoria contextual local,
- crear una estructura base de documentación de negocio,
- organizar documentación por fases, historias, dominios o producto,
- mantener coherencia entre artefactos PO/TPO,
- preparar contenido para ser publicado por otro skill,
- transformar contexto recuperado desde ADO/Jira en artefactos PO/TPO.

No debe activarse para:

- implementar código,
- tomar decisiones ejecutivas autónomas,
- modificar directamente Azure DevOps/Jira,
- administrar infraestructura,
- operar pipelines,
- diseñar arquitectura técnica profunda,
- reemplazar aprobación humana de producto.

---

## 6. Modelo de Activación

### 6.1 Activación Explícita

```txt
@po <acción>
```

Ejemplos:

```txt
@po generar historia de usuario para onboarding
@po crear épica para autenticación empresarial
@po refinar esta feature
@po generar wiki funcional del dominio pagos
@po crear estructura base de documentación de negocio
@po organizar documentación por dominio
```

### 6.2 Activación por Lenguaje Natural

Cuando el skill esté cargado, debe poder activarse semánticamente ante solicitudes como:

```txt
Necesito definir el producto para este módulo.
Ayúdame a convertir este contexto en historias.
Genera una épica con sus features.
Organiza la documentación funcional del proyecto.
Crea una estructura de negocio para este repo.
Construye un plan de trabajo por fases.
Aterriza este dominio en una memoria de producto.
Refina estas historias con criterios de aceptación.
```

### 6.3 Activación por Máquina o Script

```bash
ato-skill-po context --json
ato-skill-po capabilities --json
ato-skill-po generate story --input examples/story.input.json --json
ato-skill-po generate epic --from memory/product/context.md --out exports/po/epics/
ato-skill-po scaffold business-docs --strategy domain --out docs/business/
ato-skill-po validate --format json
```

### 6.4 Activación de Descubrimiento de Contexto

Uso humano:

```bash
ato-skill-po ask "¿Cómo uso este skill?"
ato-skill-po context
ato-skill-po usage
ato-skill-po examples
ato-skill-po capabilities
```

Uso máquina:

```bash
ato-skill-po context --json
ato-skill-po capabilities --json
ato-skill-po schema --json
ato-skill-po usage --json
```

### 6.5 Activación Ambigua

Si la intención es probable pero incompleta, el skill debe pedir delimitación mínima.

Ejemplos ambiguos:

```txt
Haz historias.
Organiza esto.
Define el producto.
Crea la documentación.
```

Respuesta esperada:

```txt
Necesito delimitar dominio, objetivo, audiencia, tipo de artefacto y fuente de contexto antes de generar contenido.
```

### 6.6 No Activación

No debe activarse cuando la solicitud esté fuera del dominio PO/TPO.

Ejemplos:

```txt
Implementa este servicio.
Despliega la infraestructura.
Corrige este bug.
Publica directamente en Azure DevOps.
Decide la prioridad final del roadmap.
```

---

## 7. Cuándo Usarlo

Usar `ato-skill-po` cuando se necesite:

- construir memoria contextual de negocio,
- generar artefactos PO/TPO,
- documentar funcionalmente un producto,
- organizar conocimiento de negocio dentro del repo,
- convertir hallazgos en épicas/features/historias,
- generar planes de trabajo,
- estructurar releases o milestones,
- registrar supuestos, riesgos y decisiones,
- mantener trazabilidad funcional,
- crear documentación base de negocio,
- preparar contenido para ADO/Jira sin publicarlo directamente.

---

## 8. Cuándo No Usarlo

No usar `ato-skill-po` para:

- operar directamente Azure DevOps o Jira,
- modificar Work Items directamente,
- publicar historias directamente en herramientas externas,
- implementar código,
- diseñar infraestructura,
- ejecutar CI/CD,
- administrar permisos,
- decidir prioridades ejecutivas sin input humano,
- sustituir al Product Owner humano,
- crear decisiones de negocio no trazables,
- mutar memoria sin instrucción explícita.

---

## 9. Contexto Operativo del Skill

El skill debe conocer y exponer:

- nombre del skill,
- versión,
- baseline mode,
- propósito,
- capacidades,
- comandos,
- rutas de memoria,
- rutas de documentación,
- rutas de exportación,
- objetos PO/TPO soportados,
- estructura documental recomendada,
- fuentes de contexto disponibles,
- skills externos configurables,
- plantillas disponibles,
- formatos de salida,
- reglas de memoria,
- reglas de seguridad,
- límites de uso,
- códigos de salida,
- validaciones disponibles.

---

## 10. Contexto del Repositorio Asistido

El repositorio donde el skill asiste puede no ser el mismo repositorio donde vive el código del skill.

Se deben diferenciar:

| Concepto | Significado |
|---|---|
| Skill repo project | Repositorio que implementa `ato-skill-po` |
| Assisted repo/project | Repositorio/proyecto donde el skill genera memoria, documentación y artefactos |
| Business documentation repo | Estructura local de documentación de negocio generada o adoptada |
| External source project | Proyecto externo consultado por skills auxiliares, por ejemplo ADO/Jira |

El skill debe operar principalmente sobre el **assisted repo/project**.

---

## 11. Estructura Recomendada del Repositorio del Skill

```txt
repo/
  AGENTS.md
  README.md
  SKILL.md
  CHANGELOG.md
  Makefile
  .env.example
  config.example.yaml
  .gitignore

  docs/
    architecture.md
    activation.md
    cli.md
    validation.md
    security.md
    configuration.md
    context-discovery.md
    scope-governance.md
    memory-model.md
    product-model.md
    tpo-engine.md
    documentation-scaffolding.md
    external-skills.md
    mcp-bridge.md

  cli/
    README.md
    ato_skill_po/

  bin/
    ato-skill-po

  scripts/
    install.sh
    bootstrap.sh
    validate.sh
    doctor.sh

  domains/
    epics/
    features/
    stories/
    acceptance/
    planning/
    roadmap/
    releases/
    milestones/
    bounded-contexts/
    traceability/
    product-docs/

  templates/
    markdown/
      epic.md.j2
      feature.md.j2
      user-story.md.j2
      acceptance-criteria.md.j2
      work-plan.md.j2
      product-wiki.md.j2
      roadmap.md.j2
      release.md.j2
      milestone.md.j2
      bounded-context.md.j2
      business-doc-index.md.j2
    json/
      manifest.json.j2
      traceability.json.j2
      product-object.json.j2

  contracts/
    input.schema.json
    output.schema.json
    context.schema.json
    capabilities.schema.json
    product-object.schema.json
    memory-entry.schema.json
    scaffold.schema.json
    manifest.schema.json

  examples/
    invocation.md
    natural-language.md
    machine-cli.md
    context-discovery.md
    memory.md
    scaffolding.md
    epics.md
    features.md
    stories.md
    inputs/
    outputs/

  memory/
    knowledge.md
    decisions.md
    iteration-history.md
    terminology-es.md
    product/
      context.md
      glossary.md
      stakeholders.md
      business-rules.md
      assumptions.md
      open-questions.md
      decisions.md
      risks.md
      roadmap.md
      releases.md
      milestones.md
      bounded-contexts.md
      dependencies.md
      traceability.md
      documentation-structure.md
      iteration-history.md
      append-log/
        .gitkeep
      snapshots/
        .gitkeep
      manifests/
        .gitkeep

  harnesses/
    restrictions.md
    behavior-limits.md
    safety-rules.md
    acceptance-checks.md
    memory-guardrails.md
    scaffolding-guardrails.md

  workspace/
    po/
      staging/
        .gitkeep
      manifests/
        .gitkeep
      doctor/
        .gitkeep
      sessions/
        .gitkeep

  exports/
    po/
      epics/
        .gitkeep
      features/
        .gitkeep
      stories/
        .gitkeep
      plans/
        .gitkeep
      wikis/
        .gitkeep
      scaffolds/
        .gitkeep
      bundles/
        .gitkeep

  logs/
    po/
      .gitkeep

  tmp/
    po/
      .gitkeep

  .github/
    copilot-instructions.md

  .agents/
    skills/
      ato-skill-po/
        SKILL.md
        scripts/
        examples/
```

---

## 12. Estructura Recomendada para el Proyecto Asistido

Cuando el usuario pida generar una estructura base de documentación de negocio, el skill puede proponer o materializar una estructura local como:

```txt
docs/
  business/
    README.md
    product-context.md
    glossary.md
    stakeholders.md
    business-rules.md
    assumptions.md
    open-questions.md
    decisions.md
    risks.md

    domains/
      README.md
      <domain-name>/
        overview.md
        bounded-context.md
        business-capabilities.md
        rules.md
        dependencies.md
        traceability.md

    roadmap/
      README.md
      roadmap.md
      releases.md
      milestones.md

    discovery/
      README.md
      interviews.md
      findings.md
      opportunities.md

    requirements/
      README.md
      epics/
      features/
      user-stories/

    planning/
      README.md
      work-plan.md
      phases.md
      backlog-slicing.md

    wiki/
      README.md
      product-wiki.md

    traceability/
      README.md
      product-traceability.md
      source-map.json

    manifests/
      scaffold-manifest.json
```

---

## 13. Estrategias de Scaffolding Documental

El skill debe soportar distintas estrategias de generación de estructura documental.

### 13.1 Por Fases

```txt
docs/business/
  phases/
    00-discovery/
    01-mvp/
    02-growth/
    03-scale/
```

### 13.2 Por Historia

```txt
docs/business/
  requirements/
    user-stories/
      US-0001/
        story.md
        acceptance-criteria.md
        notes.md
        traceability.json
```

### 13.3 Por Dominio

```txt
docs/business/
  domains/
    payments/
      overview.md
      bounded-context.md
      business-rules.md
      features.md
      stories.md
      traceability.md
```

### 13.4 Por Producto

```txt
docs/business/
  product/
    vision.md
    goals.md
    roadmap.md
    releases.md
    stakeholders.md
    metrics.md
```

### 13.5 Mixta

El skill puede proponer una estructura híbrida, pero debe registrar:

- estrategia seleccionada,
- motivo,
- impacto,
- rutas creadas,
- artefactos generados,
- manifiesto JSON,
- relación con memoria contextual.

---

## 14. Regla de Coherencia Longitudinal

El skill debe mantener coherencia de capacidades y referencias para no perderse en el tiempo.

Regla:

```txt
Toda generación, adopción o cambio de estructura documental debe quedar referenciada en la memoria contextual, en un manifiesto JSON y en el historial de iteraciones.
```

Esto aplica a:

- nuevas épicas,
- nuevas features,
- nuevas historias,
- cambios de estructura documental,
- generación de wikis,
- adopción de recomendaciones,
- reorganización por fases,
- reorganización por dominio,
- snapshots de memoria,
- consolidaciones explícitas.

---

## 15. Requisitos Fundacionales No Negociables

1. Deben existir manifiestos y documentación raíz.
2. Debe existir `SKILL.md` con frontmatter `name` y `description`.
3. El comando clave de activación es `@po`.
4. El binario principal es `ato-skill-po`.
5. La CLI es obligatoria y es el núcleo operativo.
6. El modo principal es local-first.
7. El skill genera contenido, no opera plataformas externas directamente.
8. Las integraciones ADO/Jira se delegan a otros skills.
9. La memoria contextual de negocio es local al proyecto asistido.
10. La memoria es append-only por defecto.
11. La memoria solo se resume, copia, consolida o muta bajo instrucción explícita.
12. Todo cambio importante en memoria genera manifiesto JSON.
13. Todo artefacto generado debe referenciar sus fuentes de contexto cuando existan.
14. Toda estructura documental generada debe tener manifiesto.
15. El skill debe soportar modo exploratorio y modo determinista.
16. El skill debe generar Markdown como formato primario.
17. El skill debe generar JSON manifests como formato máquina.
18. No debe decidir prioridades finales sin input humano.
19. No debe publicar directamente en ADO/Jira en v0.1.
20. No debe diseñar arquitectura técnica profunda.
21. No debe implementar código de aplicación.
22. Deben existir plantillas versionables.
23. Deben existir harnesses de restricciones y comportamiento.
24. Debe existir `doctor`.
25. Debe existir `validate`.
26. Debe existir `context`.
27. Debe existir `capabilities`.
28. Debe existir `scaffold` para documentación de negocio.
29. Debe mantener coherencia longitudinal de referencias.
30. Las decisiones de alcance deben quedar registradas.

---

## 16. Matriz de Alcance por Versión

### P0 — Obligatorio para v0.1

| Área | Alcance |
|---|---|
| CLI | `ato-skill-po` |
| Activación | `@po` y lenguaje natural equivalente |
| Stack | Python |
| Memoria | local, contextual, append-only |
| Modos | exploratorio y determinista |
| Artefactos | épicas, features, historias, criterios de aceptación, planes, wikis |
| TPO | roadmap, releases, milestones, dependencias, bounded contexts |
| Documentación negocio | scaffold base y estrategias por dominio/fase/historia/producto |
| Export | Markdown + JSON manifests |
| Context discovery | `context`, `capabilities`, `usage`, `examples`, `schema` |
| Diagnóstico | `doctor` |
| Validación | `validate` |
| Workspace | `workspace/po/` |
| Export nativo | `exports/po/` |
| Logs | `logs/po/` |
| Temporales | `tmp/po/` |
| Seguridad | sin mutación de memoria sin instrucción explícita |
| Harnesses | memoria, scaffolding, límites, aceptación |
| Integración externa | referencia documental a `ato-skill-ado-cli` |
| Publicación externa | fuera de alcance |

### P1 — Recomendado para evolución cercana

| Área | Alcance |
|---|---|
| ADO delegated adapter | invocación real de `ato-skill-ado-cli` |
| Import de contexto ADO | consumir exports Markdown/JSON de ADO |
| Bundles | paquetes listos para publicación externa |
| Plantillas avanzadas | por organización, dominio, historia, release |
| Trazabilidad | matrices avanzadas |
| Roadmap | planificación por releases/milestones |
| Jira delegated adapter | referencia preparatoria |

### P2 — Interoperabilidad avanzada

| Área | Alcance |
|---|---|
| MCP | bridge funcional |
| HTTPS | mini-servidor local |
| Skills externos | invocación MCP real |
| Sincronización | publicación controlada hacia ADO/Jira mediante skills |
| Schemas avanzados | contratos multi-skill |
| Governance | aprobaciones y políticas más formales |

### P3 — Distribución y madurez

| Área | Alcance |
|---|---|
| Homebrew | fórmula publicada |
| CI/CD | pipeline completo |
| Catálogo | publicación en catálogo interno |
| Hardening | seguridad y compliance |
| Multi-template packs | paquetes de plantillas por industria |
| Product operating model | madurez organizacional |

---

## 17. Decisiones Explícitas sobre HTTPS, Servicios Externos y MCP

### HTTPS

```txt
Decisión v0.1: No incluido.
Motivo: el skill debe estabilizar primero su contrato CLI, memoria contextual y generación de artefactos.
```

### Servicios Externos

```txt
Decisión v0.1: No operar APIs externas directamente.
El skill puede apoyarse en otros skills CLI/MCP especializados.
```

### Azure DevOps

```txt
Decisión v0.1: Integración delegada a ato-skill-ado-cli.
Referencia recomendada: https://github.com/AkimboTheOne/ia_ato-skill-ado-cli
```

### Jira

```txt
Decisión v0.1: Diferido hasta existir skill dedicado.
```

### MCP

```txt
Decisión v0.1: Referenciado para evolución futura.
No se implementa bridge MCP funcional.
Se debe conservar estructura documental para no bloquear evolución.
```

---

## 18. Decisiones Fuera de Alcance para v0.1

Queda fuera de alcance:

- operar directamente Azure DevOps,
- operar directamente Jira,
- publicar historias automáticamente en herramientas externas,
- mini-servidor HTTPS,
- bridge MCP funcional,
- UI web,
- agentes autónomos,
- priorización ejecutiva final,
- scoring automático de roadmap sin input humano,
- arquitectura técnica profunda,
- implementación de código,
- administración de backlog externo,
- sincronización bidireccional,
- mutación automática de memoria,
- borrado automático de memoria,
- generación de decisiones no trazables,
- multiusuario,
- ejecución remota,
- scheduler interno.

---

## 19. Arquitectura Técnica Mínima

### 19.1 Documentation Layer

Contiene:

- `README.md`
- `SKILL.md`
- `AGENTS.md`
- `CHANGELOG.md`
- `docs/`

### 19.2 Execution Layer

Contiene:

- `cli/`
- `bin/`
- `scripts/`
- `Makefile`

Responsabilidades:

- ejecutar CLI,
- validar contexto,
- cargar memoria,
- aplicar plantillas,
- generar artefactos,
- producir manifests,
- validar estructura,
- registrar logs.

### 19.3 Memory Layer

Contiene:

- memoria de negocio,
- append-log,
- snapshots,
- manifests de cambios,
- decisiones,
- glosario,
- reglas,
- riesgos,
- trazabilidad.

### 19.4 Product Definition Layer

Contiene:

- modelos de épica,
- feature,
- historia,
- criterios,
- roadmap,
- release,
- milestone,
- bounded context,
- plan de trabajo,
- wiki.

### 19.5 External Skill Service Layer

En v0.1 principalmente documental.

Responsabilidades:

- declarar integración delegada con otros skills,
- definir contratos esperados,
- permitir evolución a invocación real en P1/P2.

### 19.6 Compatibility Layer

En v0.1 solo documental:

- `docs/mcp-bridge.md`
- contratos JSON,
- schemas.

No debe implementar servidor ni MCP funcional.

---

## 20. Interfaz CLI Dual Humano/Máquina

### 20.1 Comandos Base

```bash
ato-skill-po init
ato-skill-po config init
ato-skill-po doctor
ato-skill-po validate
ato-skill-po context
ato-skill-po capabilities
ato-skill-po usage
ato-skill-po examples
ato-skill-po schema
ato-skill-po version
ato-skill-po logs
```

### 20.2 Memoria

```bash
ato-skill-po memory init
ato-skill-po memory append --type decision --file input.md
ato-skill-po memory append --type context --text "Nuevo contexto..."
ato-skill-po memory snapshot
ato-skill-po memory summarize --explicit --out memory/product/snapshots/
ato-skill-po memory consolidate --explicit --out memory/product/consolidated/
```

### 20.3 Exploración

```bash
ato-skill-po explore "Necesito definir el módulo de onboarding"
ato-skill-po discover domain --name payments
ato-skill-po refine feature --input examples/features.md
```

### 20.4 Generación Determinista

```bash
ato-skill-po generate epic --title "Autenticación empresarial" --out exports/po/epics/
ato-skill-po generate feature --from memory/product/context.md --out exports/po/features/
ato-skill-po generate story --input examples/story.input.json --out exports/po/stories/
ato-skill-po generate work-plan --from exports/po/features/ --out exports/po/plans/
ato-skill-po generate wiki --domain payments --out exports/po/wikis/
```

### 20.5 Scaffolding Documental

```bash
ato-skill-po scaffold business-docs --strategy default --out docs/business/
ato-skill-po scaffold business-docs --strategy domain --domain payments --out docs/business/
ato-skill-po scaffold business-docs --strategy phase --out docs/business/
ato-skill-po scaffold business-docs --strategy story --story-id US-0001 --out docs/business/
```

### 20.6 External Skills

```bash
ato-skill-po external-skills list
ato-skill-po external-skills describe ado
ato-skill-po external-skills import ado-export --input exports/ado/bundles/context.json
```

---

## 21. Contexto de Uso Expuesto por CLI

`ato-skill-po context` debe exponer:

- propósito,
- versión,
- baseline mode,
- rutas de memoria,
- política de memoria,
- capacidades disponibles,
- objetos PO/TPO soportados,
- estrategias de scaffolding,
- estructura documental recomendada,
- comandos disponibles,
- plantillas disponibles,
- rutas de workspace,
- rutas de export,
- fuentes externas configurables,
- skills externos conocidos,
- reglas de seguridad,
- restricciones de comportamiento,
- validaciones disponibles,
- códigos de salida.

Ejemplo:

```bash
ato-skill-po context --json
```

Debe devolver JSON válido.

---

## 22. Modelo de Memoria Contextual

### 22.1 Principio

```txt
La memoria contextual de negocio es local al proyecto asistido y append-only por defecto.
```

### 22.2 Estructura Recomendada

```txt
memory/
  terminology-es.md
  knowledge.md
  decisions.md
  iteration-history.md
  product/
    context.md
    glossary.md
    stakeholders.md
    business-rules.md
    assumptions.md
    open-questions.md
    decisions.md
    risks.md
    roadmap.md
    releases.md
    milestones.md
    bounded-contexts.md
    dependencies.md
    traceability.md
    documentation-structure.md
    iteration-history.md

    append-log/
      0001-initial-context.md
      0002-discovery-session.md
      0003-roadmap-refinement.md

    snapshots/
      product-context-YYYYMMDD.md

    manifests/
      memory-change-YYYYMMDD-HHMMSS.json
```

### 22.3 Mutaciones Permitidas

Solo bajo instrucción explícita:

- resumir,
- copiar,
- consolidar,
- versionar,
- crear snapshot,
- crear memoria derivada,
- marcar sección como obsoleta,
- migrar estructura.

### 22.4 Mutaciones Prohibidas por Defecto

- borrar memoria,
- reescribir decisiones,
- compactar automáticamente,
- sustituir contexto original,
- eliminar trazabilidad,
- mutar memoria sin manifiesto.

---

## 23. Modelo de Objetos PO/TPO

El skill debe manejar múltiples tipos de objeto, cada uno con contrato propio.

### Objetos P0

| Objeto | Descripción |
|---|---|
| `business-context` | Contexto general de negocio |
| `domain` | Dominio funcional o área de negocio |
| `bounded-context` | Contexto delimitado para análisis TPO |
| `stakeholder` | Actor interesado |
| `business-rule` | Regla de negocio |
| `assumption` | Supuesto |
| `open-question` | Pregunta pendiente |
| `decision` | Decisión registrada |
| `risk` | Riesgo de producto |
| `roadmap` | Mapa de evolución |
| `release` | Liberación planeada |
| `milestone` | Hito |
| `dependency` | Dependencia funcional/técnica |
| `epic` | Épica |
| `feature` | Feature |
| `user-story` | Historia de usuario |
| `acceptance-criteria` | Criterios de aceptación |
| `work-plan` | Plan de trabajo |
| `product-wiki` | Documentación funcional |
| `traceability-map` | Mapa de trazabilidad |
| `documentation-scaffold` | Estructura documental de negocio |

---

## 24. Procedimiento Operativo

### 24.1 Primer Uso

```bash
make install
make bootstrap
ato-skill-po config init
ato-skill-po doctor
ato-skill-po context
```

### 24.2 Inicializar Memoria

```bash
ato-skill-po memory init
ato-skill-po memory append --type context --text "Contexto inicial del producto..."
```

### 24.3 Crear Estructura Documental Base

```bash
ato-skill-po scaffold business-docs --strategy default --out docs/business/
```

Debe generar:

- carpetas,
- archivos Markdown,
- manifiesto JSON,
- entrada en memoria,
- registro de decisión,
- trazabilidad de rutas.

### 24.4 Generar Artefactos PO/TPO

```bash
ato-skill-po generate epic --from memory/product/context.md
ato-skill-po generate feature --from exports/po/epics/
ato-skill-po generate story --from exports/po/features/
ato-skill-po generate work-plan --from exports/po/stories/
```

### 24.5 Importar Contexto ADO Delegado

```bash
ato-skill-po external-skills import ado-export --input exports/ado/bundles/context.json
```

---

## 25. Validaciones Verificables

### Comandos

```bash
make validate
make test
make doctor
ato-skill-po validate
ato-skill-po doctor
ato-skill-po doctor --ci --json
```

### Validaciones Esperadas

- JSON válido,
- Markdown generado,
- manifests presentes,
- memoria append-only respetada,
- no mutación sin instrucción explícita,
- estructura documental consistente,
- referencias cruzadas válidas,
- rutas creadas bajo workspace autorizado,
- objetos generados con metadata,
- plantillas válidas,
- ausencia de secretos,
- capacidades expuestas por CLI.

### Códigos de Salida

| Código | Significado |
|---|---|
| `0` | Éxito |
| `1` | Error general |
| `2` | Configuración inválida |
| `3` | Memoria no inicializada |
| `4` | Fuente de contexto inválida |
| `5` | Objeto PO/TPO inválido |
| `6` | Error de validación |
| `7` | Mutación de memoria bloqueada |
| `8` | Skill externo no disponible |
| `9` | Contrato de salida inválido |

---

## 26. Reglas de Seguridad y Gobernanza

1. No operar directamente ADO/Jira.
2. No publicar objetos externos en v0.1.
3. No mutar memoria sin instrucción explícita.
4. No borrar memoria.
5. No reescribir decisiones sin snapshot.
6. No ocultar supuestos.
7. No inventar fuentes.
8. No generar prioridades finales sin input humano.
9. No convertir exploración en decisión final.
10. No mezclar diseño técnico profundo con definición PO/TPO.
11. No escribir fuera del workspace o salida autorizada.
12. No ejecutar shell arbitrario.
13. No exponer secretos.
14. Todo artefacto generado debe tener metadata.
15. Toda estructura documental creada debe tener manifiesto.
16. Toda recomendación de estructura debe registrar motivo.
17. Toda adopción de estructura debe registrar decisión.
18. Todo cambio longitudinal debe actualizar memoria.
19. Todo uso de skill externo debe registrar fuente.
20. El usuario humano conserva decisión final.

---

## 27. Dependencias e Instalación Cross-platform

### Dependencias Base

- Python 3.11+
- `pipx` recomendado para instalación CLI
- `venv` soportado
- `make`
- `jq` opcional para pruebas JSON

### Instalación Recomendada

```bash
make install
make bootstrap
```

### Instalación Manual

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
ato-skill-po doctor
```

### Homebrew

Para v0.1 solo documentar posibilidad futura:

```bash
brew install ato-skill-po
```

No publicar fórmula en v0.1.

---

## 28. Variables de Entorno y Configuración

### `.env.example`

```bash
ATO_SKILL_PO_DEFAULT_OUTPUT=md
ATO_SKILL_PO_WORKSPACE_DIR=workspace/po
ATO_SKILL_PO_EXPORT_DIR=exports/po
ATO_SKILL_PO_LOG_DIR=logs/po
ATO_SKILL_PO_TMP_DIR=tmp/po

ATO_SKILL_PO_MEMORY_DIR=memory/product
ATO_SKILL_PO_DOCS_DIR=docs/business
ATO_SKILL_PO_APPEND_ONLY_MEMORY=true
ATO_SKILL_PO_REQUIRE_EXPLICIT_MEMORY_MUTATION=true

ATO_SKILL_PO_LOG_LEVEL=info
ATO_SKILL_PO_MAX_CONTEXT_FILES=100
ATO_SKILL_PO_MAX_GENERATED_OBJECTS=50

ATO_SKILL_PO_ADO_SKILL_BIN=ato-skill-ado-cli
ATO_SKILL_PO_JIRA_SKILL_BIN=
```

### `config.example.yaml`

```yaml
defaults:
  output: "md"
  workspace_dir: "workspace/po"
  export_dir: "exports/po"
  log_dir: "logs/po"
  tmp_dir: "tmp/po"
  docs_dir: "docs/business"

memory:
  dir: "memory/product"
  append_only: true
  require_explicit_mutation: true
  snapshots_dir: "memory/product/snapshots"
  manifests_dir: "memory/product/manifests"

product_model:
  supported_objects:
    - business-context
    - domain
    - bounded-context
    - stakeholder
    - business-rule
    - assumption
    - open-question
    - decision
    - risk
    - roadmap
    - release
    - milestone
    - dependency
    - epic
    - feature
    - user-story
    - acceptance-criteria
    - work-plan
    - product-wiki
    - traceability-map
    - documentation-scaffold

scaffolding:
  default_strategy: "default"
  allowed_strategies:
    - default
    - phase
    - story
    - domain
    - product
    - mixed

external_skills:
  azure_devops:
    enabled: false
    bin: "ato-skill-ado-cli"
    mode: "delegated"
    reference: "https://github.com/AkimboTheOne/ia_ato-skill-ado-cli"
  jira:
    enabled: false
    bin: ""
    mode: "future"
```

---

## 29. Logs, Temporales y Trazabilidad

### Rutas

```txt
logs/po/
tmp/po/
workspace/po/sessions/
workspace/po/manifests/
workspace/po/doctor/
exports/po/
memory/product/manifests/
```

### Reglas

- Los logs no deben contener secretos.
- Cada generación debe producir manifiesto JSON.
- Cada scaffold debe producir manifiesto JSON.
- Cada mutación explícita de memoria debe producir manifiesto JSON.
- Cada uso de skill externo debe registrar fuente.
- Los temporales deben poder limpiarse sin romper memoria ni exports permanentes.

---

## 30. Plantillas Example

### Historia de Usuario

```md
# User Story — {{ title }}

| Campo | Valor |
|---|---|
| ID | {{ id }} |
| Dominio | {{ domain }} |
| Feature | {{ feature }} |
| Prioridad sugerida | {{ priority_suggestion }} |
| Fuente de contexto | {{ context_sources }} |

## Historia

Como {{ persona }},
quiero {{ capability }},
para {{ business_outcome }}.

## Criterios de Aceptación

{{ acceptance_criteria }}

## Reglas de Negocio

{{ business_rules }}

## Supuestos

{{ assumptions }}

## Preguntas Abiertas

{{ open_questions }}

## Trazabilidad

{{ traceability }}

## Metadatos

- Generado por: `ato-skill-po`
- Versión baseline: `v0.1`
- Manifiesto: `{{ manifest_path }}`
```

### Documentation Scaffold Manifest

```json
{
  "skill": "ato-skill-po",
  "baseline_version": "v0.1",
  "operation": "scaffold",
  "strategy": "",
  "target_path": "",
  "created_paths": [],
  "product_objects": [],
  "memory_references": [],
  "decisions_recorded": [],
  "warnings": [],
  "errors": [],
  "created_at": ""
}
```

---

## 31. Reglas de `.gitignore`

Debe excluir:

```gitignore
# Logs and temporary files
logs/*
tmp/*
workspace/po/staging/*
workspace/po/doctor/*
workspace/po/sessions/*

# Local secrets and config
.env
.env.local
.env.*.local
config.yaml
config.local.yaml
*.local.yaml
*.local.json

# Generated temporary outputs
*.log

# Python
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/
.venv/
venv/
dist/
build/
*.egg-info/

# Node or generic tooling if added later
node_modules/

# Cache
.cache/
```

Debe permitir conservar estructura y plantillas:

```gitignore
!logs/**/.gitkeep
!tmp/**/.gitkeep
!workspace/**/.gitkeep
!.env.example
!config.example.yaml
!exports/**/.gitkeep
```

Nota: `memory/product/` y `docs/business/` pueden ser versionables por decisión del proyecto asistido.

---

## 32. Historial de Iteraciones

### v0.1

| Campo | Valor |
|---|---|
| Versión | `v0.1` |
| Cambio | Creación de baseline fundacional |
| Motivo | Definir charter técnico y operativo para construir el repositorio del skill |
| Impacto esperado | Permitir implementación ordenada, verificable y evolutiva |
| Decisiones aceptadas | Python, `@po`, local-first, memoria append-only, PO/TPO engine acotado, Markdown + JSON |
| Decisiones aceptadas | Integración ADO delegada a `ato-skill-ado-cli`, Jira diferido, HTTPS/MCP no funcional |
| Decisiones diferidas | publicación externa, MCP funcional, HTTPS, Jira skill, sincronización bidireccional |
| Pendientes abiertos | definir librería CLI Python, definir motor de plantillas, definir estructura final de templates |

---

## 33. Próximos Pasos

1. Crear repositorio base.
2. Crear archivos raíz:
   - `README.md`
   - `SKILL.md`
   - `AGENTS.md`
   - `CHANGELOG.md`
3. Crear estructura de carpetas.
4. Implementar CLI mínima en Python.
5. Implementar `context`, `capabilities`, `doctor`, `validate`.
6. Implementar modelo de memoria append-only.
7. Implementar `memory init`, `memory append`, `memory snapshot`.
8. Implementar generación de épicas/features/historias.
9. Implementar scaffolding documental `docs/business/`.
10. Implementar manifests JSON.
11. Implementar plantillas Markdown.
12. Implementar harnesses de memoria y scaffolding.
13. Documentar integración delegada con `ato-skill-ado-cli`.
14. Ejecutar `make validate`.
15. Registrar primera iteración en `memory/iteration-history.md`.

---

## 34. Criterios de Aceptación v0.1

La baseline v0.1 se considera implementada cuando:

- `ato-skill-po doctor` valida estructura y configuración.
- `ato-skill-po context --json` devuelve JSON válido.
- `ato-skill-po capabilities --json` devuelve capacidades reales.
- `ato-skill-po memory init` crea memoria contextual local.
- `ato-skill-po memory append` agrega entradas sin sobrescribir memoria.
- `ato-skill-po scaffold business-docs` genera estructura documental.
- El scaffold genera manifiesto JSON.
- `ato-skill-po generate epic` genera Markdown válido.
- `ato-skill-po generate feature` genera Markdown válido.
- `ato-skill-po generate story` genera Markdown válido.
- Cada artefacto generado incluye metadata.
- Cada generación produce manifest JSON.
- La memoria no se muta sin instrucción explícita.
- La estructura documental conserva coherencia de referencias.
- `make validate` ejecuta validaciones estructurales.
- La documentación raíz permite a un agente constructor implementar el repositorio sin reinterpretar el alcance.

---

## 35. Síntesis Ejecutiva

`ato-skill-po` v0.1 será un skill Python CLI, local-first, activado por `@po`, especializado en Product Ownership y Technical Product Ownership.

Su responsabilidad será construir y mantener memoria contextual de negocio dentro del proyecto asistido y generar artefactos PO/TPO como épicas, features, historias, planes de trabajo, wikis funcionales y estructuras documentales de negocio.

El skill puede recomendar o generar estructuras base de documentación por producto, dominio, fase o historia, pero debe preservar coherencia longitudinal mediante memoria append-only, manifests JSON, trazabilidad y reglas explícitas de gobernanza.

No operará directamente Azure DevOps ni Jira en v0.1. Para ADO se apoyará en `ato-skill-ado-cli`; Jira queda diferido a un skill futuro. HTTPS y MCP funcional quedan fuera de alcance para evitar complejidad accidental.
