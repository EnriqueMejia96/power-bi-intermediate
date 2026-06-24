# Empieza Aquí Después de Generar los Datos

Si ya ejecutaste:

```bash
python scripts/python/generate_data.py --dataset all
python scripts/python/validate_data.py --dataset all
python scripts/python/generate_dictionary.py --dataset all
python scripts/python/profile_data.py --dataset all
```

y viste `training: OK` y `project: OK`, el repositorio está listo para ejecutar el laboratorio del Módulo 1.

## Orden recomendado de lectura
1. `session_01/README_SESSION_01.md`
2. `session_01/lab/LAB_GUIDE.md`
3. `session_01/lab/LAB_STEPS.md`
4. `data/training/dictionary/data_dictionary.md`
5. `powerbi/manual_steps/import_csv_files.md`
6. `session_01/templates/BI_SOLUTION_BLUEPRINT_TEMPLATE.md`

## Orden recomendado de ejecución
### Paso 1: elegir una línea de análisis
Para empezar rápido, usa SLA:

- Pregunta guía: ¿qué áreas y servicios concentran incumplimientos SLA?
- Hecho principal: `Fact_SLA`.
- Dimensiones: `Dim_Area`, `Dim_Servicio`, `Dim_Prioridad`, `Dim_Fecha`.

### Paso 2: abrir Power BI Desktop
Crear un archivo en blanco. No guardar `.pbix` dentro del repositorio si no lo pide el instructor.

### Paso 3: importar CSV
Desde `data/training/sample`, importa:

- `Dim_Fecha.csv`
- `Dim_Area.csv`
- `Dim_Servicio.csv`
- `Dim_Prioridad.csv`
- `Fact_SLA.csv`

### Paso 4: revisar Power Query
Solo verifica nombres y tipos. No hagas limpieza profunda todavía.

### Paso 5: revisar Vista de modelo
Crea o valida estas relaciones:

- `Dim_Area[AreaID]` -> `Fact_SLA[AreaID]`
- `Dim_Servicio[ServiceID]` -> `Fact_SLA[ServiceID]`
- `Dim_Prioridad[PriorityID]` -> `Fact_SLA[PriorityID]`
- `Dim_Fecha[DateKey]` -> `Fact_SLA[CreatedDateKey]`

### Paso 6: crear una página mínima
Visuales mínimos:

- Tarjeta: conteo de `SLAID`.
- Tarjeta: promedio de `BreachHours`.
- Barras: incumplimientos por `AreaName`.
- Barras o matriz: incumplimientos por `ServiceName` y `PriorityName`.
- Slicer: `PriorityName`.

### Paso 7: completar plano de solución
Abre `session_01/templates/BI_SOLUTION_BLUEPRINT_TEMPLATE.md` y completa al menos:

- Problema.
- Pregunta medible.
- Audiencia.
- KPIs.
- Tablas requeridas.
- Boceto.
- Riesgos de datos.
- Uso de IA y validación humana.

## Qué deberías tener al terminar
- Entiendes qué hace cada capa de Power BI.
- Tienes una pregunta medible.
- Tienes un KPI principal y 2 KPIs diagnóstico.
- Tienes una página exploratoria simple.
- Tienes un plano de solución listo para mejorar en módulos posteriores.
