from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.config.settings import load_settings
from src.data.schema import DIMENSION_TABLES, FACT_TABLES, PRIMARY_KEYS, RELATIONSHIPS, TABLE_COLUMNS, TABLE_DESCRIPTIONS
from src.utils.io import write_text


TABLE_GRAIN = {
    "Dim_Fecha": "Una fila por día calendario.",
    "Dim_Area": "Una fila por área o proceso minero sintético.",
    "Dim_Equipo": "Una fila por activo físico, equipo minero, equipo de planta o sistema OT.",
    "Dim_Cliente": "Una fila por cliente interno, gerencia, superintendencia o contrato sintético.",
    "Dim_Proyecto": "Una fila por proyecto minero o iniciativa Tech&Eng.",
    "Dim_Responsable": "Una fila por responsable o rol sintético.",
    "Dim_TipoTrabajo": "Una fila por tipo de trabajo operacional o de mantenimiento.",
    "Dim_Prioridad": "Una fila por nivel de prioridad operacional.",
    "Dim_Estado": "Una fila por estado estandarizado.",
    "Dim_Servicio": "Una fila por servicio operacional sujeto a SLA.",
    "Dim_Ubicacion": "Una fila por ubicación física sintética de faena.",
    "Fact_Proyectos": "Una fila por corte de seguimiento de proyecto.",
    "Fact_OrdenesTrabajo": "Una fila por orden de trabajo.",
    "Fact_Costos": "Una fila por registro de costo presupuestado, comprometido y real.",
    "Fact_SLA": "Una fila por compromiso SLA asociado a una orden de trabajo.",
    "Fact_Mantenimiento": "Una fila por evento de mantenimiento o falla.",
    "Fact_Incidentes": "Una fila por incidente HSE o acción correctiva.",
    "Fact_Energia": "Una fila por medición de consumo energético por equipo, área, ubicación y turno.",
    "Fact_Productividad": "Una fila por medición de output operacional por turno.",
}


