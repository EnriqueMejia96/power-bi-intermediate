# Guía de Laboratorio - Módulo 1

## Objetivo
Diseñar un plano de solución inicial de solución BI para una organización Tech&Eng ficticia. El laboratorio conecta negocio, datos, Power BI Desktop, KPIs, audiencia, boceto e IA asistida.

## Duración sugerida
75 minutos dentro de la sesión de 2 horas.

## Preparación del instructor
1. Ejecutar generación y validación de datos.
2. Confirmar que existen los CSV en `data/training/sample`.
3. Abrir previamente `data/training/dictionary/data_dictionary.md`.
4. Tener Power BI Desktop disponible para demostración, si se usará en vivo.
5. Recordar que no se necesita Power BI Service ni credenciales.

## Preparación del estudiante
1. Tener el repositorio abierto en su equipo.
2. Confirmar que el dataset fue generado.
3. Abrir `session_01/templates/BI_SOLUTION_BLUEPRINT_TEMPLATE.md`.
4. Abrir Power BI Desktop manualmente.

## Dataset a usar
Para Módulo 1 se recomienda usar `data/training/sample`, porque permite importar rápido y concentrarse en arquitectura. Si el equipo tiene buen rendimiento, usar `data/training/clean`.

Tablas sugeridas para importar:

- `Dim_Fecha.csv`
- `Dim_Area.csv`
- `Dim_Equipo.csv`
- `Fact_OrdenesTrabajo.csv`
- `Fact_SLA.csv`
- `Fact_Costos.csv`

## Caso de negocio
Una organización Tech&Eng gestiona proyectos, órdenes de trabajo, mantenimiento, costos, SLA, seguridad, energía y productividad. La gerencia necesita visibilidad para detectar desviaciones, priorizar acciones y reducir riesgo operativo.

## Actividades
### Actividad 1: revisar escenario de negocio
Leer `data/training/metadata/business_scenario.md`. Identificar 2 problemas posibles:

- Backlog creciente.
- Caída de SLA.
- Sobrecostos.
- Mantenimiento correctivo concentrado.
- Acciones correctivas abiertas.
- Consumo energético anormal.
- Productividad variable.

### Actividad 2: revisar diccionario de datos
Abrir `data/training/dictionary/data_dictionary.md`. Ubicar qué tablas responderían a una pregunta inicial.

Ejemplo:

- Pregunta: ¿qué áreas concentran incumplimientos SLA?
- Tablas: `Fact_SLA`, `Dim_Area`, `Dim_Servicio`, `Dim_Prioridad`, `Dim_Fecha`.

### Actividad 3: abrir Power BI Desktop manualmente
No se automatiza Power BI. El estudiante abre Desktop, crea un archivo en blanco y usa **Obtener datos > Texto/CSV**.

### Actividad 4: importar 3-5 tablas de muestra
Importar primero dimensiones y luego hechos. Revisar que las tablas aparecen en el panel de datos.

### Actividad 5: reconocer vistas
- Power Query: preparación y tipos de datos.
- Vista de modelo: relaciones y modelo semántico.
- Vista de informe: visualización orientada a decisiones.

### Actividad 6: convertir problema en pregunta medible
Usar el canvas de pregunta de negocio. Una pregunta buena incluye métrica, periodo, dimensión y decisión.

Mala pregunta: "¿Cómo estamos en operaciones?"

Buena pregunta: "¿Qué áreas tienen mayor porcentaje de órdenes abiertas o vencidas durante el último trimestre y qué prioridad concentran?"

### Actividad 7: diseñar KPIs
Definir al menos 3 KPIs preliminares. Ejemplos:

- `% SLA cumplido = órdenes SLA cumplidas / órdenes SLA evaluadas`.
- `Backlog abierto = órdenes no cerradas`.
- `Variación de costo = costo real - presupuesto`.
- `Downtime promedio = horas de parada / eventos de mantenimiento`.

### Actividad 8: definir audiencia
Identificar si el tablero será para gerencia, jefe de operaciones, planner, supervisor HSE, responsable de energía o analista BI. Cada audiencia necesita otro nivel de detalle.

### Actividad 9: crear boceto inicial
Dibujar una página simple con:

- Fila superior: 3-5 KPIs.
- Zona central: tendencia y comparación por área.
- Zona lateral: filtros clave.
- Zona inferior: tabla de detalle para acciones.

### Actividad 10: usar IA para revisar el plano de solución
Usar un prompt de `session_01/prompts/AI_PROMPT_LIBRARY_SESSION_01.md`. No compartir datos reales. Pedir revisión de claridad, supuestos, riesgos y vacíos.

## Entregable final
Completar `BI_SOLUTION_BLUEPRINT_TEMPLATE.md` con una propuesta defendible, aunque todavía sea preliminar.

## Criterio de éxito
El laboratorio es exitoso si el estudiante puede explicar por qué cada tabla, KPI y visual existe en función de una decisión.

## Caso minero base
Diseña el blueprint para una operación minera con señales de bajo rendimiento en Chancado Primario, backlog en Taller Mina, consumo energético anormal en Molienda y acciones HSE pendientes. No busques la causa raíz definitiva todavía: en Módulo 1 basta con estructurar preguntas, KPIs, datos, audiencia, páginas y validaciones.
