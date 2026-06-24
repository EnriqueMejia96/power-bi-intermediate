# Diseño del dataset minero

## Propósito
Documentar la estrategia de dataset integrado y sintético para una operación Tech&Eng minera.

## Cómo se aplica a la especialización
El dataset permite trabajar seis módulos sin crear un dataset nuevo por sesión. Cada módulo profundiza sobre la misma base.

## Conexión con Power BI
La carpeta `clean` se usa para modelo estrella. La carpeta `raw` se usa para Power Query y calidad de datos.

## Conexión con el dataset
El schema conserva 11 dimensiones y 8 tablas de hechos. Las columnas no se cambian para mantener compatibilidad y tests.

## Conexión con módulos 1-6
- Sesión 1: análisis de contexto y blueprint.
- Sesión 2: problemas raw y limpieza.
- Sesión 3: modelo estrella.
- Sesión 4: DAX.
- Sesión 5: dashboard.
- Sesión 6: optimización y entrega.

## Preguntas de negocio mineras
- ¿Qué relaciones necesita el modelo para analizar downtime por equipo y área?
- ¿Qué fecha debe usarse para SLA, cierre de órdenes o seguimiento de proyectos?
- ¿Qué hechos tienen granularidades distintas?

## KPIs soportados
Producción, mantenimiento, costos, SLA, energía, seguridad, proyectos y productividad por turno.

## Riesgos de interpretación
No unir hechos entre sí sin entender granularidad. No comparar output de áreas distintas sin contexto.

## Apoyo de IA
IA puede revisar un diseño de modelo y señalar relaciones faltantes o campos ambiguos.

## Validación profesional
Validar llaves, unicidad, integridad referencial, fechas, campos nulos y significado de cada métrica.
