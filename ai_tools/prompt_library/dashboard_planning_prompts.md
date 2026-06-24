# Planificar estructura y boceto de tablero

## Cuándo usarlo
Durante el diseño inicial del Diseño de solución BI, antes de construir el modelo final o escribir DAX productivo.

## Prompt
"Actúa como consultor BI para entornos Tech&Eng. Con los siguientes entradas: [problema], [audiencia], [tablas disponibles], [restricciones], propone una salida estructurada para planificar estructura y boceto de tablero. No inventes datos, declara supuestos y marca riesgos."

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
**Título:** Diseñar dashboard minero ejecutivo y operativo.

**Cuándo usarlo:** al pasar de KPIs a wireframe.

**Prompt:** "Propón páginas Power BI para una operación minera sintética: resumen ejecutivo, operaciones, mantenimiento/SLA, energía, seguridad y causa raíz. Para cada página indica audiencia, pregunta, KPIs, visuales, filtros, drill-through, tooltips, uso de IA y riesgos de interpretación."

**Inputs requeridos:** audiencia, KPIs priorizados, tablas y restricciones.

**Output esperado:** wireframe textual por página.

**Checklist de validación humana:** verificar que cada visual responda una decisión y que no haya sobrecarga.

**Advertencia de privacidad:** usar solo descripciones sintéticas.
