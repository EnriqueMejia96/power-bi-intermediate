# IA responsable para BI

## Qué se aprende
En este documento se aprende a proteger privacidad y validar salidas. El foco es que el estudiante pueda tomar una decisión de diseño BI y explicar por qué esa decisión mejora la confiabilidad del análisis.

## Por qué importa
En entornos Tech&Eng, los reportes suelen mezclar datos de mantenimiento, proyectos, costos, SLA, seguridad, energía y productividad. Sin arquitectura, cada reporte termina siendo una solución aislada, difícil de auditar y poco útil para decidir.

## Cómo se aplica en Tech&Eng
El caso sintético permite analizar situaciones como retrasos de proyecto, backlog, incumplimiento SLA, sobrecostos, mantenimiento correctivo, incidentes abiertos, anomalías energéticas y productividad variable.

## Aplicación práctica
Para este tema, la práctica consiste en documentar uso responsable. El estudiante debe usar el diccionario de datos y seleccionar hechos/dimensiones que respondan una pregunta concreta.

## Conexión con Power BI
- Power Query prepara los datos.
- El modelo semántico organiza relaciones.
- DAX calcula KPIs.
- Vista de informe comunica hallazgos.
- Power BI Service se deja para módulos posteriores.

## Conexión con IA asistida
La IA puede ayudar a idear preguntas, revisar KPIs, comparar visuales o detectar vacíos. No debe recibir datos sensibles ni reemplazar la validación humana.

## Ejemplo Tech&Eng
Problema: el cumplimiento SLA cae en ciertos servicios.

Pregunta medible: ¿qué áreas y servicios presentan mayor porcentaje de incumplimiento SLA durante el periodo analizado?

KPI: `% SLA cumplido`.

Dimensiones: área, servicio, prioridad y fecha.

Decisión: reasignar capacidad o revisar compromisos de servicio.

## Errores comunes
- Diseñar visuales antes de definir la pregunta.
- Usar KPIs sin fórmula ni umbral.
- Confundir limpieza de datos con DAX.
- Importar todas las tablas sin propósito.
- Aceptar salidas de IA sin revisar supuestos.

## Qué se hará en módulos futuros
Módulo 2 resolverá calidad de datos en Power Query. Módulo 3 formalizará el modelo estrella. Módulo 4 implementará medidas DAX. Módulo 5 trabajará narrativa de datos. Módulo 6 abordará optimización, publicación y proyecto.

## Checklist rápido
- ¿Hay una pregunta medible?
- ¿Existe una audiencia definida?
- ¿Las tablas elegidas soportan la métrica?
- ¿El KPI tiene decisión asociada?
- ¿La IA se usó con privacidad y validación?
