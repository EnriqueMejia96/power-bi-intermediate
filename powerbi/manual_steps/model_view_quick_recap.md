# Vista de modelo Repaso rápido

## Propósito
Comprender cómo Power BI conecta dimensiones y hechos para que los filtros funcionen correctamente. Un visual confiable depende de un modelo semántico claro.

## Relaciones para el ejercicio SLA
Crear o validar estas relaciones:

| Dimensión | Columna | Hecho | Columna | Tipo |
|---|---|---|---|---|
| Dim_Area | AreaID | Fact_SLA | AreaID | Muchos a uno |
| Dim_Servicio | ServiceID | Fact_SLA | ServiceID | Muchos a uno |
| Dim_Prioridad | PriorityID | Fact_SLA | PriorityID | Muchos a uno |
| Dim_Fecha | DateKey | Fact_SLA | CreatedDateKey | Muchos a uno |

## Configuración recomendada
- Cardinalidad: muchos a uno desde `Fact_SLA` hacia cada dimensión.
- Dirección de filtro: simple, desde dimensión hacia hecho.
- Relación activa: sí para las relaciones principales del ejercicio.

## Qué observar
Si filtras por `AreaName`, Power BI debe filtrar los registros de `Fact_SLA`. Si no ocurre, la relación no existe, está inactiva o las llaves no coinciden.

## Preguntas de aprendizaje
- ¿Por qué `Fact_SLA` no debería filtrar a `Dim_Area` como regla general?
- ¿Qué pasaría si `AreaName` se duplicara o cambiara de escritura?
- ¿Por qué usamos IDs y no nombres para relacionar?

## Advertencia
No intentes modelar todas las tablas en Módulo 1. El objetivo es entender el patrón. El modelo estrella completo se trabajará en Módulo 3.