COLUMN_DESCRIPTIONS = {
    "DateKey": "Clave de fecha en formato yyyymmdd. Permite relacionar hechos con Dim_Fecha sin depender de formatos regionales.",
    "Date": "Fecha calendario legible. Se usa para filtros, ejes temporales y validación de rangos.",
    "Year": "Año calendario.",
    "Quarter": "Trimestre calendario.",
    "MonthNumber": "Número de mes entre 1 y 12.",
    "MonthName": "Nombre del mes en español.",
    "WeekNumber": "Número de semana ISO aproximado para análisis semanal.",
    "DayOfWeek": "Día de la semana en español.",
    "IsWeekend": "Indica si la fecha cae en fin de semana.",
    "AreaID": "Clave del área minera. En dimensiones es identificador; en hechos es llave foránea hacia Dim_Area.",
    "AreaName": "Nombre del proceso o área minera sintética, por ejemplo Chancado Primario, Molienda o Taller Mina.",
    "BusinessUnit": "Unidad de negocio o superintendencia sintética a la que pertenece el área.",
    "AreaType": "Tipo analítico del área: Mina, Planta, Mantenimiento, Servicios, Seguridad, Ingeniería o Soporte Operacional.",
    "ManagerName": "Nombre sintético del responsable de gestión del área. No representa personas reales.",
    "LocationID": "Clave de ubicación. En dimensiones es identificador; en hechos permite analizar por lugar físico de faena.",
    "EquipmentID": "Clave del equipo o activo. En hechos permite conectar costos, mantenimiento, energía e incidentes con Dim_Equipo.",
    "EquipmentName": "Nombre sintético del equipo, activo o sistema OT.",
    "EquipmentType": "Tipo de equipo minero o industrial: Camión CAEX, Pala, Correa transportadora, Molino SAG, PLC, SCADA, etc.",
    "Criticality": "Criticidad operacional del equipo. Debe leerse como impacto potencial en producción, seguridad, costo o continuidad.",
    "Manufacturer": "Fabricante ficticio del equipo. Sirve para segmentar sin usar marcas reales.",
    "Model": "Modelo ficticio del equipo.",
    "CommissioningDate": "Fecha de puesta en servicio del equipo.",
    "ActiveFlag": "Indica si el equipo está activo en el periodo del dataset.",
    "ClientID": "Clave del cliente interno, gerencia o contrato sintético.",
    "ClientName": "Cliente interno o contrato ficticio relacionado con minería.",
    "Segment": "Segmento del cliente: Minería, Servicios Mineros, Operaciones Industriales, Energía Industrial o Mantenimiento Industrial.",
    "Region": "Región ficticia de gestión. No corresponde a una localización real exacta.",
    "ContractType": "Tipo de relación: SLA operacional, proyecto mina, contrato marco o servicio especializado.",
    "ProjectID": "Clave del proyecto minero sintético.",
    "ProjectName": "Nombre de iniciativa minera, por ejemplo reemplazo de correa, upgrade SCADA o reducción de consumo energético.",
    "ProjectType": "Tipo de proyecto: confiabilidad, energía, seguridad, producción, mantenimiento, automatización, infraestructura, planta, mina o transformación digital.",
    "ResponsibleID": "Clave del responsable o rol asignado.",
    "ResponsibleName": "Nombre sintético del responsable. No representa personas reales.",
    "Role": "Rol operacional o analítico del responsable.",
    "Team": "Equipo, turno o grupo de trabajo sintético.",
    "WorkTypeID": "Clave del tipo de trabajo.",
    "WorkTypeName": "Tipo de trabajo operacional o de mantenimiento.",
    "WorkCategory": "Categoría analítica del trabajo: Correctivo, Preventivo, Predictivo, Inspección, Proyecto, Emergencia o Mejora.",
    "PlannedFlag": "Indica si el registro corresponde a trabajo planificado. En mantenimiento ayuda a separar preventivo/planificado de correctivo no planificado.",
    "PriorityID": "Clave de prioridad operacional.",
    "PriorityName": "Nivel de prioridad estandarizado: Crítica, Alta, Media o Baja.",
    "PriorityRank": "Orden numérico de prioridad. Menor valor significa mayor prioridad.",
    "TargetResponseHours": "Horas objetivo para responder a una solicitud según prioridad.",
    "TargetResolutionHours": "Horas objetivo para resolver una solicitud según prioridad.",
    "StatusID": "Clave de estado estandarizado.",
    "StatusName": "Estado operacional estandarizado: Abierta, En Proceso, Vencida, Cerrada o Cancelada.",
    "StatusGroup": "Grupo de análisis del estado: abierto, cerrado, vencido u otro.",
    "SortOrder": "Orden recomendado para mostrar estados en reportes.",
    "IsClosed": "Indica si el estado se considera cerrado para KPIs de backlog o cumplimiento.",
    "ServiceID": "Clave del servicio operacional.",
    "ServiceName": "Servicio minero sujeto a gestión o SLA, por ejemplo Mantenimiento Planta, Soporte Dispatch o Gestión de Relaves.",
    "ServiceCategory": "Categoría del servicio: Mina, Planta, Mantenimiento, Energía, Seguridad, Automatización, Operaciones o Ingeniería.",
    "DefaultSLAHours": "Horas SLA por defecto del servicio antes de ajustar por prioridad o contexto.",
    "LocationName": "Nombre de ubicación física sintética: Pit Norte, Faja CV-101, Molino SAG, Relavera Principal, etc.",
    "Site": "Nombre ficticio del sitio minero. No corresponde a una faena real.",
    "Zone": "Zona operacional de la ubicación: Mina, Planta, Relaves, Energía, Mantenimiento, Control u Operaciones.",
    "Country": "País ficticio/operacional usado para el caso. No implica uso de datos reales.",
    "ProjectFactID": "Clave del registro de seguimiento del proyecto.",
    "PlannedProgressPct": "Avance planificado del proyecto a la fecha del registro.",
    "ActualProgressPct": "Avance real del proyecto a la fecha del registro.",
    "PlannedCost": "Costo planificado o presupuesto del proyecto.",
    "ActualCost": "Costo real acumulado o registrado del proyecto.",
    "RiskScore": "Puntaje sintético de riesgo del proyecto. Valores más altos sugieren mayor probabilidad de atraso, sobrecosto o impacto operacional.",
    "DelayDays": "Días de retraso del proyecto frente al plan. Cero indica sin retraso registrado.",
    "WorkOrderID": "Clave de la orden de trabajo.",
    "CreatedDateKey": "Fecha de creación de la orden o del compromiso SLA.",
    "ClosedDateKey": "Fecha de cierre de la orden. En raw puede venir nula para prácticas de limpieza.",
    "EstimatedHours": "Horas estimadas antes de ejecutar la orden.",
    "ActualHours": "Horas reales consumidas por la orden o el SLA.",
    "IsCritical": "Marca órdenes críticas por impacto operacional, seguridad, continuidad o SLA.",
    "ReworkFlag": "Indica retrabajo. Es útil para detectar problemas repetitivos de calidad, planificación o mantenimiento.",
    "SourceSystem": "Sistema fuente sintético: SAP PM, Maximo, SCADA, Dispatch o Excel Manual.",
    "CostID": "Clave del registro de costo.",
    "CostCategory": "Categoría de costo minero: repuestos, mano de obra, contratistas, energía, neumáticos, componentes mayores, instrumentación, seguridad, automatización, etc.",
    "BudgetAmount": "Monto presupuestado.",
    "ActualAmount": "Monto real registrado.",
    "CommittedAmount": "Monto comprometido, por ejemplo orden de compra o contrato aún no devengado.",
    "VendorType": "Tipo de proveedor o fuente de gasto: interno, contratista, OEM sintético o servicio especializado.",
    "SLAID": "Clave del compromiso SLA.",
    "CommittedDateKey": "Fecha comprometida para resolver o cumplir el servicio.",
    "ResolvedDateKey": "Fecha real de resolución del servicio.",
    "TargetHours": "Horas objetivo del SLA.",
    "SLAMetFlag": "Indica si el SLA fue cumplido.",
    "BreachHours": "Horas de incumplimiento. Cero significa SLA cumplido o sin brecha.",
    "MaintenanceID": "Clave del evento de mantenimiento.",
    "FailureMode": "Modo de falla minero, por ejemplo bloqueo de chancador, corte de correa, fuga hidráulica, falla de bomba o pérdida de comunicación PLC.",
    "SystemCategory": "Sistema afectado: Hidráulico, Eléctrico, Mecánico, Neumáticos, Correas, Chancado, Molienda, Bombas, Instrumentación, Control, Energía o Seguridad.",
    "DowntimeHours": "Horas de indisponibilidad operacional atribuidas al evento.",
    "RepairHours": "Horas invertidas en reparación. No siempre equivalen al downtime porque puede haber espera, permisos o pruebas.",
    "MaintenanceCost": "Costo del evento de mantenimiento.",
    "IncidentID": "Clave del incidente o acción HSE.",
    "Severity": "Severidad del incidente: Baja, Media, Alta o Crítica.",
    "IncidentType": "Tipo de incidente HSE u operacional.",
    "CorrectiveActionStatus": "Estado de la acción correctiva asociada al incidente.",
    "DaysOpen": "Días que la acción correctiva lleva abierta. Cero cuando ya está cerrada.",
    "LostTimeFlag": "Indica si el incidente generó tiempo perdido.",
    "RiskCategory": "Categoría de riesgo: Seguridad, Operación, Ambiente, Calidad o Geotecnia.",
    "EnergyID": "Clave del registro energético.",
    "kWh": "Consumo energético registrado en kilowatt-hora.",
    "EnergyCost": "Costo energético asociado al consumo.",
    "OperatingHours": "Horas de operación del equipo o sistema en el registro.",
    "OutputUnits": "Output operacional asociado al consumo. En mina/planta se interpreta como toneladas aproximadas u otra unidad operativa sintética.",
    "Shift": "Turno operacional: Día, Tarde o Noche.",
    "ProductivityID": "Clave del registro de productividad.",
    "PlannedOutput": "Output planificado por turno o área. En mina puede representar toneladas movidas; en planta, toneladas chancadas o procesadas.",
    "ActualOutput": "Output real observado. Se compara con PlannedOutput para medir cumplimiento operacional.",
    "LaborHours": "Horas laborales disponibles.",
    "ProductiveHours": "Horas efectivamente productivas.",
    "NonProductiveHours": "Horas no productivas por espera, fallas, coordinación, permisos, detenciones u otras causas sintéticas.",
}


