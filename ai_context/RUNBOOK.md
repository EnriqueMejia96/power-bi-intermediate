# Guía operativa local

## Propósito
Describir el flujo operativo para generar, validar, perfilar y usar datos.

## Cómo se usa en el repositorio
Este archivo actúa como memoria operativa para instructores, estudiantes y futuros agentes. Debe leerse antes de ampliar materiales, cambiar el dataset o proponer automatizaciones.

## Decisiones tomadas
El flujo local estándar es check-env, data, validate-data, diccionario, perfil y pruebas.

## Decisiones pendientes
Automatizar más reportes solo si no aumenta dependencia de herramientas externas.

## Reglas para futuros agentes
- Trabajar exclusivamente dentro de `power-bi-intermediate`.
- No usar datos reales, credenciales, APIs externas de IA ni servicios cloud.
- No crear archivos `.pbix`; Power BI Desktop se opera manualmente.
- Mantener el repositorio en español profesional, salvo nombres de variables, carpetas y código.
- Preservar el esquema común de Dataset A y Dataset B.

## Conexión con el Módulo 1
Da al instructor una ruta repetible antes de iniciar la sesión.

## Conexión con los módulos 2-6
Los módulos posteriores deben reutilizar el dataset integrado, profundizar de manera incremental y evitar rediseñar la arquitectura base salvo que exista una razón pedagógica documentada.
