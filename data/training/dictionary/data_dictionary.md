# Diccionario de datos - entrenamiento

Datos 100% sintéticos. Schema común para Dataset A y Dataset B.

## Dim_Fecha
Calendario para inteligencia de tiempo.

| Columna | Rol | Descripción |
|---|---|---|
| DateKey | PK | DateKey de Dim_Fecha. Calendario para inteligencia de tiempo. |
| Date | Métrica/atributo | Date de Dim_Fecha. Calendario para inteligencia de tiempo. |
| Year | Métrica/atributo | Year de Dim_Fecha. Calendario para inteligencia de tiempo. |
| Quarter | Métrica/atributo | Quarter de Dim_Fecha. Calendario para inteligencia de tiempo. |
| MonthNumber | Métrica/atributo | MonthNumber de Dim_Fecha. Calendario para inteligencia de tiempo. |
| MonthName | Métrica/atributo | MonthName de Dim_Fecha. Calendario para inteligencia de tiempo. |
| WeekNumber | Métrica/atributo | WeekNumber de Dim_Fecha. Calendario para inteligencia de tiempo. |
| DayOfWeek | Métrica/atributo | DayOfWeek de Dim_Fecha. Calendario para inteligencia de tiempo. |
| IsWeekend | Métrica/atributo | IsWeekend de Dim_Fecha. Calendario para inteligencia de tiempo. |

## Dim_Area
Áreas operativas y unidades de negocio.

| Columna | Rol | Descripción |
|---|---|---|
| AreaID | PK | AreaID de Dim_Area. Áreas operativas y unidades de negocio. |
| AreaName | Métrica/atributo | AreaName de Dim_Area. Áreas operativas y unidades de negocio. |
| BusinessUnit | Métrica/atributo | BusinessUnit de Dim_Area. Áreas operativas y unidades de negocio. |
| AreaType | Métrica/atributo | AreaType de Dim_Area. Áreas operativas y unidades de negocio. |
| ManagerName | Métrica/atributo | ManagerName de Dim_Area. Áreas operativas y unidades de negocio. |
| LocationID | FK/atributo | LocationID de Dim_Area. Áreas operativas y unidades de negocio. |

## Dim_Equipo
Activos técnicos y criticidad.

| Columna | Rol | Descripción |
|---|---|---|
| EquipmentID | PK | EquipmentID de Dim_Equipo. Activos técnicos y criticidad. |
| EquipmentName | Métrica/atributo | EquipmentName de Dim_Equipo. Activos técnicos y criticidad. |
| EquipmentType | Métrica/atributo | EquipmentType de Dim_Equipo. Activos técnicos y criticidad. |
| Criticality | Métrica/atributo | Criticality de Dim_Equipo. Activos técnicos y criticidad. |
| AreaID | FK/atributo | AreaID de Dim_Equipo. Activos técnicos y criticidad. |
| Manufacturer | Métrica/atributo | Manufacturer de Dim_Equipo. Activos técnicos y criticidad. |
| Model | Métrica/atributo | Model de Dim_Equipo. Activos técnicos y criticidad. |
| CommissioningDate | Métrica/atributo | CommissioningDate de Dim_Equipo. Activos técnicos y criticidad. |
| ActiveFlag | Métrica/atributo | ActiveFlag de Dim_Equipo. Activos técnicos y criticidad. |

## Dim_Cliente
Clientes sintéticos y segmentos.

| Columna | Rol | Descripción |
|---|---|---|
| ClientID | PK | ClientID de Dim_Cliente. Clientes sintéticos y segmentos. |
| ClientName | Métrica/atributo | ClientName de Dim_Cliente. Clientes sintéticos y segmentos. |
| Segment | Métrica/atributo | Segment de Dim_Cliente. Clientes sintéticos y segmentos. |
| Region | Métrica/atributo | Region de Dim_Cliente. Clientes sintéticos y segmentos. |
| ContractType | Métrica/atributo | ContractType de Dim_Cliente. Clientes sintéticos y segmentos. |

## Dim_Proyecto
Proyectos técnicos planificados.

