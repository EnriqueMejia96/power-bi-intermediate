# Pasos Detallados del Laboratorio

## Parte A: confirmar datos
1. Verifica que existen archivos CSV en `data/training/sample`.
2. Abre `data/training/metadata/manifest.json` y observa los conteos.
3. Abre `reports/dataset_profile/training_profile.md` para revisar volumen y columnas.

## Parte B: seleccionar una línea de análisis
Elige una de estas líneas:

| Línea | Pregunta guía | Tablas base |
|---|---|---|
| SLA | ¿Dónde se incumple más el servicio? | `Fact_SLA`, `Dim_Area`, `Dim_Servicio`, `Dim_Prioridad` |
| Backlog | ¿Qué áreas concentran órdenes abiertas? | `Fact_OrdenesTrabajo`, `Dim_Area`, `Dim_Estado`, `Dim_TipoTrabajo` |
| Costos | ¿Qué proyectos o áreas superan presupuesto? | `Fact_Costos`, `Dim_Proyecto`, `Dim_Area` |
| Mantenimiento | ¿Qué equipos críticos concentran correctivos? | `Fact_Mantenimiento`, `Dim_Equipo`, `Dim_Area` |
| Energía | ¿Qué área consume más kWh por unidad? | `Fact_Energia`, `Dim_Area`, `Dim_Equipo` |
| Productividad | ¿Dónde cae la producción real vs plan? | `Fact_Productividad`, `Dim_Area`, `Dim_Responsable` |

## Parte C: importar en Power BI Desktop
1. Abrir Power BI Desktop.
2. Seleccionar **Obtener datos > Texto/CSV**.
3. Importar `Dim_Fecha.csv`.
4. Importar una o dos dimensiones de negocio, por ejemplo `Dim_Area.csv` y `Dim_Servicio.csv`.
5. Importar una tabla de hechos, por ejemplo `Fact_SLA.csv`.
6. Presionar **Transformar datos** para entrar a Power Query.

## Parte D: recap Power Query
1. Revisar nombres de columnas.
2. Revisar tipos de datos.
3. Identificar columnas llave: `DateKey`, `AreaID`, `ServiceID`, `PriorityID`.
4. No hacer limpieza profunda todavía. Anotar observaciones para Módulo 2.

## Parte E: recap modelo
1. Ir a **Vista de modelo**.
2. Verificar relaciones sugeridas o crearlas manualmente:
   - `Dim_Area[AreaID]` -> `Fact_SLA[AreaID]`
   - `Dim_Servicio[ServiceID]` -> `Fact_SLA[ServiceID]`
   - `Dim_Prioridad[PriorityID]` -> `Fact_SLA[PriorityID]`
   - `Dim_Fecha[DateKey]` -> `Fact_SLA[CreatedDateKey]`
3. Usar cardinalidad muchos-a-uno desde hecho hacia dimensión.
4. Mantener filtro simple desde dimensión hacia hecho.

## Parte F: recap reporte
Crear una página con:

- Tarjeta: conteo de registros SLA.
- Tarjeta: promedio de `BreachHours`.
- Barras: `AreaName` por conteo de incumplimientos.
- Línea: incumplimientos por mes.
- Slicer: `PriorityName` o `ServiceName`.

No importa que las medidas aún sean simples. En Módulo 4 se formalizarán con DAX.

## Parte G: completar plano de solución
Completar:

- Problema.
- Pregunta medible.
- Audiencia.
- Decisión que habilita.
- KPIs.
- Tablas y columnas.
- Riesgos de calidad.
- Boceto.
- Prompt de IA utilizado.
- Validación humana realizada.

## Parte H: cierre
Responder el exit ticket y guardar el `.pbix` solo si el instructor lo pide. El repositorio no debe almacenar `.pbix`.

## Caso minero para el entregable
Usa este enunciado: "La operación minera está en riesgo de no cumplir sus metas operacionales por una combinación de bajo rendimiento en chancado, backlog de mantenimiento, consumo energético anormal y acciones HSE pendientes. Diseñe una solución Power BI para priorizar decisiones."

Tu respuesta debe conectar al menos producción, mantenimiento, SLA/backlog, energía y HSE.
