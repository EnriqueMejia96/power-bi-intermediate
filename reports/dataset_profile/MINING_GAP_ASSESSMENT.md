# Mining gap assessment

## Estado antes de la mejora
- El repositorio ya tenia una arquitectura didactica clara para Power BI: Dataset A para entrenamiento, Dataset B para proyecto final, datos raw/clean, validaciones, diccionario y materiales de sesion.
- El enfoque era Tech&Eng industrial, con algunas referencias a mineria, mantenimiento, energia y seguridad.
- El schema ya estaba validado por tests y debia preservarse.

## Gaps detectados
- Las dimensiones necesitaban vocabulario minero explicito: mina, planta concentradora, chancado, molienda, flotacion, relaves, HSE y OT.
- Los hechos necesitaban patrones operacionales diferenciados para backlog, SLA, downtime, energia, productividad, incidentes, costos y proyectos.
- El diccionario describia campos de forma demasiado generica y no explicaba como interpretar metricas como ActualOutput, OutputUnits, DelayDays o RiskScore.
- Los materiales del Modulo 1 necesitaban un caso minero mas concreto para blueprint, preguntas, KPIs, audiencia y wireframes.
- Faltaban tests de cobertura minera y reportes de perfil minero.

## Cambios aplicados sin romper schema
- Se mantienen las mismas tablas y columnas principales de Dataset A y Dataset B.
- Dataset A conserva uso de entrenamiento y Dataset B conserva uso de proyecto final.
- Raw mantiene problemas controlados para Power Query; clean queda listo para modelo estrella.
- Se agregan valores mineros, documentacion, reportes, Make targets y tests sin crear PBIX ni llamar servicios externos.

## Cambios opcionales futuros
- Agregar columnas opcionales como OutputUnit, CrewName o MaterialType solo si un modulo posterior lo requiere y actualiza schema, tests y diccionario.
- Implementar medidas DAX en Modulo 4 usando el backlog de KPIs mineros.
- Crear paginas Power BI manualmente en Modulos 5-6 sin versionar archivos PBIX.
