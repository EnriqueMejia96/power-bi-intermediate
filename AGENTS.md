# AGENTS.md

## Alcance
Este repositorio soporta el Módulo 1 de la especialización Power BI + Analítica Empresarial Asistida por IA para Entornos Tech&Eng. Todo el trabajo debe ocurrir dentro de `power-bi-intermediate`.

## Restricciones no negociables
- No crear, modificar, mover ni eliminar archivos fuera de `power-bi-intermediate`.
- No mover ni renombrar el PDF fuente ubicado en `docs/`.
- No usar datos reales, credenciales, secretos ni información confidencial.
- No llamar APIs externas de IA ni servicios cloud.
- No crear archivos `.pbix` ni `.pbit`.
- No asumir Power BI Desktop instalado.
- No publicar en Power BI Service.

## Seguridad y privacidad
Todo dataset debe ser sintético. Los prompts de IA deben advertir que no se debe subir información sensible. Cualquier recomendación de IA debe validarse por criterio humano, negocio y pruebas.

## Dataset sintético
- Dataset A vive en `data/training` y se usa en sesiones 1-6.
- Dataset B vive en `data/project` y conserva el mismo esquema para el proyecto final.
- `raw` contiene problemas controlados; `clean` contiene tablas listas para modelamiento.
- No crear datasets independientes por sesión.

## Estructura y convenciones
- Tablas de hechos: prefijo `Fact_`.
- Tablas de dimensiones: prefijo `Dim_`.
- IDs consistentes: `AreaID`, `EquipmentID`, `ProjectID`, etc.
- CSV en UTF-8, separador coma, cabeceras estables, nombres de columnas en inglés técnico.
- Documentación en español profesional.
- Material de instructor en `session_01/instructor`; material de estudiante en `session_01/student`.

## Python
- Usar type hints y funciones pequeñas.
- Leer configuración desde `.env` si existe, con defaults razonables.
- No hardcodear rutas absolutas ni credenciales.
- Mantener generación reproducible con `RANDOM_SEED`.
- Validar esquema, llaves primarias, relaciones y fechas.

## Tests
Las pruebas no deben requerir internet, Power BI Desktop, credenciales ni servicios externos. Deben cubrir estructura, configuración, generación, esquema, integridad referencial, diccionario, materiales y Makefile.

## Makefile
Los objetivos deben ser seguros y locales. `reset-data` solo debe ejecutarse si `OVERWRITE_DATA=true` o si hay confirmación explícita equivalente en configuración.

## Continuidad
Los módulos 2-6 deben extender esta base sin implementar contenido futuro de forma anticipada. Cualquier ampliación debe preservar el flujo: problema -> datos -> Power Query -> modelo -> DAX -> visuales -> hallazgos -> decisiones.

## Criterios antes de finalizar
- Confirmar que no se trabajó fuera de `power-bi-intermediate`.
- Confirmar que el PDF no se movió ni renombró.
- Ejecutar generación y validaciones locales cuando sea posible.
- Documentar limitaciones, decisiones abiertas y pendientes para Prompt 2.
