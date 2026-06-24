# Validar supuestos, riesgos y claridad de salida IA

## Cuándo usarlo
Durante el diseño inicial del Diseño de solución BI, antes de construir el modelo final o escribir DAX productivo.

## Prompt
"Actúa como consultor BI para entornos Tech&Eng. Con los siguientes entradas: [problema], [audiencia], [tablas disponibles], [restricciones], propone una salida estructurada para validar supuestos, riesgos y claridad de salida ia. No inventes datos, declara supuestos y marca riesgos."

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
**Título:** Validar respuesta IA en contexto minero.

**Cuándo usarlo:** después de usar IA para preguntas, KPIs, modelo o dashboard.

**Prompt:** "Evalúa esta salida IA para un caso Tech&Eng minero. Revisa si inventa datos, si respeta el schema, si distingue mina/planta/mantenimiento/energía/HSE, si la recomendación es accionable, si declara supuestos y si evita datos reales. Devuelve riesgos y correcciones."

**Inputs requeridos:** salida IA, schema o lista de tablas, audiencia.

**Output esperado:** checklist con riesgos, correcciones y decisión de aceptar/rechazar.

**Checklist de validación humana:** confirmar tablas, columnas, definiciones y privacidad.

**Advertencia de privacidad:** eliminar cualquier dato real antes de pegar contenido.
