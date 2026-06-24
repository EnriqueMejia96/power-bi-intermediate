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

## Prompts mineros recomendados

### 1. Convertir problema minero en preguntas medibles
- Cuándo usarlo: al inicio del blueprint.
- Prompt: "Convierte este problema minero en 5 preguntas medibles para Power BI: bajo rendimiento en chancado, backlog de mantenimiento, consumo energético anormal y acciones HSE pendientes. Para cada pregunta indica audiencia, decisión, KPI principal, tabla probable y riesgo de interpretación."
- Inputs requeridos: problema, audiencia tentativa, tablas disponibles.
- Output esperado: preguntas medibles y priorizadas.
- Checklist humano: validar si la audiencia puede actuar y si el KPI existe en el schema.
- Privacidad: usar solo datos sintéticos.

### 2. Diseñar KPIs mineros
- Cuándo usarlo: después de definir pregunta de negocio.
- Prompt: "Diseña KPIs para producción, mantenimiento, SLA, energía y HSE usando el dataset Tech&Eng minero. Incluye definición, fórmula conceptual, tablas, columnas, audiencia, decisión y riesgo."
- Inputs requeridos: pregunta, área minera, objetivo.
- Output esperado: árbol de KPIs.
- Checklist humano: validar denominador, unidad y granularidad.
- Privacidad: no incluir nombres reales.

### 3. Clasificar KPIs por audiencia minera
- Prompt: "Clasifica estos KPIs por audiencia minera: gerencia, operaciones, mantenimiento, energía, HSE y analista BI. Indica frecuencia, nivel de detalle, acción esperada y visual recomendado."
- Inputs requeridos: lista de KPIs.
- Output esperado: matriz audiencia-KPI.
- Checklist humano: confirmar dueño de decisión.
- Privacidad: datos sintéticos o anonimizados.

### 4. Definir datos requeridos
- Prompt: "Para analizar mantenimiento, producción, seguridad y energía en una operación minera sintética, mapea tablas y columnas necesarias del schema. Separa dimensiones, hechos, fechas, métricas y riesgos raw vs clean."
- Inputs requeridos: pregunta y tablas.
- Output esperado: matriz de requerimientos.
- Checklist humano: validar relaciones y llaves.
- Privacidad: no usar datos reales.

### 5. Proponer estructura de dashboard minero
- Prompt: "Propón una estructura de dashboard Power BI para priorizar decisiones ante bajo output, backlog, consumo energético anormal y acciones HSE pendientes. Incluye páginas, KPIs, visuales, filtros, drill-through y tooltips."
- Inputs requeridos: audiencia y KPIs.
- Output esperado: wireframe textual.
- Checklist humano: cada visual debe responder una pregunta.
- Privacidad: no cargar CSV reales en herramientas externas.

### 6. Wireframe de operaciones mina
- Prompt: "Diseña un wireframe de operaciones mina/planta con plan vs real, productividad por turno, brecha por área, tabla de detalle y filtros. Justifica cada visual."
- Inputs requeridos: audiencia, periodo, áreas.
- Output esperado: layout de página.
- Checklist humano: revisar unidad de ActualOutput.
- Privacidad: solo contexto sintético.

### 7. Wireframe de planta concentradora
- Prompt: "Diseña un wireframe para planta concentradora enfocado en chancado, correas, molienda, energía y mantenimiento. Incluye KPIs, visuales, filtros y riesgos de interpretación."
- Inputs requeridos: procesos y KPIs.
- Output esperado: layout y lógica de navegación.
- Checklist humano: validar si compara áreas compatibles.
- Privacidad: no usar nombres reales de faenas.

### 8. Revisar blueprint BI minero
- Prompt: "Revisa este blueprint BI minero. Evalúa claridad del problema, pregunta medible, KPIs, datos, audiencia, páginas, uso de IA, validación humana y riesgos. Devuelve mejoras accionables."
- Inputs requeridos: blueprint.
- Output esperado: revisión crítica.
- Checklist humano: aceptar solo observaciones justificadas.
- Privacidad: remover datos sensibles antes de pegar.

### 9. Resumen ejecutivo
- Prompt: "Genera un resumen ejecutivo de 150 palabras para gerencia de operaciones mineras. Debe mencionar riesgo operacional, KPI principal, áreas afectadas, decisión esperada y validaciones pendientes."
- Inputs requeridos: hallazgos y KPIs.
- Output esperado: resumen ejecutivo.
- Checklist humano: no agregar hechos no observados.
- Privacidad: mantener todo sintético.

### 10. Detectar riesgos de interpretación
- Prompt: "Lista riesgos de interpretación para estos KPIs mineros: producción %, downtime, SLA %, kWh/output y acciones HSE vencidas. Incluye cómo mitigarlos en Power BI."
- Inputs requeridos: KPIs y audiencia.
- Output esperado: matriz riesgo-mitigación.
- Checklist humano: validar supuestos de negocio.
- Privacidad: no usar información confidencial.
