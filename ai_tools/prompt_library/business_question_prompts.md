# Convertir problema de negocio en preguntas analíticas

## Cuándo usarlo
Durante el diseño inicial del Diseño de solución BI, antes de construir el modelo final o escribir DAX productivo.

## Prompt
"Actúa como consultor BI para entornos Tech&Eng. Con los siguientes entradas: [problema], [audiencia], [tablas disponibles], [restricciones], propone una salida estructurada para convertir problema de negocio en preguntas analíticas. No inventes datos, declara supuestos y marca riesgos."

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
**Título:** Convertir riesgo operacional minero en preguntas medibles.

**Cuándo usarlo:** cuando el problema mencione bajo output, backlog, SLA, energía o HSE.

**Prompt:** "A partir de este problema minero sintético: [problema], genera preguntas medibles para Power BI. Para cada pregunta incluye audiencia, decisión, KPI, tablas/columnas probables, visual recomendado, riesgo de interpretación y validación humana."

**Inputs requeridos:** problema, audiencia, tablas disponibles y periodo.

**Output esperado:** matriz de preguntas priorizadas.

**Checklist de validación humana:** confirmar si la audiencia puede actuar, si el KPI existe en el schema y si la pregunta no revela causa raíz no demostrada.

**Advertencia de privacidad:** no usar datos reales de faenas, personas, clientes o contratos.