| Columna | Rol | Descripción |
|---|---|---|
| ProjectID | PK | ProjectID de Dim_Proyecto. Proyectos técnicos planificados. |
| ProjectName | Métrica/atributo | ProjectName de Dim_Proyecto. Proyectos técnicos planificados. |
| ProjectType | Métrica/atributo | ProjectType de Dim_Proyecto. Proyectos técnicos planificados. |
| ClientID | FK/atributo | ClientID de Dim_Proyecto. Proyectos técnicos planificados. |
| AreaID | FK/atributo | AreaID de Dim_Proyecto. Proyectos técnicos planificados. |
| ResponsibleID | FK/atributo | ResponsibleID de Dim_Proyecto. Proyectos técnicos planificados. |
| PriorityID | FK/atributo | PriorityID de Dim_Proyecto. Proyectos técnicos planificados. |
| PlannedStartDate | Métrica/atributo | PlannedStartDate de Dim_Proyecto. Proyectos técnicos planificados. |
| PlannedEndDate | Métrica/atributo | PlannedEndDate de Dim_Proyecto. Proyectos técnicos planificados. |

## Dim_Responsable
Responsables sintéticos de operación y proyectos.

| Columna | Rol | Descripción |
|---|---|---|
| ResponsibleID | PK | ResponsibleID de Dim_Responsable. Responsables sintéticos de operación y proyectos. |
| ResponsibleName | Métrica/atributo | ResponsibleName de Dim_Responsable. Responsables sintéticos de operación y proyectos. |
| Role | Métrica/atributo | Role de Dim_Responsable. Responsables sintéticos de operación y proyectos. |
| Team | Métrica/atributo | Team de Dim_Responsable. Responsables sintéticos de operación y proyectos. |
| AreaID | FK/atributo | AreaID de Dim_Responsable. Responsables sintéticos de operación y proyectos. |

## Dim_TipoTrabajo
Tipos de trabajo planificado y correctivo.

| Columna | Rol | Descripción |
|---|---|---|
| WorkTypeID | PK | WorkTypeID de Dim_TipoTrabajo. Tipos de trabajo planificado y correctivo. |
| WorkTypeName | Métrica/atributo | WorkTypeName de Dim_TipoTrabajo. Tipos de trabajo planificado y correctivo. |
| WorkCategory | Métrica/atributo | WorkCategory de Dim_TipoTrabajo. Tipos de trabajo planificado y correctivo. |
| PlannedFlag | Métrica/atributo | PlannedFlag de Dim_TipoTrabajo. Tipos de trabajo planificado y correctivo. |

## Dim_Prioridad
Prioridades y objetivos de respuesta/resolución.

| Columna | Rol | Descripción |
|---|---|---|
| PriorityID | PK | PriorityID de Dim_Prioridad. Prioridades y objetivos de respuesta/resolución. |
| PriorityName | Métrica/atributo | PriorityName de Dim_Prioridad. Prioridades y objetivos de respuesta/resolución. |
| PriorityRank | Métrica/atributo | PriorityRank de Dim_Prioridad. Prioridades y objetivos de respuesta/resolución. |
| TargetResponseHours | Métrica/atributo | TargetResponseHours de Dim_Prioridad. Prioridades y objetivos de respuesta/resolución. |
| TargetResolutionHours | Métrica/atributo | TargetResolutionHours de Dim_Prioridad. Prioridades y objetivos de respuesta/resolución. |

## Dim_Estado
Estados operativos y grupos de cierre.

| Columna | Rol | Descripción |
|---|---|---|
| StatusID | PK | StatusID de Dim_Estado. Estados operativos y grupos de cierre. |
| StatusName | Métrica/atributo | StatusName de Dim_Estado. Estados operativos y grupos de cierre. |
| StatusGroup | Métrica/atributo | StatusGroup de Dim_Estado. Estados operativos y grupos de cierre. |
| SortOrder | Métrica/atributo | SortOrder de Dim_Estado. Estados operativos y grupos de cierre. |
| IsClosed | Métrica/atributo | IsClosed de Dim_Estado. Estados operativos y grupos de cierre. |

## Dim_Servicio
Servicios gestionados y SLA por defecto.

