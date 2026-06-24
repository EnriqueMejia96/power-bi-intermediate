# Diccionario de datos - Dataset A - entrenamiento

Datos 100% sintéticos para un caso Tech&Eng minero. El esquema es común para Dataset A y Dataset B.

## Cómo leer este diccionario
- **PK** identifica una fila única dentro de una tabla.
- **FK** conecta una tabla de hechos con una dimensión o con otra tabla transaccional.
- **Granularidad** indica qué representa una fila.
- **Clean** está listo para modelo estrella; **raw** conserva errores controlados para prácticas de Power Query.
- Dataset A y Dataset B comparten columnas, pero no comparten exactamente los mismos patrones operacionales.

## Diferencia Dataset A vs Dataset B
- Dataset A concentra patrones de entrenamiento en chancado, correas, taller mina, molienda y energía.
- Dataset B usa el mismo esquema, pero concentra problemas distintos en dispatch, relaves, molienda, flota mina y OT.
- Las causas raíz del Dataset B no deben entregarse al estudiante; sirven para evaluar transferencia.

## Dim_Fecha
Calendario para inteligencia de tiempo en operaciones mineras, mantenimiento, energia, seguridad y proyectos.

- Granularidad: Una fila por día calendario.
- Relaciones: Fact_Proyectos.DateKey -> DateKey; Fact_OrdenesTrabajo.CreatedDateKey -> DateKey; Fact_Costos.DateKey -> DateKey; Fact_SLA.CreatedDateKey -> DateKey; Fact_Mantenimiento.DateKey -> DateKey; Fact_Incidentes.DateKey -> DateKey; Fact_Energia.DateKey -> DateKey; Fact_Productividad.DateKey -> DateKey

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| DateKey | PK | Clave de fecha en formato yyyymmdd. Permite relacionar hechos con Dim_Fecha sin depender de formatos regionales. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| Date | Atributo | Fecha calendario legible. Se usa para filtros, ejes temporales y validación de rangos. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| Year | Atributo | Año calendario. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| Quarter | Atributo | Trimestre calendario. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| MonthNumber | Atributo | Número de mes entre 1 y 12. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| MonthName | Atributo | Nombre del mes en español. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| WeekNumber | Atributo | Número de semana ISO aproximado para análisis semanal. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| DayOfWeek | Atributo | Día de la semana en español. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| IsWeekend | Atributo | Indica si la fecha cae en fin de semana. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |

## Dim_Area
Areas sinteticas de una operacion minera Tech&Eng: mina, planta concentradora, relaves, mantenimiento, energia, HSE y OT.

- Granularidad: Una fila por área o proceso minero sintético.
- Relaciones: Dim_Equipo.AreaID -> AreaID; LocationID -> Dim_Ubicacion.LocationID; Dim_Proyecto.AreaID -> AreaID; Fact_Proyectos.AreaID -> AreaID; Fact_OrdenesTrabajo.AreaID -> AreaID; Fact_SLA.AreaID -> AreaID; Fact_Mantenimiento.AreaID -> AreaID; Fact_Incidentes.AreaID -> AreaID; Fact_Energia.AreaID -> AreaID; Fact_Productividad.AreaID -> AreaID

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| AreaID | PK | Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| AreaName | Atributo | Nombre del proceso o área minera sintética, por ejemplo Chancado Primario, Molienda o Taller Mina. | Chancado Primario; Molienda; Espesamiento y Relaves | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| BusinessUnit | Atributo | Unidad de negocio o superintendencia sintética a la que pertenece el área. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| AreaType | Atributo | Tipo analítico del área: Mina, Planta, Mantenimiento, Servicios, Seguridad, Ingeniería o Soporte Operacional. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| ManagerName | Atributo | Nombre sintético del responsable de gestión del área. No representa personas reales. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| LocationID | FK | Clave de ubicación. En dimensiones es identificador; en hechos permite analizar por lugar físico de faena. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |

## Dim_Equipo
Activos mineros e industriales sinteticos, con criticidad y pertenencia a areas operacionales.

