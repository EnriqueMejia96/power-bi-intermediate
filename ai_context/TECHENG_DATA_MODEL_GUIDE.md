# Guía del Modelo de Datos Tech&Eng

## Propósito
Orientar el uso de hechos, dimensiones, llaves y relaciones para un futuro modelo estrella.

## Cómo se usa en el repositorio
Este archivo actúa como memoria operativa para instructores, estudiantes y futuros agentes. Debe leerse antes de ampliar materiales, cambiar el dataset o proponer automatizaciones.

## Decisiones tomadas
Se crean 8 tablas de hechos y 11 dimensiones con IDs consistentes.

## Decisiones pendientes
Optimizar cardinalidades y relaciones inactivas cuando se diseñe el modelo en Power BI.

## Reglas para futuros agentes
- Trabajar exclusivamente dentro de `power-bi-intermediate`.
- No usar datos reales, credenciales, APIs externas de IA ni servicios cloud.
- No crear archivos `.pbix`; Power BI Desktop se opera manualmente.
- Mantener el repositorio en español profesional, salvo nombres de variables, carpetas y código.
- Preservar el esquema común de Dataset A y Dataset B.

## Conexión con el Módulo 1
Permite explicar por qué la arquitectura precede al DAX y a los visuales.

## Conexión con los módulos 2-6
Los módulos posteriores deben reutilizar el dataset integrado, profundizar de manera incremental y evitar rediseñar la arquitectura base salvo que exista una razón pedagógica documentada.

## Lectura minera del modelo
Las dimensiones describen procesos mineros, activos, ubicaciones, servicios, prioridades, estados, responsables y proyectos. Las tablas de hechos registran proyectos, órdenes, costos, SLA, mantenimiento, incidentes HSE, energía y productividad por turno.

Para Power BI, el modelo debe seguir una lógica estrella: dimensiones filtrando hechos, fechas controladas por `Dim_Fecha`, y análisis por área, equipo, servicio, prioridad, turno y ubicación. No comparar output entre áreas sin explicar la unidad operacional.
