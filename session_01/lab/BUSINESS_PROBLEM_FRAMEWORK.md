# Framework - Del dolor operativo a la pregunta medible

## Problema de negocio
La operacion minera sintetica muestra riesgo de incumplimiento operacional porque algunos servicios presentan atrasos SLA en areas criticas, pero la gerencia no sabe que areas, servicios y prioridades concentran la desviacion.

## Pregunta medible
Que areas y servicios concentran mayor incumplimiento SLA durante el periodo analizado, y que prioridad deberia atender primero la jefatura de operaciones o mantenimiento?

## KPI conceptual
**% SLA incumplido** = SLA no cumplidos / SLA evaluados.

KPIs de apoyo:
- **Horas promedio de incumplimiento**, usando `BreachHours`.
- **Volumen de SLA criticos/incumplidos**, por area, servicio y prioridad.

## Datos requeridos
Tabla de hechos:
- `Fact_SLA`: `SLAID`, `AreaID`, `ServiceID`, `PriorityID`, `CreatedDateKey`, `SLAMetFlag`, `BreachHours`.

Dimensiones:
- `Dim_Area`: `AreaID`, `AreaName`.
- `Dim_Servicio`: `ServiceID`, `ServiceName`.
- `Dim_Prioridad`: `PriorityID`, `PriorityName`.
- `Dim_Fecha`: `DateKey`, `Date`, `MonthName`, `Year`.

## Visual propuesto
Ranking de incumplimientos por area, tendencia mensual, detalle por servicio/prioridad y slicer de prioridad.