| Columna | Rol | Descripción |
|---|---|---|
| ServiceID | PK | ServiceID de Dim_Servicio. Servicios gestionados y SLA por defecto. |
| ServiceName | Métrica/atributo | ServiceName de Dim_Servicio. Servicios gestionados y SLA por defecto. |
| ServiceCategory | Métrica/atributo | ServiceCategory de Dim_Servicio. Servicios gestionados y SLA por defecto. |
| DefaultSLAHours | Métrica/atributo | DefaultSLAHours de Dim_Servicio. Servicios gestionados y SLA por defecto. |

## Dim_Ubicacion
Ubicaciones sintéticas.

| Columna | Rol | Descripción |
|---|---|---|
| LocationID | PK | LocationID de Dim_Ubicacion. Ubicaciones sintéticas. |
| LocationName | Métrica/atributo | LocationName de Dim_Ubicacion. Ubicaciones sintéticas. |
| Site | Métrica/atributo | Site de Dim_Ubicacion. Ubicaciones sintéticas. |
| Zone | Métrica/atributo | Zone de Dim_Ubicacion. Ubicaciones sintéticas. |
| Country | Métrica/atributo | Country de Dim_Ubicacion. Ubicaciones sintéticas. |

## Fact_Proyectos
Avance, costo y riesgo de proyectos.

| Columna | Rol | Descripción |
|---|---|---|
| ProjectFactID | PK | ProjectFactID de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| ProjectID | FK/atributo | ProjectID de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| DateKey | FK/atributo | DateKey de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| AreaID | FK/atributo | AreaID de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| ClientID | FK/atributo | ClientID de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| ResponsibleID | FK/atributo | ResponsibleID de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| StatusID | FK/atributo | StatusID de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| PriorityID | FK/atributo | PriorityID de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| PlannedProgressPct | Métrica/atributo | PlannedProgressPct de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| ActualProgressPct | Métrica/atributo | ActualProgressPct de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| PlannedCost | Métrica/atributo | PlannedCost de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| ActualCost | Métrica/atributo | ActualCost de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| RiskScore | Métrica/atributo | RiskScore de Fact_Proyectos. Avance, costo y riesgo de proyectos. |
| DelayDays | Métrica/atributo | DelayDays de Fact_Proyectos. Avance, costo y riesgo de proyectos. |

## Fact_OrdenesTrabajo
Órdenes de trabajo técnicas.

| Columna | Rol | Descripción |
|---|---|---|
| WorkOrderID | PK | WorkOrderID de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| CreatedDateKey | FK/atributo | CreatedDateKey de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| ClosedDateKey | FK/atributo | ClosedDateKey de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| AreaID | FK/atributo | AreaID de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| EquipmentID | FK/atributo | EquipmentID de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| ServiceID | FK/atributo | ServiceID de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| ResponsibleID | FK/atributo | ResponsibleID de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| WorkTypeID | FK/atributo | WorkTypeID de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| PriorityID | FK/atributo | PriorityID de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| StatusID | FK/atributo | StatusID de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| EstimatedHours | Métrica/atributo | EstimatedHours de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| ActualHours | Métrica/atributo | ActualHours de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| IsCritical | Métrica/atributo | IsCritical de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| ReworkFlag | Métrica/atributo | ReworkFlag de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |
| SourceSystem | Métrica/atributo | SourceSystem de Fact_OrdenesTrabajo. Órdenes de trabajo técnicas. |

## Fact_Costos
Presupuesto, comprometido y costo real.

| Columna | Rol | Descripción |
|---|---|---|
| CostID | PK | CostID de Fact_Costos. Presupuesto, comprometido y costo real. |
| DateKey | FK/atributo | DateKey de Fact_Costos. Presupuesto, comprometido y costo real. |
| ProjectID | FK/atributo | ProjectID de Fact_Costos. Presupuesto, comprometido y costo real. |
| AreaID | FK/atributo | AreaID de Fact_Costos. Presupuesto, comprometido y costo real. |
| EquipmentID | FK/atributo | EquipmentID de Fact_Costos. Presupuesto, comprometido y costo real. |
| CostCategory | Métrica/atributo | CostCategory de Fact_Costos. Presupuesto, comprometido y costo real. |
| BudgetAmount | Métrica/atributo | BudgetAmount de Fact_Costos. Presupuesto, comprometido y costo real. |
| ActualAmount | Métrica/atributo | ActualAmount de Fact_Costos. Presupuesto, comprometido y costo real. |
| CommittedAmount | Métrica/atributo | CommittedAmount de Fact_Costos. Presupuesto, comprometido y costo real. |
| VendorType | Métrica/atributo | VendorType de Fact_Costos. Presupuesto, comprometido y costo real. |