- Granularidad: Una fila por activo físico, equipo minero, equipo de planta o sistema OT.
- Relaciones: AreaID -> Dim_Area.AreaID; Fact_OrdenesTrabajo.EquipmentID -> EquipmentID; Fact_Costos.EquipmentID -> EquipmentID; Fact_Mantenimiento.EquipmentID -> EquipmentID; Fact_Incidentes.EquipmentID -> EquipmentID; Fact_Energia.EquipmentID -> EquipmentID

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| EquipmentID | PK | Clave del equipo o activo. En hechos permite conectar costos, mantenimiento, energía e incidentes con Dim_Equipo. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| EquipmentName | Atributo | Nombre sintético del equipo, activo o sistema OT. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| EquipmentType | Atributo | Tipo de equipo minero o industrial: Camión CAEX, Pala, Correa transportadora, Molino SAG, PLC, SCADA, etc. | Camión CAEX; Correa transportadora; Molino SAG; Servidor SCADA | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| Criticality | Atributo | Criticidad operacional del equipo. Debe leerse como impacto potencial en producción, seguridad, costo o continuidad. | Crítica; Alta; Media; Baja | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| AreaID | FK | Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| Manufacturer | Atributo | Fabricante ficticio del equipo. Sirve para segmentar sin usar marcas reales. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| Model | Atributo | Modelo ficticio del equipo. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| CommissioningDate | Atributo | Fecha de puesta en servicio del equipo. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| ActiveFlag | Indicador | Indica si el equipo está activo en el periodo del dataset. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |

## Dim_Cliente
Clientes internos o contratos sinteticos relacionados con mineria, servicios mineros y mantenimiento industrial.

- Granularidad: Una fila por cliente interno, gerencia, superintendencia o contrato sintético.
- Relaciones: Dim_Proyecto.ClientID -> ClientID; Fact_SLA.ClientID -> ClientID

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| ClientID | PK | Clave del cliente interno, gerencia o contrato sintético. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| ClientName | Atributo | Cliente interno o contrato ficticio relacionado con minería. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| Segment | Atributo | Segmento del cliente: Minería, Servicios Mineros, Operaciones Industriales, Energía Industrial o Mantenimiento Industrial. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| Region | Atributo | Región ficticia de gestión. No corresponde a una localización real exacta. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| ContractType | Atributo | Tipo de relación: SLA operacional, proyecto mina, contrato marco o servicio especializado. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |

## Dim_Proyecto
Proyectos mineros sinteticos de confiabilidad, produccion, energia, seguridad, automatizacion e infraestructura.

- Granularidad: Una fila por proyecto minero o iniciativa Tech&Eng.
- Relaciones: ClientID -> Dim_Cliente.ClientID; AreaID -> Dim_Area.AreaID; ResponsibleID -> Dim_Responsable.ResponsibleID; PriorityID -> Dim_Prioridad.PriorityID; Fact_Proyectos.ProjectID -> ProjectID; Fact_Costos.ProjectID -> ProjectID

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| ProjectID | PK | Clave del proyecto minero sintético. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| ProjectName | Atributo | Nombre de iniciativa minera, por ejemplo reemplazo de correa, upgrade SCADA o reducción de consumo energético. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| ProjectType | Atributo | Tipo de proyecto: confiabilidad, energía, seguridad, producción, mantenimiento, automatización, infraestructura, planta, mina o transformación digital. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| ClientID | FK | Clave del cliente interno, gerencia o contrato sintético. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| AreaID | FK | Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| ResponsibleID | FK | Clave del responsable o rol asignado. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| PriorityID | FK | Clave de prioridad operacional. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| PlannedStartDate | Atributo | Campo PlannedStartDate de Dim_Proyecto. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| PlannedEndDate | Atributo | Campo PlannedEndDate de Dim_Proyecto. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |

## Dim_Responsable
Roles sinteticos de operacion minera, mantenimiento, confiabilidad, energia, HSE, costos y OT.

