# Estrategia de Dataset Integrado

## Propósito
Explicar por qué no se crea un dataset por sesión y cómo se separan Dataset A/B.

## Cómo se usa en el repositorio
Este archivo actúa como memoria operativa para instructores, estudiantes y futuros agentes. Debe leerse antes de ampliar materiales, cambiar el dataset o proponer automatizaciones.

## Decisiones tomadas
Dataset A es entrenamiento; Dataset B comparte esquema y cambia patrones operativos.

## Decisiones pendientes
Definir casos de evaluación final más detallados sin revelar causas raíz directas.

## Reglas para futuros agentes
- Trabajar exclusivamente dentro de `power-bi-intermediate`.
- No usar datos reales, credenciales, APIs externas de IA ni servicios cloud.
- No crear archivos `.pbix`; Power BI Desktop se opera manualmente.
- Mantener el repositorio en español profesional, salvo nombres de variables, carpetas y código.
- Preservar el esquema común de Dataset A y Dataset B.

## Conexión con el Módulo 1
Da al estudiante una visión de continuidad desde recap hasta tablero final.

## Conexión con los módulos 2-6
Los módulos posteriores deben reutilizar el dataset integrado, profundizar de manera incremental y evitar rediseñar la arquitectura base salvo que exista una razón pedagógica documentada.

## Actualización minera
La estrategia se mantiene: Dataset A para entrenamiento y Dataset B para proyecto final, ambos con el mismo schema. La mejora actual no crea datasets por sesión; reemplaza valores genéricos por vocabulario y patrones Tech&Eng mineros.

Dataset A concentra señales de entrenamiento en chancado, correas, taller mina, molienda, energía y backlog. Dataset B conserva el mismo modelo, pero mueve problemas hacia dispatch, relaves, molienda, flota mina y OT para evaluar transferencia sin revelar causa raíz.
