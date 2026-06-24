# Power BI + Analítica Empresarial Asistida por IA para Entornos Tech&Eng

Repositorio base del **Módulo 1: Arquitectura analítica y recap Power BI**. Prepara datos sintéticos, guías, plantillas, prompts y pruebas locales para una sesión intermedia de 2 horas orientada a profesionales Tech&Eng.

## Objetivo
Enseñar Power BI como ciclo analítico completo: problema de negocio -> datos -> Power Query -> modelo semántico -> DAX -> visuales -> hallazgos -> decisiones.

## Audiencia
Profesionales de ingeniería, operaciones, mantenimiento, servicios técnicos, supervisión, proyectos y análisis de negocio que ya conocen Power BI básico y necesitan diseñar soluciones BI con criterio arquitectónico.

## Alcance del Módulo 1
El módulo es un recap funcional y estratégico. No implementa tableros finales, no crea `.pbix`, no publica en Power BI Service y no depende de APIs externas.

## Qué aprenderá el estudiante
- Diferenciar Power Query, modelo, DAX y visualización.
- Convertir problemas operativos en preguntas medibles.
- Definir KPIs preliminares y audiencia del tablero.
- Crear un Diseño de solución BI inicial.
- Usar IA como apoyo de diseño sin delegar validación de negocio.

## Estructura de la especialización
1. Arquitectura analítica y recap Power BI.
2. Power Query y calidad de datos.
3. Modelamiento con modelo estrella.
4. DAX para KPIs de negocio.
5. Tableros y narrativa de datos.
6. Optimización, publicación y proyecto.
7. Proyecto final: Tablero Integral de Desempeño Tech&Eng.

## Dataset sintético integrado
El repositorio usa una estrategia unificada:

- **Dataset A (`data/training`)**: entrenamiento progresivo para sesiones 1-6, con datos crudos (`raw`), datos limpios (`clean`), diccionario, metadatos, problemas controlados y muestras (`sample`).
- **Dataset B (`data/project`)**: proyecto final con el mismo esquema, valores diferentes y patrones operativos distintos para evaluar transferencia.

## Uso local
1. Crear ambiente Python opcional: `python -m venv .venv`.
2. Instalar dependencias: `python -m pip install -r requirements.txt`.
3. Generar datos: `python scripts/python/generate_data.py --dataset all`.
4. Validar datos: `python scripts/python/validate_data.py --dataset all`.
5. Generar diccionario: `python scripts/python/generate_dictionary.py --dataset all`.
6. Perfilar datos: `python scripts/python/profile_data.py --dataset all`.
7. Ejecutar pruebas: `python -m pytest`.

Si `make` está disponible, se pueden usar los objetivos declarados en el `Makefile`: `make setup`, `make check-env`, `make data`, `make validate-data`, `make data-dictionary`, `make profile-data`, `make session01-materials` y `make test`.

## Power BI Desktop
Power BI Desktop se usa manualmente. Las guías en `powerbi/manual_steps` explican cómo importar CSV, reconocer Power Query, revisar Vista de modelo y crear visuales básicos. El repositorio no genera archivos `.pbix`.

## IA asistida
Los prompts en `ai_tools/` y `session_01/prompts/` sirven para diseñar preguntas, KPIs, bocetos y validaciones. No se llama ninguna API de IA desde el código. No subas datos reales, contratos, clientes ni personas reales a herramientas externas.

## Estado actual
- Repositorio base del Módulo 1 preparado.
- Dataset A implementado con datos crudos (`raw`), datos limpios (`clean`), muestras (`sample`), metadatos y diccionario.
- Dataset B implementado con mismo esquema y patrones distintos.
- Implementación Power BI manual.
- Módulos 2-6 pendientes.

## Próximos pasos
Prompt 2 debería profundizar en Power Query y calidad de datos usando `data/training/raw`, sin cambiar el esquema base ni crear un dataset nuevo por sesión.
