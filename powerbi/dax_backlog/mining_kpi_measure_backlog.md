# Backlog de medidas KPI mineras

Este backlog prepara futuras medidas DAX para módulos posteriores. No implementa un `.pbix` ni reemplaza validación de negocio.

| KPI | Definición | Fórmula conceptual | Tablas | Columnas | Audiencia | Decisión | Riesgo | DAX futuro |
|---|---|---|---|---|---|---|---|---|
| Toneladas planificadas | Output objetivo por turno/área | SUM(PlannedOutput) | Fact_Productividad | PlannedOutput | Operaciones | Evaluar plan | Unidad depende de área | `[Planned Output]` |
| Toneladas reales | Output real registrado | SUM(ActualOutput) | Fact_Productividad | ActualOutput | Operaciones | Medir desempeño | No comparar áreas sin contexto | `[Actual Output]` |
| Cumplimiento de producción % | Real sobre plan | Actual / Planned | Fact_Productividad | ActualOutput, PlannedOutput | Gerencia, operaciones | Priorizar brechas | Dividir por cero; granularidad | `[Production Compliance %]` |
| Productividad por turno | Output real por turno | ActualOutput por Shift | Fact_Productividad, Dim_Area | ActualOutput, Shift | Jefes de turno | Balancear recursos | Turnos con distinta carga | `[Output by Shift]` |
| Toneladas por hora productiva | Output por hora productiva | ActualOutput / ProductiveHours | Fact_Productividad | ActualOutput, ProductiveHours | Operaciones | Detectar eficiencia | Horas productivas mal clasificadas | `[Output per Productive Hour]` |
| Downtime hours | Indisponibilidad total | SUM(DowntimeHours) | Fact_Mantenimiento | DowntimeHours | Mantenimiento | Priorizar activos | Downtime puede incluir espera | `[Downtime Hours]` |
| Disponibilidad operacional aprox. | Tiempo operativo vs downtime | 1 - Downtime / (OperatingHours + Downtime) | Fact_Mantenimiento, Fact_Energia | DowntimeHours, OperatingHours | Gerencia técnica | Evaluar continuidad | Aproximada, no reemplaza OEE | `[Approx Availability %]` |
| MTTR aproximado | Tiempo medio de reparación | RepairHours / eventos | Fact_Mantenimiento | RepairHours, MaintenanceID | Confiabilidad | Reducir tiempos | No incluye espera logística | `[Approx MTTR]` |
| Backlog mantenimiento | Órdenes abiertas o vencidas | Count Status no cerrado | Fact_OrdenesTrabajo, Dim_Estado | WorkOrderID, IsClosed, StatusName | Planificación | Reasignar cuadrillas | Estados raw deben limpiarse | `[Maintenance Backlog]` |
| Órdenes críticas abiertas | Órdenes críticas no cerradas | Count IsCritical y no cerrado | Fact_OrdenesTrabajo | IsCritical, StatusID | Operaciones | Escalar riesgo | Criticidad sintética | `[Open Critical WOs]` |
| Correctivo vs preventivo | Mix de tipo de trabajo | Count por WorkCategory | Fact_Mantenimiento, Dim_TipoTrabajo | WorkTypeID, WorkCategory | Mantenimiento | Mejorar estrategia | Depende de clasificación | `[Corrective Preventive Mix]` |
| Costo de mantenimiento | Costo total por eventos | SUM(MaintenanceCost) | Fact_Mantenimiento | MaintenanceCost | Mantenimiento, finanzas | Controlar gasto | Outliers intencionales | `[Maintenance Cost]` |
| Costo real vs presupuesto | Brecha de costos | ActualAmount - BudgetAmount | Fact_Costos | ActualAmount, BudgetAmount | Finanzas, gerencia | Control presupuestario | Comprometido no es real | `[Cost Variance]` |
| Costo por equipo | Costo segmentado por activo | ActualAmount por EquipmentID | Fact_Costos, Dim_Equipo | ActualAmount, EquipmentID | Mantenimiento | Priorizar activos | Equipos con distinta escala | `[Cost by Equipment]` |
| Costo por tonelada aprox. | Costo dividido por output | ActualAmount / ActualOutput | Fact_Costos, Fact_Productividad | ActualAmount, ActualOutput | Gerencia | Eficiencia económica | Requiere granularidad compatible | `[Approx Cost per Output]` |
| Cumplimiento SLA % | SLA cumplidos sobre total | SUM(SLAMetFlag) / COUNT(SLAID) | Fact_SLA | SLAMetFlag, SLAID | Servicios, operaciones | Reasignar soporte | SLA por prioridad difiere | `[SLA Compliance %]` |
| Horas de incumplimiento | Brecha total SLA | SUM(BreachHours) | Fact_SLA | BreachHours | Servicios | Atacar cuellos | Cero no siempre significa sin riesgo | `[Breach Hours]` |
| Tiempo promedio resolución | Promedio de horas reales SLA | AVERAGE(ActualHours) | Fact_SLA | ActualHours | Servicios | Ajustar capacidad | Afectado por outliers | `[Avg Resolution Hours]` |
| kWh total | Consumo energético | SUM(kWh) | Fact_Energia | kWh | Energía | Monitorear consumo | Volumen operacional cambia | `[Total kWh]` |
| Costo energía | Costo asociado al consumo | SUM(EnergyCost) | Fact_Energia | EnergyCost | Energía, finanzas | Controlar gasto | Tarifa sintética | `[Energy Cost]` |
| kWh por tonelada aprox. | Intensidad energética | kWh / OutputUnits | Fact_Energia | kWh, OutputUnits | Planta, energía | Detectar anomalías | OutputUnits depende de área | `[Approx kWh per Output]` |
| Variación de consumo | Cambio temporal de kWh | kWh actual vs periodo anterior | Fact_Energia, Dim_Fecha | kWh, DateKey | Energía | Investigar picos | Requiere calendario | `[kWh Variation]` |
| Incidentes | Conteo de incidentes | COUNT(IncidentID) | Fact_Incidentes | IncidentID | HSE | Priorizar prevención | Conteo sin severidad es limitado | `[Incidents]` |
| Incidentes por severidad | Incidentes segmentados | Count por Severity | Fact_Incidentes | Severity | HSE, gerencia | Escalar críticos | Severidad sintética | `[Incidents by Severity]` |
| Acciones correctivas abiertas | Acciones no cerradas | Count status abierto | Fact_Incidentes | CorrectiveActionStatus | HSE | Cerrar acciones | Estado debe estandarizarse | `[Open Corrective Actions]` |
| Acciones correctivas vencidas | Acciones vencidas | Count status Vencida | Fact_Incidentes | CorrectiveActionStatus, DaysOpen | HSE | Escalar vencidas | Necesita regla de vencimiento | `[Overdue Corrective Actions]` |
| Avance proyecto vs plan | Brecha de avance | ActualProgressPct - PlannedProgressPct | Fact_Proyectos | ActualProgressPct, PlannedProgressPct | PMO, gerencia | Priorizar proyectos | Porcentajes no se suman | `[Project Progress Gap]` |
| Riesgo de proyecto | Puntaje de riesgo | AVERAGE(RiskScore) | Fact_Proyectos | RiskScore | PMO | Escalar riesgos | Score sintético | `[Project Risk Score]` |
