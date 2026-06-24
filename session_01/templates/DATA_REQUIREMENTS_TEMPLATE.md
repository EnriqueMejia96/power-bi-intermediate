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
