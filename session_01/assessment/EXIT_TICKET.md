# Exit Ticket - Módulo 1

Completar en 5-7 minutos al cierre de la sesión.

## Preguntas
1. Explica en una frase la diferencia entre Power Query, modelo semántico, DAX y visuales.
2. Escribe una pregunta medible para el caso Tech&Eng.
3. Indica un KPI que responda esa pregunta y redacta su fórmula tentativa en lenguaje natural.
4. ¿Qué audiencia usaría ese KPI y qué decisión tomaría?
5. Menciona dos tablas del dataset que necesitarías.
6. ¿Qué riesgo de calidad de datos podría afectar tu análisis?
7. ¿Qué validarías antes de aceptar una recomendación generada por IA?

## Ejemplo de respuesta fuerte
Pregunta: ¿qué áreas concentran mayor porcentaje de incumplimiento SLA durante el periodo analizado?

KPI: `% SLA cumplido = registros SLA cumplidos / total de registros SLA`.

Audiencia: responsable de servicios técnicos.

Decisión: reasignar capacidad o revisar compromisos por servicio.

Tablas: `Fact_SLA`, `Dim_Area`, `Dim_Servicio`, `Dim_Prioridad`, `Dim_Fecha`.

Riesgo: prioridades o estados inconsistentes pueden distorsionar el conteo.

## Criterio rápido de revisión
Una respuesta fuerte conecta problema, dato, KPI, audiencia y decisión. Una respuesta débil solo menciona "hacer un gráfico" o "ver indicadores" sin explicar para qué.