- Granularidad: Una fila por responsable o rol sintético.
- Relaciones: Dim_Proyecto.ResponsibleID -> ResponsibleID; Fact_OrdenesTrabajo.ResponsibleID -> ResponsibleID; Fact_Productividad.ResponsibleID -> ResponsibleID

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| ResponsibleID | PK | Clave del responsable o rol asignado. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| ResponsibleName | Atributo | Nombre sintético del responsable. No representa personas reales. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| Role | Atributo | Rol operacional o analítico del responsable. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| Team | Atributo | Equipo, turno o grupo de trabajo sintético. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| AreaID | FK | Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |

## Dim_TipoTrabajo
Tipos de trabajo usados en mantenimiento y operacion minera: correctivo, preventivo, predictivo, inspeccion, paradas y emergencias.

- Granularidad: Una fila por tipo de trabajo operacional o de mantenimiento.
- Relaciones: Fact_OrdenesTrabajo.WorkTypeID -> WorkTypeID; Fact_Mantenimiento.WorkTypeID -> WorkTypeID

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| WorkTypeID | PK | Clave del tipo de trabajo. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| WorkTypeName | Atributo | Tipo de trabajo operacional o de mantenimiento. | Correctivo no planificado; Predictivo; Parada planta; Soporte OT | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| WorkCategory | Atributo | Categoría analítica del trabajo: Correctivo, Preventivo, Predictivo, Inspección, Proyecto, Emergencia o Mejora. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| PlannedFlag | Indicador | Indica si el registro corresponde a trabajo planificado. En mantenimiento ayuda a separar preventivo/planificado de correctivo no planificado. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |

## Dim_Prioridad
Prioridades operacionales y objetivos de respuesta/resolucion para servicios mineros.

- Granularidad: Una fila por nivel de prioridad operacional.
- Relaciones: Dim_Proyecto.PriorityID -> PriorityID; Fact_OrdenesTrabajo.PriorityID -> PriorityID; Fact_SLA.PriorityID -> PriorityID; Fact_Mantenimiento.PriorityID -> PriorityID

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| PriorityID | PK | Clave de prioridad operacional. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| PriorityName | Atributo | Nivel de prioridad estandarizado: Crítica, Alta, Media o Baja. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| PriorityRank | Atributo | Orden numérico de prioridad. Menor valor significa mayor prioridad. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| TargetResponseHours | Métrica | Horas objetivo para responder a una solicitud según prioridad. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| TargetResolutionHours | Métrica | Horas objetivo para resolver una solicitud según prioridad. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |

## Dim_Estado
Estados estandarizados para ordenes, proyectos y acciones operacionales.

- Granularidad: Una fila por estado estandarizado.
- Relaciones: Fact_OrdenesTrabajo.StatusID -> StatusID

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| StatusID | PK | Clave de estado estandarizado. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| StatusName | Atributo | Estado operacional estandarizado: Abierta, En Proceso, Vencida, Cerrada o Cancelada. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| StatusGroup | Atributo | Grupo de análisis del estado: abierto, cerrado, vencido u otro. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| SortOrder | Atributo | Orden recomendado para mostrar estados en reportes. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| IsClosed | Atributo | Indica si el estado se considera cerrado para KPIs de backlog o cumplimiento. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |

## Dim_Servicio
Servicios mineros gestionados con SLA: mantenimiento mina/planta, dispatch, correas, SCADA, energia, HSE y relaves.

- Granularidad: Una fila por servicio operacional sujeto a SLA.
- Relaciones: Fact_OrdenesTrabajo.ServiceID -> ServiceID; Fact_SLA.ServiceID -> ServiceID

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| ServiceID | PK | Clave del servicio operacional. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| ServiceName | Atributo | Servicio minero sujeto a gestión o SLA, por ejemplo Mantenimiento Planta, Soporte Dispatch o Gestión de Relaves. | Soporte Dispatch; Inspección de Correas; Gestión de Relaves | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| ServiceCategory | Atributo | Categoría del servicio: Mina, Planta, Mantenimiento, Energía, Seguridad, Automatización, Operaciones o Ingeniería. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| DefaultSLAHours | Métrica | Horas SLA por defecto del servicio antes de ajustar por prioridad o contexto. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |

## Dim_Ubicacion
Ubicaciones sinteticas de faena: pit, frentes, chancado, correas, molinos, relaves, salas electricas y talleres.

- Granularidad: Una fila por ubicación física sintética de faena.
- Relaciones: Dim_Area.LocationID -> LocationID; Fact_Incidentes.LocationID -> LocationID; Fact_Energia.LocationID -> LocationID; Fact_Productividad.LocationID -> LocationID

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| LocationID | PK | Clave de ubicación. En dimensiones es identificador; en hechos permite analizar por lugar físico de faena. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | Debe ser único si es PK y consistente si se usa como FK. |
| LocationName | Atributo | Nombre de ubicación física sintética: Pit Norte, Faja CV-101, Molino SAG, Relavera Principal, etc. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| Site | Atributo | Nombre ficticio del sitio minero. No corresponde a una faena real. | Sitio Andina Norte; Sitio Pampa Central; Sitio Sierra Azul | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| Zone | Atributo | Zona operacional de la ubicación: Mina, Planta, Relaves, Energía, Mantenimiento, Control u Operaciones. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |
| Country | Atributo | País ficticio/operacional usado para el caso. No implica uso de datos reales. | Depende del registro. | Segmentación, filtros, relaciones o validación del modelo. | En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query. |

## Fact_Proyectos
Avance, costo, riesgo y retraso de proyectos mineros sinteticos.

- Granularidad: Una fila por corte de seguimiento de proyecto.
- Relaciones: ProjectID -> Dim_Proyecto.ProjectID; DateKey -> Dim_Fecha.DateKey; AreaID -> Dim_Area.AreaID

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| ProjectFactID | PK | Clave del registro de seguimiento del proyecto. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ProjectID | FK | Clave del proyecto minero sintético. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| DateKey | FK | Clave de fecha en formato yyyymmdd. Permite relacionar hechos con Dim_Fecha sin depender de formatos regionales. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| AreaID | FK | Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ClientID | FK | Clave del cliente interno, gerencia o contrato sintético. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ResponsibleID | FK | Clave del responsable o rol asignado. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| StatusID | FK | Clave de estado estandarizado. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| PriorityID | FK | Clave de prioridad operacional. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| PlannedProgressPct | Métrica | Avance planificado del proyecto a la fecha del registro. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ActualProgressPct | Métrica | Avance real del proyecto a la fecha del registro. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| PlannedCost | Métrica | Costo planificado o presupuesto del proyecto. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ActualCost | Métrica | Costo real acumulado o registrado del proyecto. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| RiskScore | Métrica | Puntaje sintético de riesgo del proyecto. Valores más altos sugieren mayor probabilidad de atraso, sobrecosto o impacto operacional. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| DelayDays | Métrica | Días de retraso del proyecto frente al plan. Cero indica sin retraso registrado. | Depende del registro. | Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |

## Fact_OrdenesTrabajo
Ordenes de trabajo de mantenimiento, operaciones y soporte OT con backlog, criticidad y fuente de sistema.

