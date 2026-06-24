# Borrador de Modelo Recomendado

## Objetivo
Proponer una primera lectura del modelo para Módulo 1. No es el modelo estrella final, pero prepara el razonamiento para Módulo 3.

## Hechos principales
| Tabla | Granularidad | Preguntas típicas |
|---|---|---|
| Fact_OrdenesTrabajo | Orden de trabajo | Backlog, horas, rework, criticidad |
| Fact_SLA | Registro SLA asociado a orden | Cumplimiento, breach, prioridad |
| Fact_Costos | Registro de costo | Variación presupuesto-real |
| Fact_Mantenimiento | Evento de mantenimiento | Downtime, correctivo/preventivo |
| Fact_Incidentes | Incidente | Severidad, acciones abiertas |
| Fact_Energia | Lectura energética | kWh, costo, producción |
| Fact_Productividad | Registro de productividad | Output, horas, eficiencia |
| Fact_Proyectos | Snapshot/progreso de proyecto | Avance, costo, riesgo |

## Dimensiones conformadas
`Dim_Fecha`, `Dim_Area`, `Dim_Equipo`, `Dim_Proyecto`, `Dim_Responsable`, `Dim_Prioridad`, `Dim_Estado`, `Dim_Servicio`, `Dim_Ubicacion`, `Dim_Cliente`, `Dim_TipoTrabajo`.

## Relaciones iniciales
Priorizar relaciones desde dimensiones hacia hechos. Usar `DateKey` como relación principal de tiempo y documentar fechas alternativas como cierre o resolución.

## Decisiones pendientes
- Definir si habrá tabla calendario marcada en Power BI.
- Revisar roles de fecha para órdenes: creada, cerrada, comprometida, resuelta.
- Definir medidas base en Módulo 4.
