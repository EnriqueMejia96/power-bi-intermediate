# Mining root cause patterns - instructor-only

**INSTRUCTOR-ONLY. No copiar este archivo a carpetas student ni usarlo como handout.**

## Dataset A - entrenamiento
- Chancado Primario y Transporte por Correas concentran brechas de SLA, órdenes críticas y eventos de mantenimiento.
- Molienda muestra consumo energético anormal y brecha entre output planificado y real.
- Taller Mina concentra backlog y acciones HSE abiertas.
- Costos altos aparecen en correas, molienda y componentes de flota CAEX.

## Dataset B - proyecto final
- Dispatch, Relaves, Molienda y Automatización OT concentran problemas distintos.
- Relaves y planta tienen mayor riesgo HSE y acciones vencidas.
- Molienda y relaves concentran sobrecostos y downtime.
- La causa raíz no debe revelarse de forma directa; se espera que el estudiante la infiera con KPIs, segmentación y narrativa.

## Tablas donde observar patrones
- `Fact_OrdenesTrabajo`: backlog, estado, criticidad, retrabajo, sistema fuente.
- `Fact_SLA`: cumplimiento, breach hours, prioridad y servicio.
- `Fact_Mantenimiento`: failure mode, downtime, repair hours y costo.
- `Fact_Energia`: kWh, output units, turno y equipo.
- `Fact_Productividad`: plan vs real y horas productivas.
- `Fact_Incidentes`: severidad, estado de acción correctiva y días abiertos.
- `Fact_Costos`: categoría, presupuesto, real y comprometido.
- `Fact_Proyectos`: avance, costo, riesgo y retraso.

## Guía didáctica
- Hacer preguntas, no entregar respuestas: "¿qué cambia cuando filtras por turno?", "¿el problema es costo, downtime o SLA?", "¿la señal aparece en más de una tabla?".
- Pedir validaciones humanas: confirmar definiciones, revisar outliers, separar correlación de causalidad y explicar supuestos.
