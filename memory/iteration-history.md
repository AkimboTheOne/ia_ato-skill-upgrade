# Historial de Iteraciones

## 0.2.0 Scaffold

Se creó la estructura baseline del repositorio y el scaffold de CLI a partir del documento de requisitos v0.2.

## 0.2.0 Actualización de Madurez de Local Setup

Se actualizó el onboarding tomando como referencia la mejora de setup de `ia_ato-skill-ado-cli`:

- `setup-skill.sh` en la raíz,
- ruta de instalación exclusiva en `.venv`,
- validación de prerrequisitos del host,
- evitación de PEP 668,
- frontera explícita entre dependencias Python y binarios del sistema.

## 0.3.0 Corte de External Review

- Se añadió external review de solo lectura para repos locales de skills.
- Se añadieron read manifests para los archivos observados durante la revisión.
- Se añadió scoring de madurez por categoría.
- Se separaron las recomendaciones en salidas de madurez y de feature.

## 0.4.0 Corte de Run Contract y Fixtures

- Se añadió `run --payload-file`.
- Se añadieron schemas de request y response para invocación máquina.
- Se añadieron fixtures sintéticos para repos maduros, con setup débil y con scope inflado.
- Se añadieron tests para payloads de `run` y brechas de madurez basadas en fixtures.

## 0.5.0 Corte de Self Review y Document Reconciler

- Se añadió la entrada `--review-report` como evidencia para `document change`.
- Se añadieron guardrails de auto-revisión.
- Se bloquearon las escrituras durante la auto-revisión.
- Se limitó la profundidad recursiva de auto-revisión a 1.

## 0.7.0 Corte de Validación y Scoring

- Se añadió validación ligera de contratos.
- Se añadieron estados de madurez más expresivos.
- Se completaron los ejemplos de fixture maduro para smoke tests más limpios.

## 0.8.0 Corte de CI y Release Governance

- Se añadió CI de GitHub Actions.
- Se añadió documentación de release governance.
- Se sincronizó el metadato de versión.
- Se añadió validación de versión.

## 0.8.0 Preparación de Release

- Se añadieron release notes.
- Se preparó la promoción estable hacia `master`.
- Se planificó el tag de versión `v0.8.0`.
