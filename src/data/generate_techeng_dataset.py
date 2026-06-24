from __future__ import annotations

from dataclasses import replace
from pathlib import Path
import pandas as pd
import numpy as np

from src.config.settings import Settings, load_settings
from src.data.schema import TABLE_COLUMNS
from src.data.data_quality_injector import inject_raw_issues
from src.utils.io import write_csv, write_json, write_text
from src.utils.logging import get_logger

logger = get_logger(__name__)


MONTHS_ES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
    7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre",
}
DAYS_ES = {0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves", 4: "Viernes", 5: "Sábado", 6: "Domingo"}


def _ids(prefix: str, n: int, width: int = 3) -> list[str]:
    return [f"{prefix}{i:0{width}d}" for i in range(1, n + 1)]


def _date_key(value: pd.Timestamp | str) -> int:
    return int(pd.Timestamp(value).strftime("%Y%m%d"))


def _random_dates(rng: np.random.Generator, start: str, end: str, n: int) -> pd.Series:
    dates = pd.date_range(start, end, freq="D")
    selected = rng.choice(dates.to_numpy(), size=n, replace=True)
    return pd.Series(pd.to_datetime(selected))


def _choice(rng: np.random.Generator, values: list[str] | pd.Series, n: int, p: list[float] | None = None) -> np.ndarray:
    return rng.choice(list(values), size=n, replace=True, p=p)


def build_dimensions(settings: Settings, dataset_kind: str, rng: np.random.Generator) -> dict[str, pd.DataFrame]:
    start = settings.training_start_date if dataset_kind == "training" else settings.project_start_date
    end = settings.training_end_date if dataset_kind == "training" else settings.project_end_date
    dates = pd.date_range(start, end, freq="D")
    dim_fecha = pd.DataFrame({
        "DateKey": [int(d.strftime("%Y%m%d")) for d in dates],
        "Date": [d.strftime("%Y-%m-%d") for d in dates],
        "Year": [d.year for d in dates],
        "Quarter": [f"Q{d.quarter}" for d in dates],
        "MonthNumber": [d.month for d in dates],
        "MonthName": [MONTHS_ES[d.month] for d in dates],
        "WeekNumber": dates.isocalendar().week.astype(int).to_list(),
        "DayOfWeek": [DAYS_ES[d.dayofweek] for d in dates],
        "IsWeekend": [d.dayofweek >= 5 for d in dates],
    })

    n_locations = max(5, min(8, settings.n_areas + 1))
    location_names = ["Planta Norte", "Planta Sur", "Campus Técnico", "Centro de Servicios", "Subestación Este", "Patio Logístico", "Nodo Remoto", "Centro de Control"]
    dim_ubicacion = pd.DataFrame({
        "LocationID": _ids("L", n_locations),
        "LocationName": location_names[:n_locations],
        "Site": ["Industrial", "Industrial", "Corporativo", "Servicios", "Energía", "Logística", "Remoto", "Control"][:n_locations],
        "Zone": ["Norte", "Sur", "Centro", "Centro", "Este", "Oeste", "Norte", "Centro"][:n_locations],
        "Country": ["Perú"] * n_locations,
    })

    base_areas = ["Operaciones Mina", "Mantenimiento Planta", "Ingeniería de Proyectos", "Servicios TI/OT", "Seguridad HSE", "Energía y Utilities", "Calidad Técnica", "Logística Técnica"]
    area_names = (base_areas * ((settings.n_areas // len(base_areas)) + 1))[: settings.n_areas]
    dim_area = pd.DataFrame({
        "AreaID": _ids("A", settings.n_areas),
        "AreaName": area_names,
        "BusinessUnit": _choice(rng, ["Operaciones", "Ingeniería", "Servicios", "Soporte"], settings.n_areas),
        "AreaType": _choice(rng, ["Operativa", "Soporte", "Proyecto"], settings.n_areas),
        "ManagerName": [f"Manager Sintético {i:02d}" for i in range(1, settings.n_areas + 1)],
        "LocationID": _choice(rng, dim_ubicacion["LocationID"], settings.n_areas),
    })

    equipment_types = ["Bomba", "Compresor", "PLC", "Servidor OT", "Transformador", "Sensor", "Transportador", "Tablero"]
    manufacturers = ["AndesTech", "NovaControls", "InnovaPower", "Aster Systems", "Kuntur Labs"]
    area_for_equipment = _choice(rng, dim_area["AreaID"], settings.n_equipment)
    dim_equipo = pd.DataFrame({
        "EquipmentID": _ids("EQ", settings.n_equipment, 4),
        "EquipmentName": [f"Equipo Sintético {i:04d}" for i in range(1, settings.n_equipment + 1)],
        "EquipmentType": _choice(rng, equipment_types, settings.n_equipment),
        "Criticality": _choice(rng, ["Alta", "Media", "Baja"], settings.n_equipment, p=[0.28, 0.48, 0.24]),
        "AreaID": area_for_equipment,
        "Manufacturer": _choice(rng, manufacturers, settings.n_equipment),
        "Model": [f"M-{rng.integers(100,999)}" for _ in range(settings.n_equipment)],
        "CommissioningDate": _random_dates(rng, "2017-01-01", start, settings.n_equipment).dt.strftime("%Y-%m-%d"),
        "ActiveFlag": rng.choice([True, False], size=settings.n_equipment, p=[0.94, 0.06]),
    })

    dim_cliente = pd.DataFrame({
        "ClientID": _ids("C", settings.n_clients),
        "ClientName": [f"Cliente Sintético {i:02d}" for i in range(1, settings.n_clients + 1)],
        "Segment": _choice(rng, ["Minería", "Energía", "Manufactura", "Infraestructura", "Servicios"], settings.n_clients),
        "Region": _choice(rng, ["Lima", "Norte", "Sur", "Centro", "Oriente"], settings.n_clients),
        "ContractType": _choice(rng, ["SLA", "Proyecto", "Retainer", "Spot"], settings.n_clients),
    })

    dim_prioridad = pd.DataFrame({
        "PriorityID": ["P1", "P2", "P3", "P4"],
        "PriorityName": ["Crítica", "Alta", "Media", "Baja"],
        "PriorityRank": [1, 2, 3, 4],
        "TargetResponseHours": [2, 4, 12, 24],
        "TargetResolutionHours": [8, 24, 72, 120],
    })
    dim_estado = pd.DataFrame({
        "StatusID": ["S1", "S2", "S3", "S4", "S5"],
        "StatusName": ["Nuevo", "En Proceso", "En Espera", "Cerrado", "Cancelado"],
        "StatusGroup": ["Abierto", "Abierto", "Abierto", "Cerrado", "Cerrado"],
        "SortOrder": [1, 2, 3, 4, 5],
        "IsClosed": [False, False, False, True, True],
    })
    dim_tipo = pd.DataFrame({
        "WorkTypeID": ["WT1", "WT2", "WT3", "WT4", "WT5", "WT6"],
        "WorkTypeName": ["Preventivo", "Correctivo", "Inspección", "Mejora", "Instalación", "Soporte"],
        "WorkCategory": ["Mantenimiento", "Mantenimiento", "Control", "Proyecto", "Proyecto", "Servicio"],
        "PlannedFlag": [True, False, True, True, True, False],
    })
    dim_servicio = pd.DataFrame({
        "ServiceID": ["SV1", "SV2", "SV3", "SV4", "SV5", "SV6", "SV7", "SV8"],
        "ServiceName": ["Soporte OT", "Mantenimiento eléctrico", "Mantenimiento mecánico", "Gestión de proyectos", "Seguridad HSE", "Energía", "Automatización", "Mesa técnica"],
        "ServiceCategory": ["TI/OT", "Mantenimiento", "Mantenimiento", "Proyecto", "Seguridad", "Energía", "Automatización", "Servicio"],
        "DefaultSLAHours": [24, 48, 48, 120, 24, 72, 36, 24],
    })

    responsible_area = _choice(rng, dim_area["AreaID"], settings.n_responsibles)
    dim_responsable = pd.DataFrame({
        "ResponsibleID": _ids("R", settings.n_responsibles),
        "ResponsibleName": [f"Responsable Sintético {i:02d}" for i in range(1, settings.n_responsibles + 1)],
        "Role": _choice(rng, ["Supervisor", "Planner", "Ingeniero", "Técnico Líder", "Analista"], settings.n_responsibles),
        "Team": _choice(rng, ["Turno A", "Turno B", "Turno C", "Backoffice"], settings.n_responsibles),
        "AreaID": responsible_area,
    })

    project_area = _choice(rng, dim_area["AreaID"], settings.n_projects)
    project_dates = _random_dates(rng, start, end, settings.n_projects)
    durations = rng.integers(30, 180, size=settings.n_projects)
    dim_proyecto = pd.DataFrame({
        "ProjectID": _ids("PR", settings.n_projects, 4),
        "ProjectName": [f"Proyecto TechEng {i:04d}" for i in range(1, settings.n_projects + 1)],
        "ProjectType": _choice(rng, ["Implementación", "Optimización", "Mantenimiento mayor", "Digitalización", "Expansión"], settings.n_projects),
        "ClientID": _choice(rng, dim_cliente["ClientID"], settings.n_projects),
        "AreaID": project_area,
        "ResponsibleID": _choice(rng, dim_responsable["ResponsibleID"], settings.n_projects),
        "PriorityID": _choice(rng, dim_prioridad["PriorityID"], settings.n_projects, p=[0.14, 0.34, 0.34, 0.18]),
        "PlannedStartDate": project_dates.dt.strftime("%Y-%m-%d"),
        "PlannedEndDate": (project_dates + pd.to_timedelta(durations, unit="D")).dt.strftime("%Y-%m-%d"),
    })

    return {
        "Dim_Fecha": dim_fecha,
        "Dim_Area": dim_area,
        "Dim_Equipo": dim_equipo,
        "Dim_Cliente": dim_cliente,
        "Dim_Proyecto": dim_proyecto,
        "Dim_Responsable": dim_responsable,
        "Dim_TipoTrabajo": dim_tipo,
        "Dim_Prioridad": dim_prioridad,
        "Dim_Estado": dim_estado,
        "Dim_Servicio": dim_servicio,
        "Dim_Ubicacion": dim_ubicacion,
    }


def build_facts(settings: Settings, dataset_kind: str, dims: dict[str, pd.DataFrame], rng: np.random.Generator) -> dict[str, pd.DataFrame]:
    start = settings.training_start_date if dataset_kind == "training" else settings.project_start_date
    end = settings.training_end_date if dataset_kind == "training" else settings.project_end_date
    dim_fecha = dims["Dim_Fecha"]
    dim_area = dims["Dim_Area"]
    dim_equipo = dims["Dim_Equipo"]
    dim_proyecto = dims["Dim_Proyecto"]
    dim_responsable = dims["Dim_Responsable"]
    dim_prioridad = dims["Dim_Prioridad"]
    area_lookup = dim_area.set_index("AreaID")["AreaName"].to_dict()
    equipment_area = dim_equipo.set_index("EquipmentID")["AreaID"].to_dict()
    equipment_location = dim_equipo[["EquipmentID", "AreaID"]].merge(dim_area[["AreaID", "LocationID"]], on="AreaID").set_index("EquipmentID")["LocationID"].to_dict()
    priority_target = dim_prioridad.set_index("PriorityID")["TargetResolutionHours"].to_dict()

    projects = dim_proyecto.copy()
    n_projects = len(projects)
    project_dates = _random_dates(rng, start, end, n_projects)
    planned_progress = rng.uniform(35, 100, n_projects).round(1)
    delay_area = "A003" if dataset_kind == "training" else "A002"
    is_delay_area = projects["AreaID"].eq(delay_area).to_numpy()
    delay_days = rng.poisson(5, n_projects) + (is_delay_area * rng.integers(8, 35, n_projects))
    actual_progress = np.maximum(0, planned_progress - rng.uniform(0, 18, n_projects) - (is_delay_area * rng.uniform(5, 20, n_projects))).round(1)
    planned_cost = rng.uniform(25_000, 350_000, n_projects).round(2)
    cost_pressure_area = "A003" if dataset_kind == "training" else "A005"
    actual_cost = (planned_cost * rng.normal(1.02, 0.12, n_projects) * np.where(projects["AreaID"].eq(cost_pressure_area), rng.uniform(1.12, 1.45, n_projects), 1)).round(2)
    fact_proyectos = pd.DataFrame({
        "ProjectFactID": _ids("PF", n_projects, 5),
        "ProjectID": projects["ProjectID"],
        "DateKey": project_dates.map(_date_key),
        "AreaID": projects["AreaID"],
        "ClientID": projects["ClientID"],
        "ResponsibleID": projects["ResponsibleID"],
        "StatusID": _choice(rng, ["S1", "S2", "S3", "S4"], n_projects, p=[0.08, 0.42, 0.15, 0.35]),
        "PriorityID": projects["PriorityID"],
        "PlannedProgressPct": planned_progress,
        "ActualProgressPct": actual_progress,
        "PlannedCost": planned_cost,
        "ActualCost": actual_cost,
        "RiskScore": np.clip(rng.normal(45, 18, n_projects) + is_delay_area * rng.uniform(15, 30, n_projects), 1, 100).round(1),
        "DelayDays": delay_days.astype(int),
    })

    wo_equipment = _choice(rng, dim_equipo["EquipmentID"], settings.n_work_orders)
    wo_area = [equipment_area[eid] for eid in wo_equipment]
    created_dates = _random_dates(rng, start, end, settings.n_work_orders)
    priority = _choice(rng, ["P1", "P2", "P3", "P4"], settings.n_work_orders, p=[0.12, 0.30, 0.40, 0.18])
    status = _choice(rng, ["S1", "S2", "S3", "S4", "S5"], settings.n_work_orders, p=[0.08, 0.18, 0.08, 0.62, 0.04])
    estimated = np.array([priority_target[p] for p in priority]) * rng.uniform(0.35, 0.9, settings.n_work_orders)
    sla_pressure_area = "A004" if dataset_kind == "training" else "A001"
    actual = estimated * rng.lognormal(mean=0.10, sigma=0.42, size=settings.n_work_orders) * np.where(np.array(wo_area) == sla_pressure_area, 1.35, 1.0)
    closed_dates = []
    for created, status_id, hours in zip(created_dates, status, actual):
        if status_id in {"S4", "S5"}:
            closed = min(pd.Timestamp(end), created + pd.to_timedelta(max(1, int(hours // 8) + 1), unit="D"))
            closed_dates.append(_date_key(closed))
        else:
            closed_dates.append(pd.NA)
    fact_ordenes = pd.DataFrame({
        "WorkOrderID": _ids("WO", settings.n_work_orders, 6),
        "CreatedDateKey": created_dates.map(_date_key),
        "ClosedDateKey": pd.array(closed_dates, dtype="Int64"),
        "AreaID": wo_area,
        "EquipmentID": wo_equipment,
        "ServiceID": _choice(rng, dims["Dim_Servicio"]["ServiceID"], settings.n_work_orders),
        "ResponsibleID": _choice(rng, dim_responsable["ResponsibleID"], settings.n_work_orders),
        "WorkTypeID": _choice(rng, dims["Dim_TipoTrabajo"]["WorkTypeID"], settings.n_work_orders, p=[0.25, 0.32, 0.16, 0.08, 0.07, 0.12]),
        "PriorityID": priority,
        "StatusID": status,
        "EstimatedHours": estimated.round(2),
        "ActualHours": actual.round(2),
        "IsCritical": np.isin(priority, ["P1", "P2"]),
        "ReworkFlag": rng.choice([True, False], settings.n_work_orders, p=[0.11 if dataset_kind == "training" else 0.15, 0.89 if dataset_kind == "training" else 0.85]),
        "SourceSystem": _choice(rng, ["CMMS", "ServiceDesk", "ERP"], settings.n_work_orders),
    })

    cost_projects = dim_proyecto.sample(settings.n_cost_records, replace=True, random_state=int(rng.integers(1, 999_999))).reset_index(drop=True)
    cost_dates = _random_dates(rng, start, end, settings.n_cost_records)
    cost_equipment = _choice(rng, dim_equipo["EquipmentID"], settings.n_cost_records)
    budget = rng.uniform(1_000, 70_000, settings.n_cost_records)
    cost_factor = np.where(cost_projects["AreaID"].eq(cost_pressure_area), rng.uniform(1.10, 1.55, settings.n_cost_records), rng.normal(1.0, 0.16, settings.n_cost_records))
    fact_costos = pd.DataFrame({
        "CostID": _ids("CO", settings.n_cost_records, 6),
        "DateKey": cost_dates.map(_date_key),
        "ProjectID": cost_projects["ProjectID"],
        "AreaID": cost_projects["AreaID"],
        "EquipmentID": cost_equipment,
        "CostCategory": _choice(rng, ["Materiales", "Mano de obra", "Servicios", "Energía", "Repuestos", "Contratista"], settings.n_cost_records),
        "BudgetAmount": budget.round(2),
        "ActualAmount": (budget * cost_factor).round(2),
        "CommittedAmount": (budget * rng.uniform(0.2, 1.1, settings.n_cost_records)).round(2),
        "VendorType": _choice(rng, ["Interno", "Proveedor local", "Proveedor internacional", "Contratista"], settings.n_cost_records),
    })

    sla_source = fact_ordenes.sample(settings.n_sla_records, replace=settings.n_sla_records > len(fact_ordenes), random_state=int(rng.integers(1, 999_999))).reset_index(drop=True)
    target_hours = np.array([priority_target[p] for p in sla_source["PriorityID"]])
    actual_hours = sla_source["ActualHours"].to_numpy()
    breach = np.maximum(0, actual_hours - target_hours)
    committed = pd.to_datetime(sla_source["CreatedDateKey"].astype(str), format="%Y%m%d") + pd.to_timedelta((target_hours / 24).round().astype(int), unit="D")
    resolved = pd.to_datetime(sla_source["CreatedDateKey"].astype(str), format="%Y%m%d") + pd.to_timedelta(np.ceil(actual_hours / 24).astype(int), unit="D")
    resolved = resolved.clip(upper=pd.Timestamp(end))
    fact_sla = pd.DataFrame({
        "SLAID": _ids("SLA", settings.n_sla_records, 6),
        "WorkOrderID": sla_source["WorkOrderID"],
        "ClientID": _choice(rng, dims["Dim_Cliente"]["ClientID"], settings.n_sla_records),
        "ServiceID": sla_source["ServiceID"],
        "AreaID": sla_source["AreaID"],
        "PriorityID": sla_source["PriorityID"],
        "CreatedDateKey": sla_source["CreatedDateKey"],
        "CommittedDateKey": committed.map(_date_key),
        "ResolvedDateKey": resolved.map(_date_key),
        "TargetHours": target_hours.round(2),
        "ActualHours": actual_hours.round(2),
        "SLAMetFlag": breach <= 0,
        "BreachHours": breach.round(2),
    })

    maint_equipment = _choice(rng, dim_equipo["EquipmentID"], settings.n_maintenance_records)
    maint_area = [equipment_area[eid] for eid in maint_equipment]
    maint_dates = _random_dates(rng, start, end, settings.n_maintenance_records)
    critical_equipment = set(dim_equipo.loc[dim_equipo["Criticality"].eq("Alta"), "EquipmentID"])
    corrective_bias_area = "A002" if dataset_kind == "training" else "A006"
    planned_flag = []
    for eid, area_id in zip(maint_equipment, maint_area):
        corrective_probability = 0.35 + (0.22 if eid in critical_equipment else 0) + (0.18 if area_id == corrective_bias_area else 0)
        planned_flag.append(not bool(rng.random() < corrective_probability))
    downtime = rng.gamma(2.0, 2.2, settings.n_maintenance_records) * np.where(np.array(planned_flag), 0.65, 1.35)
    fact_mantenimiento = pd.DataFrame({
        "MaintenanceID": _ids("MT", settings.n_maintenance_records, 6),
        "DateKey": maint_dates.map(_date_key),
        "EquipmentID": maint_equipment,
        "AreaID": maint_area,
        "WorkTypeID": np.where(planned_flag, "WT1", "WT2"),
        "PriorityID": _choice(rng, ["P1", "P2", "P3", "P4"], settings.n_maintenance_records, p=[0.12, 0.30, 0.40, 0.18]),
        "FailureMode": _choice(rng, ["Desgaste", "Sobrecalentamiento", "Vibración", "Falla eléctrica", "Calibración", "No aplica"], settings.n_maintenance_records),
        "SystemCategory": _choice(rng, ["Mecánico", "Eléctrico", "Control", "TI/OT", "Energía"], settings.n_maintenance_records),
        "DowntimeHours": downtime.round(2),
        "RepairHours": (downtime * rng.uniform(0.4, 0.95, settings.n_maintenance_records)).round(2),
        "MaintenanceCost": (downtime * rng.uniform(180, 950, settings.n_maintenance_records)).round(2),
        "PlannedFlag": planned_flag,
    })

    incident_equipment = _choice(rng, dim_equipo["EquipmentID"], settings.n_incidents)
    incident_area = [equipment_area[eid] for eid in incident_equipment]
    open_area = "A005" if dataset_kind == "training" else "A003"
    action_status = []
    for area_id in incident_area:
        action_status.append(rng.choice(["Abierta", "En progreso", "Cerrada"], p=[0.36, 0.28, 0.36] if area_id == open_area else [0.16, 0.24, 0.60]))
    fact_incidentes = pd.DataFrame({
        "IncidentID": _ids("IN", settings.n_incidents, 5),
        "DateKey": _random_dates(rng, start, end, settings.n_incidents).map(_date_key),
        "AreaID": incident_area,
        "EquipmentID": incident_equipment,
        "LocationID": [equipment_location[eid] for eid in incident_equipment],
        "Severity": _choice(rng, ["Alta", "Media", "Baja"], settings.n_incidents, p=[0.14, 0.36, 0.50]),
        "IncidentType": _choice(rng, ["Casi accidente", "Daño equipo", "Condición insegura", "Ambiental", "Lesión menor"], settings.n_incidents),
        "CorrectiveActionStatus": action_status,
        "DaysOpen": [0 if s == "Cerrada" else int(rng.integers(3, 90)) for s in action_status],
        "LostTimeFlag": rng.choice([True, False], settings.n_incidents, p=[0.08, 0.92]),
        "RiskCategory": _choice(rng, ["Seguridad", "Operación", "Ambiente", "Calidad"], settings.n_incidents),
    })

    energy_equipment = _choice(rng, dim_equipo["EquipmentID"], settings.n_energy_records)
    energy_area = np.array([equipment_area[eid] for eid in energy_equipment])
    energy_dates = _random_dates(rng, start, end, settings.n_energy_records)
    operating = rng.uniform(3, 24, settings.n_energy_records)
    base_kwh = operating * rng.uniform(20, 160, settings.n_energy_records)
    anomaly_area = "A006" if dataset_kind == "training" else "A004"
    anomaly_month = 8 if dataset_kind == "training" else 3
    anomaly_mask = (energy_area == anomaly_area) & (energy_dates.dt.month.to_numpy() == anomaly_month)
    kwh = base_kwh * np.where(anomaly_mask, rng.uniform(1.45, 2.1, settings.n_energy_records), 1.0)
    fact_energia = pd.DataFrame({
        "EnergyID": _ids("EN", settings.n_energy_records, 7),
        "DateKey": energy_dates.map(_date_key),
        "AreaID": energy_area,
        "EquipmentID": energy_equipment,
        "LocationID": [equipment_location[eid] for eid in energy_equipment],
        "kWh": kwh.round(2),
        "EnergyCost": (kwh * rng.uniform(0.34, 0.62, settings.n_energy_records)).round(2),
        "OperatingHours": operating.round(2),
        "OutputUnits": rng.integers(20, 850, settings.n_energy_records),
        "Shift": _choice(rng, ["Día", "Tarde", "Noche"], settings.n_energy_records),
    })

    prod_area = _choice(rng, dim_area["AreaID"], settings.n_productivity_records)
    planned_output = rng.integers(50, 900, settings.n_productivity_records)
    productivity_pressure_area = "A001" if dataset_kind == "training" else "A002"
    actual_output = planned_output * rng.normal(0.94, 0.12, settings.n_productivity_records) * np.where(prod_area == productivity_pressure_area, rng.uniform(0.72, 0.92, settings.n_productivity_records), 1.0)
    labor = rng.uniform(6, 12, settings.n_productivity_records)
    non_productive = labor * rng.uniform(0.08, 0.34, settings.n_productivity_records) * np.where(prod_area == productivity_pressure_area, 1.35, 1.0)
    fact_productividad = pd.DataFrame({
        "ProductivityID": _ids("PD", settings.n_productivity_records, 6),
        "DateKey": _random_dates(rng, start, end, settings.n_productivity_records).map(_date_key),
        "AreaID": prod_area,
        "ResponsibleID": _choice(rng, dim_responsable["ResponsibleID"], settings.n_productivity_records),
        "LocationID": _choice(rng, dims["Dim_Ubicacion"]["LocationID"], settings.n_productivity_records),
        "Shift": _choice(rng, ["Día", "Tarde", "Noche"], settings.n_productivity_records),
        "PlannedOutput": planned_output,
        "ActualOutput": np.maximum(0, actual_output).round(0).astype(int),
        "LaborHours": labor.round(2),
        "ProductiveHours": np.maximum(0, labor - non_productive).round(2),
        "NonProductiveHours": non_productive.round(2),
    })

    facts = {
        "Fact_Proyectos": fact_proyectos,
        "Fact_OrdenesTrabajo": fact_ordenes,
        "Fact_Costos": fact_costos,
        "Fact_SLA": fact_sla,
        "Fact_Mantenimiento": fact_mantenimiento,
        "Fact_Incidentes": fact_incidentes,
        "Fact_Energia": fact_energia,
        "Fact_Productividad": fact_productividad,
    }
    return facts


def generate_dataset(dataset_kind: str, settings: Settings | None = None, root: Path | None = None) -> dict[str, int]:
    if dataset_kind not in {"training", "project"}:
        raise ValueError("dataset_kind debe ser 'training' o 'project'")
    settings = settings or load_settings(root)
    root = (root or settings.repo_root).resolve()
    seed_offset = 0 if dataset_kind == "training" else 10_000
    rng = np.random.default_rng(settings.random_seed + seed_offset)
    output_root = root / "data" / dataset_kind
    dims = build_dimensions(settings, dataset_kind, rng)
    facts = build_facts(settings, dataset_kind, dims, rng)
    clean_tables = {**dims, **facts}
    for name, columns in TABLE_COLUMNS.items():
        clean_tables[name] = clean_tables[name].loc[:, columns]

    if settings.export_csv and settings.include_clean_dataset:
        for name, df in clean_tables.items():
            write_csv(df, output_root / "clean" / f"{name}.csv", root)

    if settings.include_raw_data_quality_issues:
        raw_tables, extras, issues = inject_raw_issues(clean_tables, dataset_kind, rng)
        for name, df in raw_tables.items():
            write_csv(df, output_root / "raw" / f"{name}.csv", root)
        for name, df in extras.items():
            write_csv(df, output_root / "raw" / f"{name}.csv", root)
    else:
        issues = []

    if dataset_kind == "training" and settings.export_sample_files:
        sample_root = output_root / "sample"
        for name in ["Dim_Fecha", "Dim_Area", "Dim_Equipo", "Fact_OrdenesTrabajo", "Fact_SLA", "Fact_Costos"]:
            write_csv(clean_tables[name].head(250), sample_root / f"{name}.csv", root)

    scenario = "Dataset A de entrenamiento" if dataset_kind == "training" else "Dataset B de proyecto final"
    write_text(
        f"""# Escenario de negocio - {scenario}

        Organización sintética Tech&Eng con proyectos técnicos, órdenes de trabajo, mantenimiento, costos, SLA, seguridad, energía y productividad.

                El dataset `{dataset_kind}` usa el mismo esquema común. Dataset A contiene problemas controlados para aprendizaje progresivo; Dataset B conserva el esquema y cambia patrones operativos para evaluación de transferencia.
        """,
        output_root / "metadata" / "business_scenario.md",
        root,
    )
    write_text(
        "# Problemas de calidad controlados\n\n" + "\n".join(f"- {issue}" for issue in issues) + "\n",
        output_root / "metadata" / "data_quality_issues.md",
        root,
    )
    manifest = {
        "dataset_kind": dataset_kind,
        "scenario": scenario,
        "row_counts": {name: int(len(df)) for name, df in clean_tables.items()},
        "schema_tables": list(TABLE_COLUMNS),
        "raw_issues": issues,
        "notes": "Datos 100% sintéticos, sin credenciales ni dependencias cloud.",
    }
    write_json(manifest, output_root / "metadata" / "manifest.json", root)
    logger.info("Dataset %s generado en %s", dataset_kind, output_root)
    return manifest["row_counts"]


def generate_all(settings: Settings | None = None, root: Path | None = None) -> dict[str, dict[str, int]]:
    settings = settings or load_settings(root)
    outputs: dict[str, dict[str, int]] = {}
    if settings.generate_training_dataset:
        outputs["training"] = generate_dataset("training", settings, root)
    if settings.generate_project_dataset and settings.include_project_dataset:
        outputs["project"] = generate_dataset("project", settings, root)
    return outputs


if __name__ == "__main__":
    generate_all()
