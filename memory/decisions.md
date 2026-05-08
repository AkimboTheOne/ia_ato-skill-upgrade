# Decisiones

- Usar `argparse` de la biblioteca estándar en el primer corte de implementación para no bloquearse por instalación de dependencias.
- Mantener `analyze`, `plan`, `charter` y `document change` en modo scaffold hasta que la lógica central quede implementada.
- Seguir el patrón local de instalación en `.venv` observado en `ia_ato-skill-ado-cli`.
- Añadir `setup-skill.sh` en la raíz como comando preferido de onboarding después del clone o download.
- Tratar la robustez de instalación como una preocupación de madurez: detectar prerrequisitos del host, instalar en `.venv` y no vendorizar binarios ni compiladores.
- Añadir `review external` como el primer camino productivo para evaluar otros skills sin modificarlos.
- Separar las recomendaciones de external review en sugerencias de madurez y sugerencias de feature.
- Añadir contratos `run` antes de profundizar en la reconciliación documental para que otros agentes puedan invocar operaciones estables.
- Mantener los sample skills locales y sintéticos para smoke tests deterministas.
- Bloquear operaciones de escritura durante la auto-revisión para evitar auto-modificación recursiva.
- Permitir que la reconciliación documental consuma reportes de external review como evidencia detectada.
- Mantener la validación de JSON Schema sin dependencias hasta que exista una justificación más fuerte para usar otra librería.
- Usar `ready-with-notes` para skills con score alto y brechas pequeñas de evidencia.
- Mover la versión de implementación a `0.8.0` después de agregar CI y governance de release.
- Mantener la CI mínima: `setup`, `validate` y tests.
- Usar el tag `v0.8.0` para la primera release sólida pre-productiva.
- Abrir PR hacia `master` para promoción trazable en lugar de merge directo.
