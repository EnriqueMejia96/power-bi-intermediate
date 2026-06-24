# Power BI + Analítica Empresarial Asistida por IA para Entornos Tech&Eng

Repositorio base del **Módulo 1: Arquitectura analítica y recap Power BI**. Prepara datos sintéticos, guías, plantillas, prompts y pruebas locales para una sesión intermedia de 2 horas orientada a profesionales Tech&Eng.

## Objetivo
Enseñar Power BI como ciclo analítico completo: problema de negocio -> datos -> Power Query -> modelo semántico -> DAX -> visuales -> hallazgos -> decisiones.

## Enfoque Tech&Eng minero
El caso del repositorio ahora representa una operación **Tech&Eng minero / industrial minero**. Mantiene la arquitectura didáctica original, pero los datos, preguntas, KPIs, prompts y wireframes usan procesos como mina rajo abierto, despacho mina, chancado, correas, molienda, flotación, relaves, mantenimiento, energía, HSE y automatización OT.

Esto no convierte la especialización en un curso exclusivamente minero: la minería funciona como contexto realista para aprender arquitectura Power BI, calidad de datos, modelo estrella, DAX, diseño de dashboards y analítica asistida por IA.

## Audiencia
Profesionales de ingeniería, operaciones, mantenimiento, servicios técnicos, supervisión, proyectos y análisis de negocio que ya conocen Power BI básico y necesitan diseñar soluciones BI con criterio arquitectónico.

## Alcance del Módulo 1
El módulo es un recap funcional y estratégico. No implementa tableros finales, no crea `.pbix`, no publica en Power BI Service y no depende de APIs externas.

## Qué aprenderá el estudiante
- Diferenciar Power Query, modelo, DAX y visualización.
- Convertir problemas operativos en preguntas medibles.
- Definir KPIs preliminares y audiencia del tablero.
- Crear un Diseño de solución BI inicial.
- Usar IA como apoyo de diseño sin delegar validación de negocio.

## Estructura de la especialización
1. Arquitectura analítica y recap Power BI.
2. Power Query y calidad de datos.
3. Modelamiento con modelo estrella.
4. DAX para KPIs de negocio.
5. Tableros y narrativa de datos.
6. Optimización, publicación y proyecto.
7. Proyecto final: Tablero Integral de Desempeño Tech&Eng.

## Dataset sintético integrado
El repositorio usa una estrategia unificada:

- **Dataset A (`data/training`)**: entrenamiento progresivo para sesiones 1-6, con foco en chancado, correas, taller mina, molienda, consumo energético y backlog.
- **Dataset B (`data/project`)**: proyecto final con el mismo esquema, valores diferentes y patrones distintos en dispatch, relaves, molienda, flota mina y OT.

Ambos datasets son 100% sintéticos, comparten el mismo schema y mantienen carpetas `raw`, `clean`, `dictionary`, `metadata` y, para entrenamiento, `sample`.

## Uso local
1. Crear ambiente Python opcional: `python -m venv .venv`.
2. Instalar dependencias: `python -m pip install -r requirements.txt`.
3. Generar datos mineros: `python scripts/python/generate_data.py --dataset all`.
4. Validar datos: `python scripts/python/validate_data.py --dataset all`.
5. Generar diccionario: `python scripts/python/generate_dictionary.py --dataset all`.
6. Perfilar datos: `python scripts/python/profile_data.py --dataset all`.
7. Ejecutar pruebas: `python -m pytest`.

Si `make` está disponible, el flujo recomendado es:

```bash
make setup
make check-env
make data-mining
make validate-data
make validate-mining
make data-dictionary
make profile-data
make profile-mining
make mining-report
make session01-materials
make test
```

Los reportes mineros quedan en `reports/dataset_profile/` y `reports/session_01/`.

## Power BI Desktop
Power BI Desktop se usa manualmente. Las guías en `powerbi/manual_steps` explican cómo importar CSV, reconocer Power Query, revisar Vista de modelo y crear visuales básicos. El repositorio no genera archivos `.pbix`.

## IA asistida
Los prompts en `ai_tools/` y `session_01/prompts/` sirven para diseñar preguntas, KPIs, bocetos y validaciones. No se llama ninguna API de IA desde el código. No subas datos reales, contratos, clientes ni personas reales a herramientas externas.

## Cobertura minera esperada
- Dimensiones con vocabulario de mina, planta, relaves, HSE, energía, mantenimiento y OT.
- Hechos con patrones de productividad, backlog, SLA, downtime, costos, energía, incidentes y proyectos mineros.
- Diccionario con definiciones por campo, interpretación de KPIs, ejemplos y notas raw vs clean.
- Wireframes y backlog DAX preparados para tableros ejecutivos, operaciones, mantenimiento, SLA/backlog, energía, seguridad y causa raíz.

## Estado actual
- Repositorio base del Módulo 1 preparado.
- Dataset A minero implementado con datos crudos (`raw`), datos limpios (`clean`), muestras (`sample`), metadatos y diccionario.
- Dataset B minero implementado con mismo esquema y patrones distintos.
- Implementación Power BI manual.
- Módulos 2-6 pendientes.

## Próximos pasos
Prompt 2 debería profundizar en Power Query y calidad de datos usando `data/training/raw`, sin cambiar el esquema base ni crear un dataset nuevo por sesión.

Queda pendiente para módulos posteriores implementar medidas DAX definitivas, diseñar páginas Power BI en Desktop y preparar la publicación gobernada. Este repositorio no crea `.pbix` ni publica en Power BI Service.
