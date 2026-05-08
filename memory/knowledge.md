# Conocimiento

- `ato-skill-upgrade` es un skill de soporte para el agente principal de codificación.
- El skill ayuda a pensar, planificar y documentar; no sustituye la ejecución del agente principal.
- El modo `document` documenta únicamente cambios ejecutados o verificables.
- El onboarding local debe exponer un entrypoint raíz `./setup-skill.sh`.
- La instalación debe crear o reutilizar `.venv` y evitar escribir en Python global para prevenir fallos de PEP 668.
- Las dependencias de Python se declaran en `pyproject.toml`; los binarios y compiladores del sistema son prerrequisitos, no contenido del repositorio.
- `review external` debe operar en solo lectura y escribir sus salidas únicamente en el workspace activo.
- El análisis de madurez productiva usa puntuaciones por categoría en lugar de un checklist plano.
- `run --payload-file` es la superficie máquina para automatización repetible.
- Los fixtures sintéticos de skills son la forma preferida de probar sugerencias de madurez y feature sin depender de repos remotos.
- La auto-revisión solo se permite en dry-run y con profundidad máxima 1.
- Los reportes de external review cuentan como evidencia detectada para la reconciliación documental.
- El estado de madurez debe distinguir brechas menores de fallas materiales.
- La validación de schemas es liviana y sin dependencias en esta fase.
- `v0.8` introduce CI y validación de consistencia de versión.
- La preparación de release requiere `setup`, `validate`, tests, análisis de madurez, external review, changelog, memoria y metadatos de versión sincronizados.