- Granularidad: Una fila por orden de trabajo.
- Relaciones: EquipmentID -> Dim_Equipo.EquipmentID; CreatedDateKey -> Dim_Fecha.DateKey; AreaID -> Dim_Area.AreaID; ServiceID -> Dim_Servicio.ServiceID; ResponsibleID -> Dim_Responsable.ResponsibleID; WorkTypeID -> Dim_TipoTrabajo.WorkTypeID; PriorityID -> Dim_Prioridad.PriorityID; StatusID -> Dim_Estado.StatusID; Fact_SLA.WorkOrderID -> WorkOrderID

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| WorkOrderID | PK | Clave de la orden de trabajo. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| CreatedDateKey | FK | Fecha de creación de la orden o del compromiso SLA. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ClosedDateKey | FK | Fecha de cierre de la orden. En raw puede venir nula para prácticas de limpieza. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | En raw puede aparecer nulo o con formato inconsistente; en clean debe permitir análisis de cierre/resolución. |
| AreaID | FK | Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| EquipmentID | FK | Clave del equipo o activo. En hechos permite conectar costos, mantenimiento, energía e incidentes con Dim_Equipo. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ServiceID | FK | Clave del servicio operacional. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ResponsibleID | FK | Clave del responsable o rol asignado. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| WorkTypeID | FK | Clave del tipo de trabajo. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| PriorityID | FK | Clave de prioridad operacional. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| StatusID | FK | Clave de estado estandarizado. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| EstimatedHours | Métrica | Horas estimadas antes de ejecutar la orden. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ActualHours | Métrica | Horas reales consumidas por la orden o el SLA. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| IsCritical | Atributo | Marca órdenes críticas por impacto operacional, seguridad, continuidad o SLA. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ReworkFlag | Indicador | Indica retrabajo. Es útil para detectar problemas repetitivos de calidad, planificación o mantenimiento. | Depende del registro. | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| SourceSystem | Atributo | Sistema fuente sintético: SAP PM, Maximo, SCADA, Dispatch o Excel Manual. | SAP PM; Maximo; SCADA; Dispatch; Excel Manual | Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |

## Fact_Costos
Presupuesto, comprometido y costo real de operacion, mantenimiento, energia, repuestos, contratistas y proyectos mineros.

- Granularidad: Una fila por registro de costo presupuestado, comprometido y real.
- Relaciones: ProjectID -> Dim_Proyecto.ProjectID; EquipmentID -> Dim_Equipo.EquipmentID; DateKey -> Dim_Fecha.DateKey

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| CostID | PK | Clave del registro de costo. | Depende del registro. | Costo real vs presupuesto, variación de costo, costo por área/equipo/proyecto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| DateKey | FK | Clave de fecha en formato yyyymmdd. Permite relacionar hechos con Dim_Fecha sin depender de formatos regionales. | Depende del registro. | Costo real vs presupuesto, variación de costo, costo por área/equipo/proyecto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ProjectID | FK | Clave del proyecto minero sintético. | Depende del registro. | Costo real vs presupuesto, variación de costo, costo por área/equipo/proyecto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| AreaID | FK | Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area. | Depende del registro. | Costo real vs presupuesto, variación de costo, costo por área/equipo/proyecto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| EquipmentID | FK | Clave del equipo o activo. En hechos permite conectar costos, mantenimiento, energía e incidentes con Dim_Equipo. | Depende del registro. | Costo real vs presupuesto, variación de costo, costo por área/equipo/proyecto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| CostCategory | Atributo | Categoría de costo minero: repuestos, mano de obra, contratistas, energía, neumáticos, componentes mayores, instrumentación, seguridad, automatización, etc. | Neumáticos; Energía; Componentes mayores; Parada planta | Costo real vs presupuesto, variación de costo, costo por área/equipo/proyecto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| BudgetAmount | Métrica | Monto presupuestado. | Depende del registro. | Costo real vs presupuesto, variación de costo, costo por área/equipo/proyecto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ActualAmount | Métrica | Monto real registrado. | Depende del registro. | Costo real vs presupuesto, variación de costo, costo por área/equipo/proyecto. | Revisar outliers antes de concluir causas; algunos patrones son intencionales para el laboratorio. |
| CommittedAmount | Métrica | Monto comprometido, por ejemplo orden de compra o contrato aún no devengado. | Depende del registro. | Costo real vs presupuesto, variación de costo, costo por área/equipo/proyecto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| VendorType | Atributo | Tipo de proveedor o fuente de gasto: interno, contratista, OEM sintético o servicio especializado. | Depende del registro. | Costo real vs presupuesto, variación de costo, costo por área/equipo/proyecto. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |

## Fact_SLA
Cumplimiento de acuerdos de servicio para servicios operacionales mineros.

