# Importar Datos Sample en Power BI Desktop

## Ruta recomendada
`data/training/sample`

## Tablas sugeridas
- `Dim_Fecha.csv`
- `Dim_Area.csv`
- `Dim_Servicio.csv`
- `Dim_Prioridad.csv`
- `Fact_SLA.csv`

## Pasos
1. Power BI Desktop > Obtener datos > Texto/CSV.
2. Seleccionar el primer archivo.
3. Revisar vista previa.
4. Elegir Transformar datos si se quiere revisar Power Query.
5. Repetir con el resto de tablas.
6. Aplicar cambios.

## Validaciones rápidas
- `DateKey` debe leerse como entero o texto consistente.
- IDs como `AreaID` y `ServiceID` deben coincidir entre dimensiones y hechos.
- No convertir IDs a número si tienen prefijos como `A001`.

## Nota
Usar archivos de muestra evita fricción. El dataset limpio completo está en `data/training/clean`.
