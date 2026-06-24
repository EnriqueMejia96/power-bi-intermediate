# Guía de KPIs mineros

## Propósito
Proveer una biblioteca conceptual para transformar problemas mineros en indicadores medibles dentro de Power BI.

## Aplicación a la especialización
Los KPIs sirven como hilo conductor entre arquitectura, Power Query, modelo, DAX, visualización e IA asistida.

## Conexión con Power BI
Las medidas definitivas se implementarán en módulos posteriores. En Módulo 1 se definen nombre, pregunta, audiencia, tabla base y riesgo de interpretación.

## Conexión con el dataset
- Producción/productividad: `Fact_Productividad`.
- Mantenimiento/confiabilidad: `Fact_Mantenimiento` y `Fact_OrdenesTrabajo`.
- SLA/backlog: `Fact_SLA` y `Fact_OrdenesTrabajo`.
- Costos: `Fact_Costos` y `Fact_Proyectos`.
- Energía: `Fact_Energia`.
- Seguridad: `Fact_Incidentes`.

## Conexión con módulos 1-6
Módulo 1 diseña KPIs; Módulo 2 limpia campos; Módulo 3 modela relaciones; Módulo 4 escribe DAX; Módulo 5 visualiza; Módulo 6 valida y optimiza.

## Preguntas de negocio
- ¿Qué área tiene mayor brecha plan vs real?
- ¿Qué equipo genera más downtime por evento?
- ¿Qué servicios incumplen SLA crítico?
- ¿Qué categoría de costo explica el sobrecosto?
- ¿Dónde sube el kWh por unidad de output?

## KPIs ejemplo
- Cumplimiento de producción % = output real / output planificado.
- Downtime hours = suma de horas de indisponibilidad.
- MTTR aproximado = repair hours / eventos de mantenimiento.
- Backlog = órdenes abiertas o vencidas.
- Cumplimiento SLA % = SLA cumplidos / SLA totales.
- kWh por tonelada aproximado = kWh / OutputUnits.
- Acciones HSE vencidas = incidentes con CorrectiveActionStatus = Vencida.

## Riesgos de interpretación
Algunos denominadores son aproximados. `OutputUnits` depende del área y no debe compararse sin segmentar. `RepairHours` no siempre explica todo el downtime.

## Cómo puede ayudar IA
IA puede proponer nombres de medidas, explicar fórmulas conceptuales y detectar KPIs sin decisión asociada.

## Qué debe validar el profesional
Unidad, frecuencia, dueño del KPI, umbral, acción esperada y si la métrica se puede auditar.