## Fact_SLA
Cumplimiento de acuerdos de servicio.

| Columna | Rol | Descripción |
|---|---|---|
| SLAID | PK | SLAID de Fact_SLA. Cumplimiento de acuerdos de servicio. |
| WorkOrderID | FK/atributo | WorkOrderID de Fact_SLA. Cumplimiento de acuerdos de servicio. |
| ClientID | FK/atributo | ClientID de Fact_SLA. Cumplimiento de acuerdos de servicio. |
| ServiceID | FK/atributo | ServiceID de Fact_SLA. Cumplimiento de acuerdos de servicio. |
| AreaID | FK/atributo | AreaID de Fact_SLA. Cumplimiento de acuerdos de servicio. |
| PriorityID | FK/atributo | PriorityID de Fact_SLA. Cumplimiento de acuerdos de servicio. |
| CreatedDateKey | FK/atributo | CreatedDateKey de Fact_SLA. Cumplimiento de acuerdos de servicio. |
| CommittedDateKey | FK/atributo | CommittedDateKey de Fact_SLA. Cumplimiento de acuerdos de servicio. |
| ResolvedDateKey | FK/atributo | ResolvedDateKey de Fact_SLA. Cumplimiento de acuerdos de servicio. |
| TargetHours | Métrica/atributo | TargetHours de Fact_SLA. Cumplimiento de acuerdos de servicio. |
| ActualHours | Métrica/atributo | ActualHours de Fact_SLA. Cumplimiento de acuerdos de servicio. |
| SLAMetFlag | Métrica/atributo | SLAMetFlag de Fact_SLA. Cumplimiento de acuerdos de servicio. |
| BreachHours | Métrica/atributo | BreachHours de Fact_SLA. Cumplimiento de acuerdos de servicio. |

## Fact_Mantenimiento
Eventos de mantenimiento y downtime.

| Columna | Rol | Descripción |
|---|---|---|
| MaintenanceID | PK | MaintenanceID de Fact_Mantenimiento. Eventos de mantenimiento y downtime. |
| DateKey | FK/atributo | DateKey de Fact_Mantenimiento. Eventos de mantenimiento y downtime. |
| EquipmentID | FK/atributo | EquipmentID de Fact_Mantenimiento. Eventos de mantenimiento y downtime. |
| AreaID | FK/atributo | AreaID de Fact_Mantenimiento. Eventos de mantenimiento y downtime. |
| WorkTypeID | FK/atributo | WorkTypeID de Fact_Mantenimiento. Eventos de mantenimiento y downtime. |
| PriorityID | FK/atributo | PriorityID de Fact_Mantenimiento. Eventos de mantenimiento y downtime. |
| FailureMode | Métrica/atributo | FailureMode de Fact_Mantenimiento. Eventos de mantenimiento y downtime. |
| SystemCategory | Métrica/atributo | SystemCategory de Fact_Mantenimiento. Eventos de mantenimiento y downtime. |
| DowntimeHours | Métrica/atributo | DowntimeHours de Fact_Mantenimiento. Eventos de mantenimiento y downtime. |
| RepairHours | Métrica/atributo | RepairHours de Fact_Mantenimiento. Eventos de mantenimiento y downtime. |
| MaintenanceCost | Métrica/atributo | MaintenanceCost de Fact_Mantenimiento. Eventos de mantenimiento y downtime. |
| PlannedFlag | Métrica/atributo | PlannedFlag de Fact_Mantenimiento. Eventos de mantenimiento y downtime. |

## Fact_Incidentes
Incidentes de seguridad y acciones correctivas.

