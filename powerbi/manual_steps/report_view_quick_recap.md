# Vista de informe Repaso rápido

## Propósito
Crear una página exploratoria mínima para conectar datos con una pregunta de negocio. No es el tablero final.

## Pregunta de ejemplo
¿Qué áreas y servicios concentran incumplimientos SLA y dónde debería priorizarse la revisión operativa?

## Visuales mínimos
Usa campos de dimensiones para segmentar y campos de `Fact_SLA` para contar o calcular. Si el objetivo es analizar incumplimientos, aplica filtro visual `Fact_SLA[SLAMetFlag] = False` o `0` en los visuales de diagnóstico.

| Visual | Campo de Power BI | Qué colocar | Agregación o filtro | Propósito |
|---|---|---|---|---|
| Tarjeta - volumen SLA | Datos / Valor | `Fact_SLA[SLAID]` | Recuento | Volumen total analizado |
| Tarjeta - horas incumplidas | Datos / Valor | `Fact_SLA[BreachHours]` | Promedio | Magnitud promedio del incumplimiento |
| Tarjeta - horas incumplidas | Filtros de este objeto visual | `Fact_SLA[SLAMetFlag]` | `False` o `0` | Mantener foco en incumplimientos |
| Barras - incumplimientos por área | Eje Y | `Dim_Area[AreaName]` | Sin agregación | Priorizar áreas |
| Barras - incumplimientos por área | Eje X | `Fact_SLA[SLAID]` | Recuento | Medir volumen de casos |
| Barras - incumplimientos por área | Filtros de este objeto visual | `Fact_SLA[SLAMetFlag]` | `False` o `0` | Mostrar solo incumplidos |
| Línea - tendencia mensual | Eje X | `Dim_Fecha[MonthName]` o `Dim_Fecha[Date]` | Usar `Date` si se necesita orden cronológico | Ver evolución |
| Línea - tendencia mensual | Eje Y | `Fact_SLA[SLAID]` | Recuento | Medir incumplimientos por periodo |
| Línea - tendencia mensual | Filtros de este objeto visual | `Fact_SLA[SLAMetFlag]` | `False` o `0` | Mostrar solo incumplidos |
| Barras apiladas - diagnóstico por servicio | Eje Y | `Dim_Servicio[ServiceName]` | Sin agregación | Ver qué servicios explican la desviación |
| Barras apiladas - diagnóstico por servicio | Eje X | `Fact_SLA[SLAID]` | Recuento | Medir volumen de incumplimientos |
| Barras apiladas - diagnóstico por servicio | Leyenda | `Dim_Prioridad[PriorityName]` | Sin agregación | Separar severidad/prioridad |
| Barras apiladas - diagnóstico por servicio | Filtros de este objeto visual | `Fact_SLA[SLAMetFlag]` | `False` o `0` | Mostrar solo incumplidos |
| Matriz - alternativa de diagnóstico | Filas | `Dim_Servicio[ServiceName]` | Sin agregación | Cruzar servicio y prioridad |
| Matriz - alternativa de diagnóstico | Columnas | `Dim_Prioridad[PriorityName]` | Sin agregación | Comparar prioridad por servicio |
| Matriz - alternativa de diagnóstico | Valores | `Fact_SLA[SLAID]` | Recuento | Medir volumen de casos |
| Matriz - alternativa de diagnóstico | Filtros de este objeto visual | `Fact_SLA[SLAMetFlag]` | `False` o `0` | Mostrar solo incumplidos |
| Slicer - prioridad | Campo | `Dim_Prioridad[PriorityName]` | Lista o desplegable | Explorar severidad |
| Slicer - servicio | Campo | `Dim_Servicio[ServiceName]` | Lista o desplegable | Filtrar servicio |
| Tabla - detalle accionable | Columnas | `Fact_SLA[SLAID]`, `Dim_Area[AreaName]`, `Dim_Servicio[ServiceName]`, `Dim_Prioridad[PriorityName]`, `Fact_SLA[BreachHours]` | Sin agregación para campos descriptivos | Ver casos para seguimiento |
| Tabla - detalle accionable | Filtros de este objeto visual | `Fact_SLA[SLAMetFlag]` | `False` o `0` | Mostrar solo casos accionables |

## Medidas simples para Módulo 1
Puedes usar agregaciones automáticas para explorar. En Módulo 4 se reemplazarán por medidas DAX formales.

## Diseño recomendado
- Título orientado a pregunta.
- KPIs arriba.
- Gráfico principal al centro.
- Filtros al lado o arriba.
- Detalle abajo.

## Preguntas de revisión
- ¿El visual muestra una prioridad de acción?
- ¿La audiencia entendería qué hacer después?
- ¿El filtro cambia correctamente todos los visuales?
- ¿Hay visuales decorativos que no aportan?