COLUMN_EXAMPLES = {
    "AreaName": "Chancado Primario; Molienda; Espesamiento y Relaves",
    "EquipmentType": "Camión CAEX; Correa transportadora; Molino SAG; Servidor SCADA",
    "Criticality": "Crítica; Alta; Media; Baja",
    "ServiceName": "Soporte Dispatch; Inspección de Correas; Gestión de Relaves",
    "WorkTypeName": "Correctivo no planificado; Predictivo; Parada planta; Soporte OT",
    "FailureMode": "Bloqueo de chancador; Corte de correa; Falla de bomba de pulpa",
    "SystemCategory": "Chancado; Correas; Molienda; Control",
    "CostCategory": "Neumáticos; Energía; Componentes mayores; Parada planta",
    "SourceSystem": "SAP PM; Maximo; SCADA; Dispatch; Excel Manual",
    "IncidentType": "Casi accidente; Evento HSE; Riesgo geotécnico; Falla de control crítico",
    "Shift": "Día; Tarde; Noche",
    "Site": "Sitio Andina Norte; Sitio Pampa Central; Sitio Sierra Azul",
}


KPI_USAGE = {
    "Fact_Productividad": "Cumplimiento de producción, productividad por turno, toneladas por hora productiva y brecha plan vs real.",
    "Fact_Energia": "kWh total, costo energía, kWh por tonelada, consumo anormal por área/equipo/turno.",
    "Fact_Mantenimiento": "Downtime, MTTR aproximado, costo de mantenimiento, correctivo vs preventivo y fallas repetitivas.",
    "Fact_OrdenesTrabajo": "Backlog, órdenes críticas abiertas, retrabajo, horas reales vs estimadas y carga por sistema fuente.",
    "Fact_SLA": "% cumplimiento SLA, breach hours, resolución promedio, SLA por prioridad, servicio y área.",
    "Fact_Costos": "Costo real vs presupuesto, variación de costo, costo por área/equipo/proyecto.",
    "Fact_Incidentes": "Incidentes por severidad, acciones abiertas/vencidas, días abiertos y foco HSE por área.",
    "Fact_Proyectos": "Avance real vs plan, delay days, cost variance, risk score y cumplimiento de presupuesto.",
}


