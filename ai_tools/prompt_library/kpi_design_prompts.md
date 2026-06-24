# Diseñar KPIs y árboles de métricas

## Cuándo usarlo
Durante el diseño inicial del Diseño de solución BI, antes de construir el modelo final o escribir DAX productivo.

## Prompt
"Actúa como consultor BI para entornos Tech&Eng. Con los siguientes entradas: [problema], [audiencia], [tablas disponibles], [restricciones], propone una salida estructurada para diseñar kpis y árboles de métricas. No inventes datos, declara supuestos y marca riesgos."

## Inputs requeridos
Problema, audiencia, decisión esperada, tablas disponibles, periodo y restricciones.

## Output esperado
Lista priorizada con justificación, supuestos, riesgos y próximos pasos.

## Checklist de validación humana
- ¿La salida responde a una decisión?
- ¿El KPI o visual sugerido puede medirse con el esquema?
- ¿Hay supuestos no confirmados?
- ¿Se evitó compartir información sensible?

## Herramientas sugeridas
Microsoft Copilot for Power BI, Microsoft Copilot for Microsoft 365, Power BI Q&A, ChatGPT, Gemini, Claude, Perplexity, Excel Copilot o IA en hojas de cálculo.

## Advertencia de privacidad
Usar solo datos sintéticos o descripciones anonimizadas. No incluir clientes, contratos, personas, ubicaciones reales ni credenciales.

## Prompt minero adicional
**Título:** Diseñar KPIs mineros por dominio.

**Cuándo usarlo:** al construir el árbol de KPIs del blueprint.

**Prompt:** "Diseña KPIs para una operación minera sintética en producción, mantenimiento, costos, SLA, energía y HSE. Para cada KPI entrega definición, fórmula conceptual, tablas, columnas, audiencia, decisión, riesgo y posible nombre de medida DAX futura."

**Inputs requeridos:** dominio, audiencia, pregunta de negocio y columnas disponibles.

**Output esperado:** backlog de KPIs listo para revisión humana.

**Checklist de validación humana:** revisar unidad, denominador, granularidad y acción asociada.

**Advertencia de privacidad:** no cargar CSV ni nombres reales en herramientas externas.
