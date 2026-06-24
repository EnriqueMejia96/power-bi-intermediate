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
