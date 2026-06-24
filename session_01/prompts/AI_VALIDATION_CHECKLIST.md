# Checklist de Validación de IA

Antes de aceptar una respuesta generada por IA, validar:

| Criterio | Pregunta | Estado |
|---|---|---|
| Privacidad | ¿No contiene datos reales ni sensibles? | |
| Schema | ¿Usa solo tablas/columnas existentes? | |
| Decisión | ¿La recomendación habilita una acción concreta? | |
| KPI | ¿Tiene fórmula, periodo y audiencia? | |
| Supuestos | ¿Declara lo que no sabe? | |
| Visual | ¿El visual responde a la pregunta? | |
| Riesgo | ¿Advierte posibles interpretaciones erróneas? | |
| Validación | ¿Qué debe revisar una persona antes de usarlo? | |

## Señales de alerta
- La IA inventa columnas.
- Propone KPIs sin fórmula.
- Sugiere visuales decorativos.
- Usa lenguaje absoluto sin evidencia.
- Omite privacidad o calidad de datos.

## Validación específica para minería
- ¿La salida distingue mina, planta, mantenimiento, energía, HSE y OT?
- ¿Evita usar nombres reales de faenas, personas o empresas?
- ¿Explica si `ActualOutput` y `OutputUnits` son comparables entre áreas?
- ¿Evita revelar causas raíz instructor-only del Dataset B?
- ¿Propone decisiones accionables para la audiencia minera indicada?
