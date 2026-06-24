# Backlog Futuro de Medidas DAX

Estas medidas no se implementan en Módulo 1. Sirven para conectar el plano de solución con Módulo 4.

| KPI | Descripción | Tabla base | Prioridad |
|---|---|---|---|
| Total Work Orders | Conteo de órdenes | Fact_OrdenesTrabajo | Alta |
| Open Backlog | Órdenes no cerradas | Fact_OrdenesTrabajo + Dim_Estado | Alta |
| SLA Compliance % | SLA cumplidos / total SLA | Fact_SLA | Alta |
| Average Breach Hours | Promedio de horas de incumplimiento | Fact_SLA | Alta |
| Cost Variance | Costo real - presupuesto | Fact_Costos | Alta |
| Cost Variance % | Variación relativa | Fact_Costos | Media |
| Corrective Maintenance % | Correctivos / mantenimientos | Fact_Mantenimiento | Alta |
| Downtime Hours | Horas de parada | Fact_Mantenimiento | Alta |
| Open Corrective Actions | Incidentes con acción no cerrada | Fact_Incidentes | Media |
| kWh per Output Unit | Consumo por unidad producida | Fact_Energia | Media |
| Productivity Rate | Producción real / producción planificada | Fact_Productividad | Alta |

## Reglas
Toda medida DAX futura debe tener definición de negocio, fórmula, tabla base, filtros esperados y prueba de consistencia.