- Granularidad: Una fila por compromiso SLA asociado a una orden de trabajo.
- Relaciones: WorkOrderID -> Fact_OrdenesTrabajo.WorkOrderID; ClientID -> Dim_Cliente.ClientID; ServiceID -> Dim_Servicio.ServiceID; AreaID -> Dim_Area.AreaID; PriorityID -> Dim_Prioridad.PriorityID; CreatedDateKey -> Dim_Fecha.DateKey

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| SLAID | PK | Clave del compromiso SLA. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| WorkOrderID | FK | Clave de la orden de trabajo. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ClientID | FK | Clave del cliente interno, gerencia o contrato sintético. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ServiceID | FK | Clave del servicio operacional. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| AreaID | FK | Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| PriorityID | FK | Clave de prioridad operacional. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| CreatedDateKey | FK | Fecha de creación de la orden o del compromiso SLA. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| CommittedDateKey | FK | Fecha comprometida para resolver o cumplir el servicio. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ResolvedDateKey | FK | Fecha real de resolución del servicio. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | En raw puede aparecer nulo o con formato inconsistente; en clean debe permitir análisis de cierre/resolución. |
| TargetHours | Métrica | Horas objetivo del SLA. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ActualHours | Métrica | Horas reales consumidas por la orden o el SLA. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| SLAMetFlag | Indicador | Indica si el SLA fue cumplido. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| BreachHours | Métrica | Horas de incumplimiento. Cero significa SLA cumplido o sin brecha. | Depende del registro. | % cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |

## Fact_Mantenimiento
Eventos de mantenimiento y confiabilidad minera con downtime, repair hours, modos de falla y costos.

- Granularidad: Una fila por evento de mantenimiento o falla.
- Relaciones: EquipmentID -> Dim_Equipo.EquipmentID; AreaID -> Dim_Area.AreaID; WorkTypeID -> Dim_TipoTrabajo.WorkTypeID; PriorityID -> Dim_Prioridad.PriorityID; DateKey -> Dim_Fecha.DateKey

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| MaintenanceID | PK | Clave del evento de mantenimiento. | Depende del registro. | Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| DateKey | FK | Clave de fecha en formato yyyymmdd. Permite relacionar hechos con Dim_Fecha sin depender de formatos regionales. | Depende del registro. | Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| EquipmentID | FK | Clave del equipo o activo. En hechos permite conectar costos, mantenimiento, energía e incidentes con Dim_Equipo. | Depende del registro. | Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| AreaID | FK | Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area. | Depende del registro. | Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| WorkTypeID | FK | Clave del tipo de trabajo. | Depende del registro. | Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| PriorityID | FK | Clave de prioridad operacional. | Depende del registro. | Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| FailureMode | Atributo | Modo de falla minero, por ejemplo bloqueo de chancador, corte de correa, fuga hidráulica, falla de bomba o pérdida de comunicación PLC. | Bloqueo de chancador; Corte de correa; Falla de bomba de pulpa | Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| SystemCategory | Atributo | Sistema afectado: Hidráulico, Eléctrico, Mecánico, Neumáticos, Correas, Chancado, Molienda, Bombas, Instrumentación, Control, Energía o Seguridad. | Chancado; Correas; Molienda; Control | Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| DowntimeHours | Métrica | Horas de indisponibilidad operacional atribuidas al evento. | Depende del registro. | Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas. | Revisar outliers antes de concluir causas; algunos patrones son intencionales para el laboratorio. |
| RepairHours | Métrica | Horas invertidas en reparación. No siempre equivalen al downtime porque puede haber espera, permisos o pruebas. | Depende del registro. | Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| MaintenanceCost | Métrica | Costo del evento de mantenimiento. | Depende del registro. | Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas. | Revisar outliers antes de concluir causas; algunos patrones son intencionales para el laboratorio. |
| PlannedFlag | Indicador | Indica si el registro corresponde a trabajo planificado. En mantenimiento ayuda a separar preventivo/planificado de correctivo no planificado. | Depende del registro. | Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |

## Fact_Incidentes
Incidentes HSE y acciones correctivas en contexto minero sintetico.

