# Guía operativa local

## Propósito
Describir el flujo operativo para generar, validar, perfilar y usar datos.

## Cómo se usa en el repositorio
Este archivo actúa como memoria operativa para instructores, estudiantes y futuros agentes. Debe leerse antes de ampliar materiales, cambiar el dataset o proponer automatizaciones.

## Decisiones tomadas
El flujo local estándar es check-env, data-mining, validate-data, validate-mining, diccionario, perfil, reportes mineros y pruebas.

## Flujo local recomendado
```bash
make setup
make check-env
make data-mining
make validate-data
make validate-mining
make data-dictionary
make profile-data
make profile-mining
make mining-report
make session01-materials
make test
```

Si `make` no está disponible, usar los comandos Python equivalentes:

```bash
python scripts/python/generate_data.py --dataset all
python scripts/python/validate_data.py --dataset all
python scripts/python/generate_dictionary.py --dataset all
python scripts/python/profile_data.py --dataset all
python scripts/python/generate_mining_reports.py --report all
python -m pytest
```

## Reportes mineros
- `reports/dataset_profile/MINING_GAP_ASSESSMENT.md`
- `reports/dataset_profile/MINING_DOMAIN_COVERAGE_REPORT.md`
- `reports/dataset_profile/MINING_DATA_QUALITY_REPORT.md`
- `reports/dataset_profile/MINING_ROOT_CAUSE_PATTERNS_INSTRUCTOR.md`
- `reports/session_01/MINING_SESSION_01_READINESS.md`

## Decisiones pendientes
Automatizar más reportes solo si no aumenta dependencia de herramientas externas.

## Reglas para futuros agentes
- Trabajar exclusivamente dentro de `power-bi-intermediate`.
- No usar datos reales, credenciales, APIs externas de IA ni servicios cloud.
- No crear archivos `.pbix`; Power BI Desktop se opera manualmente.
- Mantener el repositorio en español profesional, salvo nombres de variables, carpetas y código.
- Preservar el esquema común de Dataset A y Dataset B.
- Mantener el enfoque Tech&Eng minero sin crear datasets por sesión.
- Mantener causa raíz de Dataset B en archivos instructor-only.

## Conexión con el Módulo 1
Da al instructor una ruta repetible antes de iniciar la sesión.

## Conexión con los módulos 2-6
Los módulos posteriores deben reutilizar el dataset integrado, profundizar de manera incremental y evitar rediseñar la arquitectura base salvo que exista una razón pedagógica documentada.
