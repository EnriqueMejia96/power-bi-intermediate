# Importar Archivos CSV en Power BI Desktop

## Propósito
Importar un subconjunto del dataset sintético para practicar el flujo Power BI sin perder tiempo cargando todas las tablas. En Módulo 1 el objetivo no es construir el modelo completo, sino reconocer cómo un problema de negocio llega a datos, relaciones y visuales.

## Ruta de trabajo
Usar preferentemente:

`data/training/sample`

Si la máquina tiene buen rendimiento y el instructor lo indica, usar:

`data/training/clean`

## Tablas para el ejercicio SLA
Importar en este orden:

1. `Dim_Fecha.csv`
2. `Dim_Area.csv`
3. `Dim_Servicio.csv`
4. `Dim_Prioridad.csv`
5. `Fact_SLA.csv`

## Pasos detallados
1. Abrir Power BI Desktop.
2. Seleccionar **Obtener datos**.
3. Elegir **Texto/CSV**.
4. Navegar a `data/training/sample`.
5. Seleccionar `Dim_Area.csv`.
6. En la vista previa, confirmar que las columnas se ven separadas correctamente.
7. Elegir **Transformar datos** si quieres revisar Power Query; elegir **Cargar** si solo harás importación rápida.
8. Repetir con las demás tablas.
9. Aplicar cambios.

## Revisión inmediata después de importar
- `Dim_Area` debe tener `AreaID` y `AreaName`.
- `Dim_Servicio` debe tener `ServiceID` y `ServiceName`.
- `Dim_Prioridad` debe tener `PriorityID` y `PriorityName`.
- `Fact_SLA` debe tener `SLAID`, `AreaID`, `ServiceID`, `PriorityID`, `CreatedDateKey`, `SLAMetFlag` y `BreachHours`.

## Problemas comunes
| Problema | Causa probable | Acción |
|---|---|---|
| Power BI interpreta IDs como números | Columna parece numérica | Cambiar a texto si tiene prefijo o debe preservar ceros |
| No aparece relación automática | Tipos distintos o autode detección deshabilitada | Crear relación manual |
| Carga lenta | Dataset completo importado | Usar archivos de muestra (`sample`) |
| Fechas no se reconocen | `DateKey` es entero YYYYMMDD | Mantener como llave; usar `Dim_Fecha[Date]` para calendario |

## Cierre
Al terminar, debes tener las tablas cargadas y listas para revisar relaciones en Vista de modelo.