def _role(table: str, column: str) -> str:
    if PRIMARY_KEYS.get(table) == column:
        return "PK"
    if column.endswith("ID") or column.endswith("Key"):
        return "FK" if table in FACT_TABLES or table != column.replace("ID", "") else "Clave"
    if column.endswith("Flag"):
        return "Indicador"
    if column.endswith("Hours") or column.endswith("Cost") or column.endswith("Amount") or column.endswith("Pct") or column.endswith("Score") or column.endswith("Days"):
        return "Métrica"
    return "Atributo"


def _relationships_for_table(table: str) -> str:
    items: list[str] = []
    for parent_table, parent_col, child_table, child_col in RELATIONSHIPS:
        if child_table == table:
            items.append(f"{child_col} -> {parent_table}.{parent_col}")
        elif parent_table == table:
            items.append(f"{child_table}.{child_col} -> {parent_col}")
    return "; ".join(items) if items else "Sin relaciones directas declaradas."


def _quality_note(table: str, column: str) -> str:
    if table.startswith("Dim_"):
        if column.endswith("ID") or column.endswith("Key"):
            return "Debe ser único si es PK y consistente si se usa como FK."
        return "En clean está estandarizado; en raw puede tener variaciones controladas para práctica de Power Query."
    if column in {"ClosedDateKey", "ResolvedDateKey"}:
        return "En raw puede aparecer nulo o con formato inconsistente; en clean debe permitir análisis de cierre/resolución."
    if column in {"ActualAmount", "MaintenanceCost", "kWh", "DowntimeHours", "ActualOutput"}:
        return "Revisar outliers antes de concluir causas; algunos patrones son intencionales para el laboratorio."
    return "Validar contra dimensiones, fechas y reglas de negocio antes de usar en decisiones."


