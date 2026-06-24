# Notas del Instructor

## Enfoque pedagógico
Este módulo debe sentirse como una transición de usuario de Power BI a arquitecto analítico. La conversación no debe quedarse en botones. Cada acción en Power BI debe responder a una razón de negocio.

## Apertura sugerida
"Hoy no venimos a hacer un tablero bonito. Venimos a diseñar la lógica que hace que un tablero sea confiable: qué problema resuelve, qué datos necesita, qué modelo lo sostiene, qué KPI traduce la operación y qué decisión habilita."

## Conceptos que conviene aterrizar
- **Power Query**: capa de preparación. Corrige estructura, tipos, nombres, columnas y granularidad.
- **Modelo semántico**: capa de significado. Relaciona hechos y dimensiones.
- **DAX**: capa de métricas. Convierte datos en indicadores reutilizables.
- **Visualización**: capa de decisión. Ordena información para una audiencia.

## Errores frecuentes a interceptar
- Preguntas demasiado amplias: "¿cómo va la operación?"
- KPIs sin fórmula ni periodo.
- Importar todas las tablas sin saber para qué.
- Dejar que Power BI auto-relacione todo sin revisar.
- Copiar una salida de IA sin cuestionarla.

## Preguntas para facilitar discusión
- ¿Qué decisión tomaría una persona con este tablero?
- ¿Qué indicador alertaría antes de que el problema sea visible en costos?
- ¿Qué dimensiones permitirían explicar la desviación?
- ¿Qué riesgo aparece si la fecha, estado o prioridad viene inconsistente?
- ¿Qué parte de esta respuesta de IA necesita validación humana?

## Puente hacia Módulo 2
Cuando aparezcan errores en datos crudos (`raw`), no resolverlos completos. Decir: "Excelente, ese es exactamente el material del siguiente módulo: Power Query y calidad de datos."

## Caso minero para facilitar
Usar como hilo conductor: bajo rendimiento en Chancado Primario, backlog en Taller Mina, consumo energético anormal en Molienda y acciones HSE pendientes. Guiar con preguntas, no con respuestas. Si un estudiante salta directo a causa raíz, pedir evidencia cruzada en productividad, mantenimiento, SLA, energía, costos y seguridad.

Mantener `MINING_ROOT_CAUSE_PATTERNS_INSTRUCTOR.md` como instructor-only; no compartirlo con estudiantes.
