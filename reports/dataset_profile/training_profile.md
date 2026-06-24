# Perfil dataset training

## Dim_Fecha
- Filas: 366
- Columnas: 9
- Nulos principales: sin nulos críticos.
- Columnas numéricas: DateKey, Year, MonthNumber, WeekNumber

## Dim_Area
- Filas: 17
- Columnas: 6
- Nulos principales: sin nulos críticos.

## Dim_Equipo
- Filas: 60
- Columnas: 9
- Nulos principales: sin nulos críticos.

## Dim_Cliente
- Filas: 20
- Columnas: 5
- Nulos principales: sin nulos críticos.

## Dim_Proyecto
- Filas: 80
- Columnas: 9
- Nulos principales: sin nulos críticos.

## Dim_Responsable
- Filas: 30
- Columnas: 5
- Nulos principales: sin nulos críticos.

## Dim_TipoTrabajo
- Filas: 12
- Columnas: 4
- Nulos principales: sin nulos críticos.

## Dim_Prioridad
- Filas: 4
- Columnas: 5
- Nulos principales: sin nulos críticos.
- Columnas numéricas: PriorityRank, TargetResponseHours, TargetResolutionHours

## Dim_Estado
- Filas: 5
- Columnas: 5
- Nulos principales: sin nulos críticos.
- Columnas numéricas: SortOrder

## Dim_Servicio
- Filas: 12
- Columnas: 4
- Nulos principales: sin nulos críticos.
- Columnas numéricas: DefaultSLAHours

## Dim_Ubicacion
- Filas: 17
- Columnas: 5
- Nulos principales: sin nulos críticos.

## Fact_Proyectos
- Filas: 80
- Columnas: 14
- Nulos principales: sin nulos críticos.
- Columnas numéricas: DateKey, PlannedProgressPct, ActualProgressPct, PlannedCost, ActualCost, RiskScore, DelayDays

## Fact_OrdenesTrabajo
- Filas: 5000
- Columnas: 15
- Nulos principales: ClosedDateKey=1802
- Columnas numéricas: CreatedDateKey, ClosedDateKey, EstimatedHours, ActualHours

## Fact_Costos
- Filas: 2500
- Columnas: 10
- Nulos principales: sin nulos críticos.
- Columnas numéricas: DateKey, BudgetAmount, ActualAmount, CommittedAmount

## Fact_SLA
- Filas: 4000
- Columnas: 13
- Nulos principales: sin nulos críticos.
- Columnas numéricas: CreatedDateKey, CommittedDateKey, ResolvedDateKey, TargetHours, ActualHours, BreachHours

## Fact_Mantenimiento
- Filas: 1800
- Columnas: 12
- Nulos principales: sin nulos críticos.
- Columnas numéricas: DateKey, DowntimeHours, RepairHours, MaintenanceCost

## Fact_Incidentes
- Filas: 500
- Columnas: 11
- Nulos principales: sin nulos críticos.
- Columnas numéricas: DateKey, DaysOpen

## Fact_Energia
- Filas: 12000
- Columnas: 10
- Nulos principales: sin nulos críticos.
- Columnas numéricas: DateKey, kWh, EnergyCost, OperatingHours, OutputUnits

## Fact_Productividad
- Filas: 4000
- Columnas: 11
- Nulos principales: sin nulos críticos.
- Columnas numéricas: DateKey, PlannedOutput, ActualOutput, LaborHours, ProductiveHours, NonProductiveHours
