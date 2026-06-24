# KPIs y preguntas de negocio mineras

## Propósito
Convertir problemas de operación minera en preguntas medibles y KPIs accionables para Power BI.

## Cómo se aplica a la especialización
Los estudiantes aprenden a no partir por el gráfico. Primero formulan decisión, audiencia, pregunta, KPI, datos y validación.

## Conexión con Power BI
Cada KPI debe mapearse a tablas, columnas, filtros y visuales. Las medidas DAX se implementarán en módulos posteriores.

## Conexión con el dataset
- `Fact_Productividad`: producción planificada y real.
- `Fact_Mantenimiento`: fallas, downtime, repair hours y costo.
- `Fact_OrdenesTrabajo`: backlog, criticidad y retrabajo.
- `Fact_SLA`: cumplimiento e incumplimiento.
- `Fact_Costos`: presupuesto, comprometido y real.
- `Fact_Energia`: kWh, costo y output.
- `Fact_Incidentes`: severidad y acciones correctivas.

## Conexión con módulos 1-6
Los KPIs se diseñan en Módulo 1, se limpian en Módulo 2, se modelan en Módulo 3, se calculan en Módulo 4 y se comunican en Módulos 5-6.

## Preguntas y KPIs ejemplo
| Pregunta | KPI | Tablas | Decisión |
|---|---|---|---|
| ¿Dónde cae la producción? | Cumplimiento de producción % | Fact_Productividad, Dim_Area | Priorizar soporte operativo |
| ¿Qué equipos generan más pérdida? | Downtime hours | Fact_Mantenimiento, Dim_Equipo | Priorizar mantenimiento |
| ¿Qué servicios incumplen? | % Cumplimiento SLA | Fact_SLA, Dim_Servicio | Reasignar recursos |
| ¿Dónde sube el gasto? | Variación de costo | Fact_Costos | Revisar presupuesto |
| ¿Dónde la energía es anómala? | kWh por output | Fact_Energia | Investigar eficiencia |
| ¿Qué riesgos HSE siguen abiertos? | Acciones vencidas | Fact_Incidentes | Escalar cierre |

## Riesgos de interpretación
Un KPI sin umbral no guía acción. Un promedio puede ocultar turnos o áreas críticas.

## Apoyo de IA
Pedir a IA que convierta un problema minero en preguntas medibles, pero exigir tabla, columna, fórmula conceptual y validación humana.

## Validación profesional
Confirmar definición, unidad, frecuencia, responsable, umbral y decisión asociada.
