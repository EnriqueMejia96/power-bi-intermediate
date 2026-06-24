# Biblioteca de Prompts IA - Sesión 01

## Reglas de uso
- No pegues datos reales ni información confidencial.
- Usa descripciones y nombres sintéticos.
- Pide supuestos explícitos.
- Valida toda recomendación con criterio de negocio.

## Prompt 1: convertir problema en preguntas medibles
**Cuándo usarlo:** al inicio del plano de solución.

**Prompt:**
"Actúa como consultor senior de Business Intelligence para entornos Tech&Eng. Tengo este problema sintético: [problema]. La audiencia es [audiencia] y las tablas disponibles son [tablas]. Propón 5 preguntas analíticas medibles. Para cada una incluye métrica, periodo, dimensión de análisis, decisión que habilita, tablas necesarias y riesgos de interpretación. No inventes columnas fuera del esquema."

**Output esperado:** tabla priorizada de preguntas.

**Validación humana:** confirmar que la decisión es realista para la audiencia.

## Prompt 2: diseñar KPIs
"Con esta pregunta medible: [pregunta], diseña un árbol de KPIs. Incluye KPI principal, KPIs diagnóstico, fórmula tentativa en lenguaje natural, dimensiones de corte, umbral sugerido y acción esperada. Marca supuestos y datos faltantes."

## Prompt 3: mapear datos requeridos
"Usando estas tablas del dataset Tech&Eng: [tablas], mapea qué columnas usarías para responder [pregunta]. Separa dimensiones, hechos, fechas y métricas. Indica riesgos de calidad que deberían revisarse en Power Query."

## Prompt 4: diseñar boceto
"Diseña un boceto textual para una página de Power BI dirigida a [audiencia]. La pregunta principal es [pregunta]. Incluye KPIs superiores, visual de tendencia, visual de comparación, filtros, tabla de detalle y acción esperada. Justifica cada visual."

## Prompt 5: revisar plano de solución
"Revisa este Diseño de solución BI: [pegar plano de solución]. Evalúa claridad de problema, pregunta medible, KPI, audiencia, datos requeridos, riesgos de calidad, diseño de página y uso responsable de IA. Devuelve observaciones críticas y recomendaciones accionables."

## Prompt 6: resumen ejecutivo
"Crea un resumen ejecutivo de máximo 150 palabras para este plano de solución. Debe mencionar problema, KPI principal, audiencia, decisión esperada y riesgos pendientes. No agregues información que no esté en el plano de solución."

## Herramientas sugeridas
Microsoft Copilot for Power BI, Microsoft Copilot for Microsoft 365, Power BI Q&A, ChatGPT, Gemini, Claude, Perplexity, Excel Copilot o IA en hojas de cálculo.