- Granularidad: Una fila por incidente HSE o acción correctiva.
- Relaciones: AreaID -> Dim_Area.AreaID; EquipmentID -> Dim_Equipo.EquipmentID; LocationID -> Dim_Ubicacion.LocationID; DateKey -> Dim_Fecha.DateKey

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| IncidentID | PK | Clave del incidente o acción HSE. | Depende del registro. | Incidentes por severidad, acciones abiertas/vencidas, días abiertos y foco HSE por área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| DateKey | FK | Clave de fecha en formato yyyymmdd. Permite relacionar hechos con Dim_Fecha sin depender de formatos regionales. | Depende del registro. | Incidentes por severidad, acciones abiertas/vencidas, días abiertos y foco HSE por área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| AreaID | FK | Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area. | Depende del registro. | Incidentes por severidad, acciones abiertas/vencidas, días abiertos y foco HSE por área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| EquipmentID | FK | Clave del equipo o activo. En hechos permite conectar costos, mantenimiento, energía e incidentes con Dim_Equipo. | Depende del registro. | Incidentes por severidad, acciones abiertas/vencidas, días abiertos y foco HSE por área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| LocationID | FK | Clave de ubicación. En dimensiones es identificador; en hechos permite analizar por lugar físico de faena. | Depende del registro. | Incidentes por severidad, acciones abiertas/vencidas, días abiertos y foco HSE por área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| Severity | Atributo | Severidad del incidente: Baja, Media, Alta o Crítica. | Depende del registro. | Incidentes por severidad, acciones abiertas/vencidas, días abiertos y foco HSE por área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| IncidentType | Atributo | Tipo de incidente HSE u operacional. | Casi accidente; Evento HSE; Riesgo geotécnico; Falla de control crítico | Incidentes por severidad, acciones abiertas/vencidas, días abiertos y foco HSE por área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| CorrectiveActionStatus | Atributo | Estado de la acción correctiva asociada al incidente. | Depende del registro. | Incidentes por severidad, acciones abiertas/vencidas, días abiertos y foco HSE por área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| DaysOpen | Atributo | Días que la acción correctiva lleva abierta. Cero cuando ya está cerrada. | Depende del registro. | Incidentes por severidad, acciones abiertas/vencidas, días abiertos y foco HSE por área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| LostTimeFlag | Indicador | Indica si el incidente generó tiempo perdido. | Depende del registro. | Incidentes por severidad, acciones abiertas/vencidas, días abiertos y foco HSE por área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| RiskCategory | Atributo | Categoría de riesgo: Seguridad, Operación, Ambiente, Calidad o Geotecnia. | Depende del registro. | Incidentes por severidad, acciones abiertas/vencidas, días abiertos y foco HSE por área. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |

## Fact_Energia
Consumo energetico, costo y output operacional asociado a equipos y areas mineras.

- Granularidad: Una fila por medición de consumo energético por equipo, área, ubicación y turno.
- Relaciones: AreaID -> Dim_Area.AreaID; EquipmentID -> Dim_Equipo.EquipmentID; LocationID -> Dim_Ubicacion.LocationID; DateKey -> Dim_Fecha.DateKey

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| EnergyID | PK | Clave del registro energético. | Depende del registro. | kWh total, costo energía, kWh por tonelada, consumo anormal por área/equipo/turno. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| DateKey | FK | Clave de fecha en formato yyyymmdd. Permite relacionar hechos con Dim_Fecha sin depender de formatos regionales. | Depende del registro. | kWh total, costo energía, kWh por tonelada, consumo anormal por área/equipo/turno. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| AreaID | FK | Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area. | Depende del registro. | kWh total, costo energía, kWh por tonelada, consumo anormal por área/equipo/turno. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| EquipmentID | FK | Clave del equipo o activo. En hechos permite conectar costos, mantenimiento, energía e incidentes con Dim_Equipo. | Depende del registro. | kWh total, costo energía, kWh por tonelada, consumo anormal por área/equipo/turno. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| LocationID | FK | Clave de ubicación. En dimensiones es identificador; en hechos permite analizar por lugar físico de faena. | Depende del registro. | kWh total, costo energía, kWh por tonelada, consumo anormal por área/equipo/turno. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| kWh | Atributo | Consumo energético registrado en kilowatt-hora. | Depende del registro. | kWh total, costo energía, kWh por tonelada, consumo anormal por área/equipo/turno. | Revisar outliers antes de concluir causas; algunos patrones son intencionales para el laboratorio. |
| EnergyCost | Métrica | Costo energético asociado al consumo. | Depende del registro. | kWh total, costo energía, kWh por tonelada, consumo anormal por área/equipo/turno. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| OperatingHours | Métrica | Horas de operación del equipo o sistema en el registro. | Depende del registro. | kWh total, costo energía, kWh por tonelada, consumo anormal por área/equipo/turno. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| OutputUnits | Atributo | Output operacional asociado al consumo. En mina/planta se interpreta como toneladas aproximadas u otra unidad operativa sintética. | Depende del registro. | kWh total, costo energía, kWh por tonelada, consumo anormal por área/equipo/turno. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| Shift | Atributo | Turno operacional: Día, Tarde o Noche. | Día; Tarde; Noche | kWh total, costo energía, kWh por tonelada, consumo anormal por área/equipo/turno. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |

