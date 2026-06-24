# Power Query, Vista de modelo y Vista de informe

## Power Query
Se usa para preparar datos antes de cargarlos al modelo. Ejemplos: corregir tipos, quitar columnas, normalizar valores, separar columnas y resolver formatos.

## Vista de modelo
Define relaciones y significado. Aquí se revisa si las dimensiones filtran correctamente a los hechos.

## Vista de informe
Comunica la decisión. Un visual no debe existir porque se ve bien, sino porque responde una pregunta.

## Ejercicio rápido
1. En Power Query, ubica `Fact_SLA[SLAMetFlag]`.
2. En Vista de modelo, relaciona `Dim_Area[AreaID]` con `Fact_SLA[AreaID]`.
3. En Vista de informe, crea un gráfico por `AreaName`.

## Discusión
Si el gráfico no responde una decisión, todavía no es BI; es solo visualización.
