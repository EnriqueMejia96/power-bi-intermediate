# Plantilla de Requerimientos de Datos

| Pregunta | Tabla | Columna | Tipo esperado | Transformación | Regla de calidad |
|---|---|---|---|---|---|
| | | | | | |

## Checklist
- ¿Existe una fecha para analizar tendencia?
- ¿Existe una dimensión para comparar?
- ¿La tabla de hechos tiene granularidad clara?
- ¿Las llaves conectan con dimensiones?
- ¿Hay valores nulos, duplicados o formatos mixtos?
- ¿La regla de negocio de cierre/estado está documentada?

## Ejemplo SLA
| Pregunta | Tabla | Columna | Tipo esperado | Transformación | Regla |
|---|---|---|---|---|---|
| Cumplimiento SLA por área | Fact_SLA | SLAMetFlag | Booleano | Ninguna en datos limpios (`clean`) | No nulo |
| Cumplimiento SLA por área | Dim_Area | AreaName | Texto | Normalizar en datos crudos (`raw`) | Sin variantes |

## Ejemplo minero integrado
| Pregunta | Tabla | Columna | Tipo esperado | Transformación | Regla |
|---|---|---|---|---|---|
| Bajo rendimiento en chancado | Fact_Productividad | PlannedOutput, ActualOutput | Numérico | Validar nulos y tipos | Output real <= plan requiere explicación |
| Backlog de mantenimiento | Fact_OrdenesTrabajo | StatusID, IsCritical | ID/Booleano | Relacionar con Dim_Estado | Estado limpio y consistente |
| Consumo energético anormal | Fact_Energia | kWh, OutputUnits, Shift | Numérico/texto | Validar outliers | No dividir por cero |
| Acciones HSE pendientes | Fact_Incidentes | CorrectiveActionStatus, DaysOpen | Texto/numérico | Estandarizar estado | Vencidas deben escalarse |