| Columna | Rol | Descripción |
|---|---|---|
| IncidentID | PK | IncidentID de Fact_Incidentes. Incidentes de seguridad y acciones correctivas. |
| DateKey | FK/atributo | DateKey de Fact_Incidentes. Incidentes de seguridad y acciones correctivas. |
| AreaID | FK/atributo | AreaID de Fact_Incidentes. Incidentes de seguridad y acciones correctivas. |
| EquipmentID | FK/atributo | EquipmentID de Fact_Incidentes. Incidentes de seguridad y acciones correctivas. |
| LocationID | FK/atributo | LocationID de Fact_Incidentes. Incidentes de seguridad y acciones correctivas. |
| Severity | Métrica/atributo | Severity de Fact_Incidentes. Incidentes de seguridad y acciones correctivas. |
| IncidentType | Métrica/atributo | IncidentType de Fact_Incidentes. Incidentes de seguridad y acciones correctivas. |
| CorrectiveActionStatus | Métrica/atributo | CorrectiveActionStatus de Fact_Incidentes. Incidentes de seguridad y acciones correctivas. |
| DaysOpen | Métrica/atributo | DaysOpen de Fact_Incidentes. Incidentes de seguridad y acciones correctivas. |
| LostTimeFlag | Métrica/atributo | LostTimeFlag de Fact_Incidentes. Incidentes de seguridad y acciones correctivas. |
| RiskCategory | Métrica/atributo | RiskCategory de Fact_Incidentes. Incidentes de seguridad y acciones correctivas. |

## Fact_Energia
Consumo energético, costo y producción asociada.

| Columna | Rol | Descripción |
|---|---|---|
| EnergyID | PK | EnergyID de Fact_Energia. Consumo energético, costo y producción asociada. |
| DateKey | FK/atributo | DateKey de Fact_Energia. Consumo energético, costo y producción asociada. |
| AreaID | FK/atributo | AreaID de Fact_Energia. Consumo energético, costo y producción asociada. |
| EquipmentID | FK/atributo | EquipmentID de Fact_Energia. Consumo energético, costo y producción asociada. |
| LocationID | FK/atributo | LocationID de Fact_Energia. Consumo energético, costo y producción asociada. |
| kWh | Métrica/atributo | kWh de Fact_Energia. Consumo energético, costo y producción asociada. |
| EnergyCost | Métrica/atributo | EnergyCost de Fact_Energia. Consumo energético, costo y producción asociada. |
| OperatingHours | Métrica/atributo | OperatingHours de Fact_Energia. Consumo energético, costo y producción asociada. |
| OutputUnits | Métrica/atributo | OutputUnits de Fact_Energia. Consumo energético, costo y producción asociada. |
| Shift | Métrica/atributo | Shift de Fact_Energia. Consumo energético, costo y producción asociada. |

## Fact_Productividad
Producción, horas laborales y productividad.

| Columna | Rol | Descripción |
|---|---|---|
| ProductivityID | PK | ProductivityID de Fact_Productividad. Producción, horas laborales y productividad. |
| DateKey | FK/atributo | DateKey de Fact_Productividad. Producción, horas laborales y productividad. |
| AreaID | FK/atributo | AreaID de Fact_Productividad. Producción, horas laborales y productividad. |
| ResponsibleID | FK/atributo | ResponsibleID de Fact_Productividad. Producción, horas laborales y productividad. |
| LocationID | FK/atributo | LocationID de Fact_Productividad. Producción, horas laborales y productividad. |
| Shift | Métrica/atributo | Shift de Fact_Productividad. Producción, horas laborales y productividad. |
| PlannedOutput | Métrica/atributo | PlannedOutput de Fact_Productividad. Producción, horas laborales y productividad. |
| ActualOutput | Métrica/atributo | ActualOutput de Fact_Productividad. Producción, horas laborales y productividad. |
| LaborHours | Métrica/atributo | LaborHours de Fact_Productividad. Producción, horas laborales y productividad. |
| ProductiveHours | Métrica/atributo | ProductiveHours de Fact_Productividad. Producción, horas laborales y productividad. |
| NonProductiveHours | Métrica/atributo | NonProductiveHours de Fact_Productividad. Producción, horas laborales y productividad. |
