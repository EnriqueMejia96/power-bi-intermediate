# Revisión de Código

## Propósito
Definir criterios para revisar cambios en generadores, validadores y documentación.

## Cómo se usa en el repositorio
Este archivo actúa como memoria operativa para instructores, estudiantes y futuros agentes. Debe leerse antes de ampliar materiales, cambiar el dataset o proponer automatizaciones.

## Decisiones tomadas
La prioridad es seguridad local, reproducibilidad, esquema estable y pruebas.

## Decisiones pendientes
Incorporar revisión de performance si el dataset crece significativamente.

## Reglas para futuros agentes
- Trabajar exclusivamente dentro de `power-bi-intermediate`.
- No usar datos reales, credenciales, APIs externas de IA ni servicios cloud.
- No crear archivos `.pbix`; Power BI Desktop se opera manualmente.
- Mantener el repositorio en español profesional, salvo nombres de variables, carpetas y código.
- Preservar el esquema común de Dataset A y Dataset B.

## Conexión con el Módulo 1
Evita romper continuidad pedagógica al modificar archivos base.

## Conexión con los módulos 2-6
Los módulos posteriores deben reutilizar el dataset integrado, profundizar de manera incremental y evitar rediseñar la arquitectura base salvo que exista una razón pedagógica documentada.
