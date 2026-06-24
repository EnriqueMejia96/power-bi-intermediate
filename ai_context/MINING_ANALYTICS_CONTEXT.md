# Contexto de analítica minera Tech&Eng

## Propósito
Definir el marco de negocio del caso sintético: una operación minera industrial con mina rajo abierto, planta concentradora, relaves, mantenimiento, energía, HSE y sistemas OT.

## Aplicación a la especialización
La minería funciona como contexto integrador para enseñar Power BI de extremo a extremo. No reemplaza el enfoque Tech&Eng; lo vuelve más concreto y operacional.

## Conexión con Power BI
Power BI se usa para transformar datos raw, construir modelo estrella, definir KPIs, diseñar páginas, contar hallazgos y priorizar decisiones. No se crea `.pbix` desde el repositorio.

## Conexión con el dataset
Dataset A entrena con señales en chancado, correas, taller mina, molienda y energía. Dataset B conserva el mismo schema y cambia las señales hacia dispatch, relaves, molienda, flota mina y OT.

## Conexión con módulos 1-6
- Módulo 1: blueprint BI, preguntas, KPIs, audiencia y wireframes.
- Módulo 2: limpieza raw vs clean, estandarización y trazabilidad.
- Módulo 3: modelo estrella y relaciones.
- Módulo 4: medidas DAX de producción, mantenimiento, SLA, costos, energía y HSE.
- Módulo 5: narrativa visual y diseño de dashboards.
- Módulo 6: optimización, publicación gobernada y proyecto.

## Preguntas de negocio
- ¿Qué áreas ponen en riesgo el cumplimiento operacional?
- ¿El bajo output se explica por fallas, energía, backlog o SLA?
- ¿Qué equipos críticos concentran downtime y costo?
- ¿Dónde hay acciones HSE vencidas?
- ¿Qué diferencias operacionales aparecen entre Dataset A y Dataset B?

## KPIs mineros
Cumplimiento de producción, downtime, costo de mantenimiento, órdenes críticas abiertas, % cumplimiento SLA, kWh por tonelada aproximado, incidentes por severidad, acciones correctivas vencidas y avance real vs plan.

## Riesgos de interpretación
No confundir correlación con causa raíz. Validar denominadores, granularidad, outliers, turnos, diferencias entre áreas y calidad raw antes de concluir.

## Cómo puede ayudar IA
IA puede ayudar a reformular problemas, proponer KPIs, revisar supuestos, generar preguntas de exploración y mejorar narrativa ejecutiva.

## Qué debe validar el profesional
Definiciones de negocio, reglas de cálculo, unidades, criticidad, contexto operacional y si una recomendación es accionable.
