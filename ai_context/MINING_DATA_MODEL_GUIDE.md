# Guía de modelo de datos minero

## Propósito
Explicar cómo leer el schema común de Dataset A y Dataset B como modelo estrella para un caso minero Tech&Eng.

## Aplicación a la especialización
El modelo permite enseñar relaciones, cardinalidad, contexto de filtro, tablas de hechos, dimensiones y futuras medidas DAX.

## Conexión con Power BI
Importar CSV desde `data/training/clean` o `data/project/clean`, crear relaciones desde dimensiones hacia hechos y validar filtros por fecha, área, equipo, servicio, prioridad y ubicación.

## Conexión con el dataset
Las dimensiones describen el negocio; los hechos registran eventos, costos, SLA, energía, productividad, incidentes y proyectos. Dataset A y Dataset B comparten columnas.

## Conexión con módulos 1-6
Módulo 1 diseña modelo preliminar; Módulo 2 prepara datos; Módulo 3 lo implementa; Módulo 4 agrega medidas; Módulo 5 diseña páginas; Módulo 6 optimiza.

## Preguntas de negocio
- ¿Qué dimensiones filtran cada hecho?
- ¿Qué tabla define el eje temporal de cada análisis?
- ¿Qué nivel de granularidad tiene cada tabla?
- ¿Dónde puede aparecer duplicidad o relación ambigua?

## KPIs afectados por el modelo
Todos los KPIs dependen de relaciones correctas. Ejemplos: SLA por área, downtime por equipo, costo por proyecto, energía por turno y productividad por ubicación.

## Riesgos de interpretación
No sumar porcentajes sin ponderar. No mezclar hechos con granularidades distintas sin una pregunta clara. Evitar relaciones bidireccionales salvo justificación didáctica.

## Cómo puede ayudar IA
IA puede revisar si una propuesta de modelo respeta estrella, detectar relaciones faltantes y explicar granularidad a usuarios de negocio.

## Qué debe validar el profesional
Cardinalidad, dirección de filtro, unicidad de claves, fechas activas, nulos y consistencia de IDs.
