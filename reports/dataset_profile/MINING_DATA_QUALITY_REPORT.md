# Mining data quality report

## training
# Problemas de calidad controlados

- Nombres de area minera inconsistentes en Dim_Area.
- Prioridades mezclan espanol, ingles, mayusculas y criticidad minera.
- Estados inconsistentes: Open, In Progress, Closed, Cerrado y Done.
- Servicios mineros abreviados en raw: Mant. Mina, Mant. Planta, Insp. Correas y Soporte Disp.
- Fechas de proyecto minero exportadas como texto en formatos mixtos.
- Duplicados controlados en ordenes de trabajo de mantenimiento minero.
- Fechas de cierre nulas en ordenes abiertas.
- Costos outliers y columna innecesaria exportada desde ERP minero.
- Algunos mantenimientos referencian equipo minero por nombre y no por ID.
- Archivo adicional de energia en formato ancho por turno.

## project
# Problemas de calidad controlados

- Nombres de area minera inconsistentes en Dim_Area.
- Prioridades mezclan espanol, ingles, mayusculas y criticidad minera.
- Estados inconsistentes: Open, In Progress, Closed, Cerrado y Done.
- Servicios mineros abreviados en raw: Mant. Mina, Mant. Planta, Insp. Correas y Soporte Disp.
- Fechas de proyecto minero exportadas como texto en formatos mixtos.
- Duplicados controlados en ordenes de trabajo de mantenimiento minero.
- Fechas de cierre nulas en ordenes abiertas.
- Costos outliers y columna innecesaria exportada desde ERP minero.
- Algunos mantenimientos referencian equipo minero por nombre y no por ID.
- Archivo adicional de energia en formato ancho por turno.

## Raw vs clean
- `raw` conserva fechas como texto, estados mixtos, prioridades inconsistentes, duplicados, nulos, outliers, columnas extra y energia en formato ancho.
- `clean` mantiene columnas estables, llaves consistentes y valores estandarizados para modelo estrella.
- Estos problemas estan diseñados para el Modulo 2; no deben eliminarse sin actualizar materiales y tests.