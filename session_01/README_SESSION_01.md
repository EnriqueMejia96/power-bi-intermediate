# Módulo 1: Arquitectura analítica y recap Power BI

Este módulo es la puerta de entrada a la especialización **Power BI + Analítica Empresarial Asistida por IA para Entornos Tech&Eng**. No busca enseñar Power BI desde cero ni construir un tablero final. Su objetivo es que el estudiante piense como diseñador de soluciones analíticas: antes de crear visuales, debe entender la decisión, la audiencia, el dato, el modelo y el KPI.

## Resultado de aprendizaje
Al finalizar la sesión, el estudiante debe poder explicar y aplicar el ciclo:

`problema de negocio -> fuentes de datos -> Power Query -> modelo semántico -> DAX -> visuales -> hallazgos -> decisiones`

También debe entregar un **Diseño de solución BI inicial** para un caso Tech&Eng usando el dataset sintético del repositorio.

## Qué se ejecuta antes del laboratorio
Desde la raíz `power-bi-intermediate`:

```bash
python scripts/python/generate_data.py --dataset all
python scripts/python/validate_data.py --dataset all
python scripts/python/generate_dictionary.py --dataset all
python scripts/python/profile_data.py --dataset all
```

Si esos comandos ya devolvieron `training: OK` y `project: OK`, el laboratorio puede comenzar.

## Archivos clave para la sesión
- Dataset de trabajo rápido: `data/training/sample`.
- Dataset limpio completo: `data/training/clean`.
- Dataset crudo (`raw`) para observar problemas futuros: `data/training/raw`.
- Diccionario de datos: `data/training/dictionary/data_dictionary.md`.
- Guía de laboratorio: `session_01/lab/LAB_GUIDE.md`.
- Pasos detallados: `session_01/lab/LAB_STEPS.md`.
- Plantilla principal: `session_01/templates/BI_SOLUTION_BLUEPRINT_TEMPLATE.md`.
- Guías Power BI manuales: `powerbi/manual_steps/`.

## Secuencia recomendada de lectura
Usa este orden si necesitas completar el laboratorio de forma guiada, conectando problema de negocio, pregunta medible, KPI conceptual, datos requeridos, Power Query, DAX y visuales.

| Orden | Archivo | Para qué leerlo |
|---:|---|---|
| 1 | `session_01/README_SESSION_01.md` | Entender el objetivo del módulo y el ciclo analítico completo. |
| 2 | `session_01/lab/START_HERE_AFTER_DATA_GENERATION.md` | Confirmar el punto de partida después de generar datos. |
| 3 | `session_01/lab/LAB_GUIDE.md` | Revisar el caso, actividades y entregable esperado. |
| 4 | `session_01/lab/LAB_STEPS.md` | Seguir la ejecución detallada del laboratorio. |
| 5 | `data/training/metadata/business_scenario.md` | Identificar el problema de negocio y contexto operativo. |
| 6 | `session_01/lab/BUSINESS_PROBLEM_FRAMEWORK.md` | Convertir dolor operativo en pregunta medible, KPI, datos y visual. |
| 7 | `session_01/templates/BUSINESS_QUESTION_CANVAS.md` | Redactar una pregunta medible con métrica, periodo, dimensión y decisión. |
| 8 | `session_01/templates/KPI_TREE_TEMPLATE.md` | Definir KPI principal y KPIs de diagnóstico. |
| 9 | `data/training/dictionary/data_dictionary.md` | Ubicar tablas, columnas, llaves y significado de los datos. |
| 10 | `session_01/templates/DATA_REQUIREMENTS_TEMPLATE.md` | Documentar datos requeridos, transformaciones y reglas de calidad. |
| 11 | `powerbi/manual_steps/import_csv_files.md` | Importar el subconjunto de CSV necesario en Power BI Desktop. |
| 12 | `powerbi/manual_steps/power_query_quick_recap.md` | Revisar tipos, llaves, fechas y problemas que luego se resolverán en Power Query. |
| 13 | `powerbi/manual_steps/model_view_quick_recap.md` | Validar relaciones entre hechos y dimensiones. |
| 14 | `powerbi/dax_backlog/mining_kpi_measure_backlog.md` | Revisar medidas DAX futuras; en Módulo 1 se mantienen conceptuales. |
| 15 | `powerbi/manual_steps/report_view_quick_recap.md` | Crear visuales mínimos y saber qué campo colocar en cada bucket visual. |
| 16 | `powerbi/report_wireframes/mining_sla_backlog_dashboard_wireframe.md` | Consultar visuales recomendados para el caso SLA/backlog minero. |
| 17 | `session_01/templates/BI_SOLUTION_BLUEPRINT_TEMPLATE.md` | Completar el blueprint final con problema, pregunta, KPIs, datos, visuales y validación. |

## Agenda sugerida de 2 horas
| Minutos | Bloque | Resultado |
|---:|---|---|
| 0-10 | Apertura y contexto | Entender por qué Power BI es una arquitectura de decisiones |
| 10-25 | Ciclo analítico completo | Distinguir capas y responsabilidades |
| 25-45 | Recap Power BI Desktop | Reconocer Power Query, Vista de modelo, Vista de informe y DAX |
| 45-65 | Preguntas medibles y KPIs | Convertir problemas Tech&Eng en métricas |
| 65-95 | Laboratorio guiado | Importar tablas y explorar el caso |
| 95-110 | IA asistida | Revisar plano de solución con prompts y validación humana |
| 110-120 | Cierre | Exit ticket y próximos pasos |

## Producto esperado
Un archivo o copia de trabajo del plano de solución con:

- Problema operativo seleccionado.
- Pregunta analítica medible.
- Audiencia y decisión asociada.
- KPIs preliminares.
- Tablas necesarias.
- Boceto inicial.
- Riesgos de datos.
- Registro de cómo se usó IA y qué se validó manualmente.

## Límite pedagógico
En esta sesión no se corrigen todos los problemas de calidad, no se diseña el modelo estrella definitivo, no se escriben medidas DAX avanzadas y no se publica nada en Power BI Service. Eso se aborda en módulos posteriores.

## Caso minero del laboratorio
La operación minera sintética está en riesgo de no cumplir sus metas operacionales por una combinación de bajo rendimiento en chancado, backlog de mantenimiento, consumo energético anormal y acciones HSE pendientes. El estudiante debe diseñar una solución Power BI para priorizar decisiones, definir audiencia, seleccionar KPIs y justificar qué datos usar.

El blueprint debe incluir problema de negocio, preguntas analíticas, KPIs, datos necesarios, audiencia, páginas del dashboard, uso de IA, validaciones humanas y riesgos de interpretación.