def build_dictionary_frame() -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    for table, columns in TABLE_COLUMNS.items():
        for column in columns:
            rows.append(
                {
                    "TableName": table,
                    "TableType": "Dimensión" if table in DIMENSION_TABLES else "Hecho",
                    "TableDescription": TABLE_DESCRIPTIONS.get(table, ""),
                    "Grain": TABLE_GRAIN.get(table, ""),
                    "ColumnName": column,
                    "Role": _role(table, column),
                    "Description": COLUMN_DESCRIPTIONS.get(column, f"Campo {column} de {table}."),
                    "ExampleValues": COLUMN_EXAMPLES.get(column, "Depende del registro."),
                    "KPIUsage": KPI_USAGE.get(table, "Segmentación, filtros, relaciones o validación del modelo."),
                    "DataQualityNotes": _quality_note(table, column),
                    "Relationships": _relationships_for_table(table),
                }
            )
    return pd.DataFrame(rows)


def generate_data_dictionary(dataset_kind: str, root: Path | None = None) -> tuple[Path, Path | None]:
    settings = load_settings(root)
    root = (root or settings.repo_root).resolve()
    out_dir = root / "data" / dataset_kind / "dictionary"
    out_dir.mkdir(parents=True, exist_ok=True)
    df = build_dictionary_frame()

    dataset_label = "Dataset A - entrenamiento" if dataset_kind == "training" else "Dataset B - proyecto final"
    lines = [
        f"# Diccionario de datos - {dataset_label}",
        "",
        "Datos 100% sintéticos para un caso Tech&Eng minero. El esquema es común para Dataset A y Dataset B.",
        "",
        "## Cómo leer este diccionario",
        "- **PK** identifica una fila única dentro de una tabla.",
        "- **FK** conecta una tabla de hechos con una dimensión o con otra tabla transaccional.",
        "- **Granularidad** indica qué representa una fila.",
        "- **Clean** está listo para modelo estrella; **raw** conserva errores controlados para prácticas de Power Query.",
        "- Dataset A y Dataset B comparten columnas, pero no comparten exactamente los mismos patrones operacionales.",
        "",
        "## Diferencia Dataset A vs Dataset B",
        "- Dataset A concentra patrones de entrenamiento en chancado, correas, taller mina, molienda y energía.",
        "- Dataset B usa el mismo esquema, pero concentra problemas distintos en dispatch, relaves, molienda, flota mina y OT.",
        "- Las causas raíz del Dataset B no deben entregarse al estudiante; sirven para evaluar transferencia.",
        "",
    ]

    for table in DIMENSION_TABLES + FACT_TABLES:
        subset = df[df["TableName"] == table]
        lines.append(f"## {table}")
        lines.append(TABLE_DESCRIPTIONS.get(table, ""))
        lines.append("")
        lines.append(f"- Granularidad: {TABLE_GRAIN.get(table, '')}")
        lines.append(f"- Relaciones: {_relationships_for_table(table)}")
        lines.append("")
        lines.append("| Columna | Rol | Definición | Ejemplos | Uso analítico/KPI | Calidad de datos |")
        lines.append("|---|---|---|---|---|---|")
        for _, row in subset.iterrows():
            lines.append(
                f"| {row['ColumnName']} | {row['Role']} | {row['Description']} | {row['ExampleValues']} | {row['KPIUsage']} | {row['DataQualityNotes']} |"
            )
        lines.append("")

    md_path = out_dir / "data_dictionary.md"
    write_text("\n".join(lines), md_path, root)

    xlsx_path: Path | None = None
    if settings.export_excel_dictionary:
        xlsx_path = out_dir / "data_dictionary.xlsx"
        with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Dictionary")
            pd.DataFrame({"DimensionTables": DIMENSION_TABLES}).to_excel(writer, index=False, sheet_name="Dimensions")
            pd.DataFrame({"FactTables": FACT_TABLES}).to_excel(writer, index=False, sheet_name="Facts")
            pd.DataFrame({"TableName": list(TABLE_GRAIN), "Grain": list(TABLE_GRAIN.values())}).to_excel(writer, index=False, sheet_name="Grain")
    return md_path, xlsx_path


def generate_all_dictionaries(root: Path | None = None) -> dict[str, tuple[Path, Path | None]]:
    return {kind: generate_data_dictionary(kind, root) for kind in ["training", "project"]}