## Fact_Productividad
Produccion u output operacional por turno, area, responsable y ubicacion.

- Granularidad: Una fila por medición de output operacional por turno.
- Relaciones: AreaID -> Dim_Area.AreaID; ResponsibleID -> Dim_Responsable.ResponsibleID; LocationID -> Dim_Ubicacion.LocationID; DateKey -> Dim_Fecha.DateKey

| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |
|---|---|---|---|---|---|
| ProductivityID | PK | Clave del registro de productividad. | Depende del registro. | Cumplimiento de producción, productividad por turno, toneladas por hora productiva y brecha plan vs real. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| DateKey | FK | Clave de fecha en formato yyyymmdd. Permite relacionar hechos con Dim_Fecha sin depender de formatos regionales. | Depende del registro. | Cumplimiento de producción, productividad por turno, toneladas por hora productiva y brecha plan vs real. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| AreaID | FK | Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area. | Depende del registro. | Cumplimiento de producción, productividad por turno, toneladas por hora productiva y brecha plan vs real. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ResponsibleID | FK | Clave del responsable o rol asignado. | Depende del registro. | Cumplimiento de producción, productividad por turno, toneladas por hora productiva y brecha plan vs real. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| LocationID | FK | Clave de ubicación. En dimensiones es identificador; en hechos permite analizar por lugar físico de faena. | Depende del registro. | Cumplimiento de producción, productividad por turno, toneladas por hora productiva y brecha plan vs real. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| Shift | Atributo | Turno operacional: Día, Tarde o Noche. | Día; Tarde; Noche | Cumplimiento de producción, productividad por turno, toneladas por hora productiva y brecha plan vs real. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| PlannedOutput | Atributo | Output planificado por turno o área. En mina puede representar toneladas movidas; en planta, toneladas chancadas o procesadas. | Depende del registro. | Cumplimiento de producción, productividad por turno, toneladas por hora productiva y brecha plan vs real. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ActualOutput | Atributo | Output real observado. Se compara con PlannedOutput para medir cumplimiento operacional. | Depende del registro. | Cumplimiento de producción, productividad por turno, toneladas por hora productiva y brecha plan vs real. | Revisar outliers antes de concluir causas; algunos patrones son intencionales para el laboratorio. |
| LaborHours | Métrica | Horas laborales disponibles. | Depende del registro. | Cumplimiento de producción, productividad por turno, toneladas por hora productiva y brecha plan vs real. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| ProductiveHours | Métrica | Horas efectivamente productivas. | Depende del registro. | Cumplimiento de producción, productividad por turno, toneladas por hora productiva y brecha plan vs real. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
| NonProductiveHours | Métrica | Horas no productivas por espera, fallas, coordinación, permisos, detenciones u otras causas sintéticas. | Depende del registro. | Cumplimiento de producción, productividad por turno, toneladas por hora productiva y brecha plan vs real. | Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones. |
