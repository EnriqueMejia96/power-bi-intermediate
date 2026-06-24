# Vista de informe Repaso rápido

## Propósito
Crear una página exploratoria mínima para conectar datos con una pregunta de negocio. No es el tablero final.

## Pregunta de ejemplo
¿Qué áreas y servicios concentran incumplimientos SLA y dónde debería priorizarse la revisión operativa?

## Visuales mínimos
| Visual | Campos | Propósito |
|---|---|---|
| Tarjeta | Conteo de `SLAID` | Volumen total analizado |
| Tarjeta | Promedio de `BreachHours` | Magnitud del incumplimiento |
| Barras | `AreaName` + conteo de incumplimientos | Priorizar áreas |
| Barras apiladas o matriz | `ServiceName`, `PriorityName` | Diagnóstico |
| Slicer | `PriorityName` | Explorar severidad |
| Tabla | `SLAID`, `AreaName`, `ServiceName`, `BreachHours` | Ver detalle accionable |

## Medidas simples para Módulo 1
Puedes usar agregaciones automáticas para explorar. En Módulo 4 se reemplazarán por medidas DAX formales.

## Diseño recomendado
- Título orientado a pregunta.
- KPIs arriba.
- Gráfico principal al centro.
- Filtros al lado o arriba.
- Detalle abajo.

## Preguntas de revisión
- ¿El visual muestra una prioridad de acción?
- ¿La audiencia entendería qué hacer después?
- ¿El filtro cambia correctamente todos los visuales?
- ¿Hay visuales decorativos que no aportan?
