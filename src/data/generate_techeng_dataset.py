from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from src.config.settings import Settings, load_settings
from src.data.data_quality_injector import inject_raw_issues
from src.data.schema import TABLE_COLUMNS
from src.utils.io import write_csv, write_json, write_text
from src.utils.logging import get_logger

logger = get_logger(__name__)


MONTHS_ES = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}
DAYS_ES = {0: "Lunes", 1: "Martes", 2: "Miércoles", 3: "Jueves", 4: "Viernes", 5: "Sábado", 6: "Domingo"}

MINING_AREAS = [
    ("Mina Rajo Abierto", "Operaciones Mina", "Mina"),
    ("Despacho Mina", "Operaciones Mina", "Soporte Operacional"),
    ("Perforación y Tronadura", "Operaciones Mina", "Mina"),
    ("Carguío y Transporte", "Operaciones Mina", "Mina"),
    ("Chancado Primario", "Planta Concentradora", "Planta"),
    ("Transporte por Correas", "Planta Concentradora", "Planta"),
    ("Planta Concentradora", "Planta Concentradora", "Planta"),
    ("Molienda", "Planta Concentradora", "Planta"),
    ("Flotación", "Planta Concentradora", "Planta"),
    ("Espesamiento y Relaves", "Relaves", "Planta"),
    ("Taller Mina", "Mantenimiento", "Mantenimiento"),
    ("Taller Planta", "Mantenimiento", "Mantenimiento"),
    ("Energía y Servicios", "Servicios Mina", "Servicios"),
    ("Seguridad HSE", "Seguridad", "Seguridad"),
    ("Planificación Mina", "Ingeniería", "Ingeniería"),
    ("Control de Procesos", "Automatización", "Soporte Operacional"),
    ("Automatización OT", "Automatización", "Soporte Operacional"),
]

MINING_LOCATIONS = [
    ("Pit Norte", "Sitio Andina Norte", "Mina", "Chile"),
    ("Pit Sur", "Sitio Andina Norte", "Mina", "Chile"),
    ("Frente 4100", "Sitio Andina Norte", "Mina", "Chile"),
    ("Stockpile ROM", "Sitio Andina Norte", "Mina", "Chile"),
    ("Chancador Primario", "Sitio Pampa Central", "Planta", "Chile"),
    ("Faja CV-101", "Sitio Pampa Central", "Planta", "Chile"),
    ("Transferencia CV-203", "Sitio Pampa Central", "Planta", "Chile"),
    ("Molino SAG", "Sitio Pampa Central", "Planta", "Chile"),
    ("Molino de Bolas", "Sitio Pampa Central", "Planta", "Chile"),
    ("Celdas de Flotación", "Sitio Pampa Central", "Planta", "Chile"),
    ("Relavera Principal", "Sitio Sierra Azul", "Relaves", "Chile"),
    ("Sala Eléctrica Planta", "Sitio Pampa Central", "Energía", "Chile"),
    ("Subestación Mina", "Sitio Andina Norte", "Energía", "Chile"),
    ("Taller Camiones", "Sitio Andina Norte", "Mantenimiento", "Chile"),
    ("Taller Palas", "Sitio Andina Norte", "Mantenimiento", "Chile"),
    ("Centro Integrado de Operaciones", "Sitio Andina Norte", "Operaciones", "Chile"),
    ("Sala de Control Planta", "Sitio Pampa Central", "Control", "Chile"),
]

EQUIPMENT_TYPES = [
    "Camión CAEX",
    "Pala eléctrica",
    "Pala hidráulica",
    "Perforadora",
    "Cargador frontal",
    "Bulldozer",
    "Motoniveladora",
    "Camión aljibe",
    "Sistema dispatch",
    "Chancador primario",
    "Chancador secundario",
    "Harnero",
    "Alimentador",
    "Correa transportadora",
    "Molino SAG",
    "Molino de bolas",
    "Bomba de pulpa",
    "Celda de flotación",
    "Espesador",
    "Filtro",
    "Sistema de relaves",
    "PLC",
    "RTU",
    "Servidor SCADA",
    "Servidor Historiador",
    "Switch industrial",
    "Sensor de vibración",
    "Medidor de energía",
    "Sistema de control distribuido",
]

SERVICE_ROWS = [
    ("SV1", "Mantenimiento Mecánico Mina", "Mina", 24),
    ("SV2", "Mantenimiento Eléctrico Mina", "Mina", 24),
    ("SV3", "Mantenimiento Planta", "Planta", 36),
    ("SV4", "Inspección de Correas", "Mantenimiento", 18),
    ("SV5", "Soporte Dispatch", "Operaciones", 12),
    ("SV6", "Automatización y Control", "Automatización", 24),
    ("SV7", "Energía y Subestaciones", "Energía", 36),
    ("SV8", "Seguridad HSE", "Seguridad", 24),
    ("SV9", "Gestión de Relaves", "Planta", 48),
    ("SV10", "Monitoreo Geotécnico", "Ingeniería", 24),
    ("SV11", "Soporte SCADA", "Automatización", 18),
    ("SV12", "Gestión de Paradas Planta", "Mantenimiento", 72),
]

WORK_TYPE_ROWS = [
    ("WT1", "Preventivo", "Preventivo", True),
    ("WT2", "Correctivo no planificado", "Correctivo", False),
    ("WT3", "Predictivo", "Predictivo", True),
    ("WT4", "Inspección operacional", "Inspección", True),
    ("WT5", "Inspección HSE", "Inspección", True),
    ("WT6", "Overhaul", "Proyecto", True),
    ("WT7", "Cambio de componentes", "Correctivo", False),
    ("WT8", "Lubricación", "Preventivo", True),
    ("WT9", "Calibración de instrumentación", "Preventivo", True),
    ("WT10", "Parada planta", "Proyecto", True),
    ("WT11", "Emergencia operacional", "Emergencia", False),
    ("WT12", "Soporte OT", "Emergencia", False),
]

FAILURE_MODES = [
    "Fuga hidráulica",
    "Falla de motor",
    "Sobrecalentamiento",
    "Falla de transmisión",
    "Desgaste de neumáticos",
    "Falla de pala",
    "Desalineamiento de correa",
    "Corte de correa",
    "Bloqueo de chancador",
    "Desgaste de revestimientos",
    "Falla de bomba de pulpa",
    "Falla de sello mecánico",
    "Falla eléctrica",
    "Trip de variador",
    "Pérdida de comunicación PLC",
    "Deriva de sensor",
    "Alta vibración",
    "Baja presión",
    "Obstrucción de chute",
    "Falla de instrumentación",
]


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


def _area_id_by_name(dim_area: pd.DataFrame, name: str) -> str:
    match = dim_area.loc[dim_area["AreaName"].eq(name), "AreaID"]
    return str(match.iloc[0]) if not match.empty else str(dim_area["AreaID"].iloc[0])


def _equipment_area_for_type(equipment_type: str, area_by_name: dict[str, str]) -> str:
    mine_types = {"Camión CAEX", "Pala eléctrica", "Pala hidráulica", "Perforadora", "Cargador frontal", "Bulldozer", "Motoniveladora", "Camión aljibe", "Sistema dispatch"}
    crushing_types = {"Chancador primario", "Chancador secundario", "Harnero", "Alimentador"}
    conveyor_types = {"Correa transportadora"}
    grinding_types = {"Molino SAG", "Molino de bolas"}
    flotation_types = {"Celda de flotación"}
    tailings_types = {"Espesador", "Filtro", "Sistema de relaves"}
    ot_types = {"PLC", "RTU", "Servidor SCADA", "Servidor Historiador", "Switch industrial", "Sensor de vibración", "Sistema de control distribuido"}
    energy_types = {"Medidor de energía"}
    if equipment_type in mine_types:
        return area_by_name.get("Carguío y Transporte", area_by_name.get("Mina Rajo Abierto"))
    if equipment_type in crushing_types:
        return area_by_name.get("Chancado Primario", area_by_name.get("Planta Concentradora"))
    if equipment_type in conveyor_types:
        return area_by_name.get("Transporte por Correas", area_by_name.get("Planta Concentradora"))
    if equipment_type in grinding_types:
        return area_by_name.get("Molienda", area_by_name.get("Planta Concentradora"))
    if equipment_type in flotation_types:
        return area_by_name.get("Flotación", area_by_name.get("Planta Concentradora"))
    if equipment_type in tailings_types:
        return area_by_name.get("Espesamiento y Relaves", area_by_name.get("Planta Concentradora"))
    if equipment_type in ot_types:
        return area_by_name.get("Automatización OT", area_by_name.get("Control de Procesos"))
    if equipment_type in energy_types:
        return area_by_name.get("Energía y Servicios", area_by_name.get("Planta Concentradora"))
    return area_by_name.get("Taller Planta", area_by_name.get("Planta Concentradora"))


def build_dimensions(settings: Settings, dataset_kind: str, rng: np.random.Generator) -> dict[str, pd.DataFrame]:
    start = settings.training_start_date if dataset_kind == "training" else settings.project_start_date
    end = settings.training_end_date if dataset_kind == "training" else settings.project_end_date
    dates = pd.date_range(start, end, freq="D")
    dim_fecha = pd.DataFrame(
        {
            "DateKey": [int(d.strftime("%Y%m%d")) for d in dates],
            "Date": [d.strftime("%Y-%m-%d") for d in dates],
            "Year": [d.year for d in dates],
            "Quarter": [f"Q{d.quarter}" for d in dates],
            "MonthNumber": [d.month for d in dates],
            "MonthName": [MONTHS_ES[d.month] for d in dates],
            "WeekNumber": dates.isocalendar().week.astype(int).to_list(),
            "DayOfWeek": [DAYS_ES[d.dayofweek] for d in dates],
            "IsWeekend": [d.dayofweek >= 5 for d in dates],
        }
    )

    n_locations = max(8, min(len(MINING_LOCATIONS), settings.n_areas + 2))
    locations = MINING_LOCATIONS[:n_locations]
    dim_ubicacion = pd.DataFrame(
        {
            "LocationID": _ids("L", n_locations),
            "LocationName": [row[0] for row in locations],
            "Site": [row[1] for row in locations],
            "Zone": [row[2] for row in locations],
            "Country": [row[3] for row in locations],
        }
    )

    areas = (MINING_AREAS * ((settings.n_areas // len(MINING_AREAS)) + 1))[: settings.n_areas]
    dim_area = pd.DataFrame(
        {
            "AreaID": _ids("A", settings.n_areas),
            "AreaName": [row[0] for row in areas],
            "BusinessUnit": [row[1] for row in areas],
            "AreaType": [row[2] for row in areas],
            "ManagerName": [f"Gerente Sintético Mina {i:02d}" for i in range(1, settings.n_areas + 1)],
            "LocationID": _choice(rng, dim_ubicacion["LocationID"], settings.n_areas),
        }
    )
    area_by_name = dict(zip(dim_area["AreaName"], dim_area["AreaID"]))

    equipment_type_values = (EQUIPMENT_TYPES * ((settings.n_equipment // len(EQUIPMENT_TYPES)) + 1))[: settings.n_equipment]
    rng.shuffle(equipment_type_values)
    area_for_equipment = [_equipment_area_for_type(equipment_type, area_by_name) for equipment_type in equipment_type_values]
    dim_equipo = pd.DataFrame(
        {
            "EquipmentID": _ids("EQ", settings.n_equipment, 4),
            "EquipmentName": [f"{equipment_type_values[i - 1]} Sintético {i:04d}" for i in range(1, settings.n_equipment + 1)],
            "EquipmentType": equipment_type_values,
            "Criticality": _choice(rng, ["Crítica", "Alta", "Media", "Baja"], settings.n_equipment, p=[0.22, 0.34, 0.32, 0.12]),
            "AreaID": area_for_equipment,
            "Manufacturer": _choice(rng, ["Andes Mining Systems", "Pampa Controls", "Sierra Motion", "Kuntur Industrial", "NovaMine"], settings.n_equipment),
            "Model": [f"MIN-{rng.integers(100,999)}" for _ in range(settings.n_equipment)],
            "CommissioningDate": _random_dates(rng, "2015-01-01", start, settings.n_equipment).dt.strftime("%Y-%m-%d"),
            "ActiveFlag": rng.choice([True, False], size=settings.n_equipment, p=[0.95, 0.05]),
        }
    )

    mining_clients = [
        "Operaciones Mina Norte",
        "Planta Concentradora Central",
        "Gerencia de Mantenimiento",
        "Gerencia HSE",
        "Gerencia Energía",
        "Gerencia Proyectos Mina",
        "Contrato Servicios Mina",
        "Contrato Mantenimiento Planta",
        "Centro Integrado de Operaciones",
        "Superintendencia Chancado",
        "Superintendencia Molienda",
        "Superintendencia Relaves",
        "Superintendencia Mina",
        "Contrato Automatización OT",
        "Contrato Energía Planta",
        "Superintendencia Flotación",
    ]
    client_names = (mining_clients * ((settings.n_clients // len(mining_clients)) + 1))[: settings.n_clients]
    dim_cliente = pd.DataFrame(
        {
            "ClientID": _ids("C", settings.n_clients),
            "ClientName": client_names,
            "Segment": _choice(rng, ["Minería", "Servicios Mineros", "Operaciones Industriales", "Energía Industrial", "Mantenimiento Industrial"], settings.n_clients, p=[0.45, 0.25, 0.12, 0.10, 0.08]),
            "Region": _choice(rng, ["Norte", "Cordillera", "Pampa", "Centro", "Costa"], settings.n_clients),
            "ContractType": _choice(rng, ["SLA Operacional", "Proyecto Mina", "Contrato Marco", "Servicio Especializado"], settings.n_clients),
        }
    )

    dim_prioridad = pd.DataFrame(
        {
            "PriorityID": ["P1", "P2", "P3", "P4"],
            "PriorityName": ["Crítica", "Alta", "Media", "Baja"],
            "PriorityRank": [1, 2, 3, 4],
            "TargetResponseHours": [1, 4, 12, 24],
            "TargetResolutionHours": [8, 24, 72, 120],
        }
    )
    dim_estado = pd.DataFrame(
        {
            "StatusID": ["S1", "S2", "S3", "S4", "S5"],
            "StatusName": ["Abierta", "En Proceso", "Vencida", "Cerrada", "Cancelada"],
            "StatusGroup": ["Abierto", "Abierto", "Abierto", "Cerrado", "Cerrado"],
            "SortOrder": [1, 2, 3, 4, 5],
            "IsClosed": [False, False, False, True, True],
        }
    )
    dim_tipo = pd.DataFrame(
        {
            "WorkTypeID": [row[0] for row in WORK_TYPE_ROWS],
            "WorkTypeName": [row[1] for row in WORK_TYPE_ROWS],
            "WorkCategory": [row[2] for row in WORK_TYPE_ROWS],
            "PlannedFlag": [row[3] for row in WORK_TYPE_ROWS],
        }
    )
    dim_servicio = pd.DataFrame(
        {
            "ServiceID": [row[0] for row in SERVICE_ROWS],
            "ServiceName": [row[1] for row in SERVICE_ROWS],
            "ServiceCategory": [row[2] for row in SERVICE_ROWS],
            "DefaultSLAHours": [row[3] for row in SERVICE_ROWS],
        }
    )

    mining_roles = [
        "Ingeniero de Confiabilidad",
        "Ingeniero de Mantenimiento Mina",
        "Ingeniero de Mantenimiento Planta",
        "Supervisor de Operaciones Mina",
        "Supervisor de Chancado",
        "Supervisor de Molienda",
        "Analista Dispatch",
        "Especialista OT",
        "Ingeniero de Automatización",
        "Ingeniero HSE",
        "Planificador de Mantenimiento",
        "Coordinador de Parada Planta",
        "Analista de Energía",
        "Ingeniero de Producción",
        "Jefe de Turno",
        "Analista de Costos Operacionales",
    ]
    dim_responsable = pd.DataFrame(
        {
            "ResponsibleID": _ids("R", settings.n_responsibles),
            "ResponsibleName": [f"Responsable Minero Sintético {i:02d}" for i in range(1, settings.n_responsibles + 1)],
            "Role": _choice(rng, mining_roles, settings.n_responsibles),
            "Team": _choice(rng, ["Turno A", "Turno B", "Turno C", "Guardia Planta", "Backoffice Mina"], settings.n_responsibles),
            "AreaID": _choice(rng, dim_area["AreaID"], settings.n_responsibles),
        }
    )

    project_names_base = [
        "Optimización de Chancado Primario",
        "Reemplazo de Correa CV-101",
        "Mejora de Disponibilidad de Camiones CAEX",
        "Modernización Sistema Dispatch",
        "Upgrade SCADA Planta",
        "Reducción de Consumo Energético en Molienda",
        "Programa de Seguridad en Taller Mina",
        "Mejoramiento Sistema de Relaves",
        "Cambio de Revestimientos Molino SAG",
        "Automatización de Reporte de Producción",
        "Proyecto de Monitoreo Geotécnico",
        "Mejora de Confiabilidad de Bombas de Pulpa",
        "Programa de Reducción de Backlog",
        "Optimización de Flotación",
        "Reemplazo de Variadores en Correas",
        "Implementación de Tablero Operacional",
    ]
    project_dates = _random_dates(rng, start, end, settings.n_projects)
    durations = rng.integers(30, 180, size=settings.n_projects)
    dim_proyecto = pd.DataFrame(
        {
            "ProjectID": _ids("PR", settings.n_projects, 4),
            "ProjectName": [f"{project_names_base[(i - 1) % len(project_names_base)]} {i:03d}" for i in range(1, settings.n_projects + 1)],
            "ProjectType": _choice(rng, ["Confiabilidad", "Energía", "Seguridad", "Producción", "Mantenimiento", "Automatización", "Infraestructura", "Planta", "Mina", "Transformación Digital"], settings.n_projects),
            "ClientID": _choice(rng, dim_cliente["ClientID"], settings.n_projects),
            "AreaID": _choice(rng, dim_area["AreaID"], settings.n_projects),
            "ResponsibleID": _choice(rng, dim_responsable["ResponsibleID"], settings.n_projects),
            "PriorityID": _choice(rng, dim_prioridad["PriorityID"], settings.n_projects, p=[0.18, 0.36, 0.32, 0.14]),
            "PlannedStartDate": project_dates.dt.strftime("%Y-%m-%d"),
            "PlannedEndDate": (project_dates + pd.to_timedelta(durations, unit="D")).dt.strftime("%Y-%m-%d"),
        }
    )

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


def _failure_mode_for_equipment(equipment_type: str, rng: np.random.Generator) -> tuple[str, str]:
    if "CAEX" in equipment_type:
        return str(rng.choice(["Desgaste de neumáticos", "Falla de motor", "Falla de transmisión"])), str(rng.choice(["Neumáticos", "Mecánico", "Hidráulico"]))
    if "Pala" in equipment_type or "Perforadora" in equipment_type:
        return str(rng.choice(["Fuga hidráulica", "Falla de pala", "Alta vibración"])), str(rng.choice(["Hidráulico", "Mecánico", "Control"]))
    if "Correa" in equipment_type:
        return str(rng.choice(["Desalineamiento de correa", "Corte de correa", "Obstrucción de chute"])), "Correas"
    if "Chancador" in equipment_type:
        return str(rng.choice(["Bloqueo de chancador", "Alta vibración", "Falla eléctrica"])), "Chancado"
    if "Molino" in equipment_type:
        return str(rng.choice(["Desgaste de revestimientos", "Alta vibración", "Trip de variador"])), "Molienda"
    if "Bomba" in equipment_type:
        return str(rng.choice(["Falla de bomba de pulpa", "Falla de sello mecánico", "Baja presión"])), "Bombas"
    if equipment_type in {"PLC", "RTU", "Servidor SCADA", "Servidor Historiador", "Switch industrial", "Sistema de control distribuido"}:
        return str(rng.choice(["Pérdida de comunicación PLC", "Falla de instrumentación", "Deriva de sensor"])), "Control"
    return str(rng.choice(FAILURE_MODES)), str(rng.choice(["Mecánico", "Eléctrico", "Instrumentación", "Energía", "Seguridad"]))


def build_facts(settings: Settings, dataset_kind: str, dims: dict[str, pd.DataFrame], rng: np.random.Generator) -> dict[str, pd.DataFrame]:
    start = settings.training_start_date if dataset_kind == "training" else settings.project_start_date
    end = settings.training_end_date if dataset_kind == "training" else settings.project_end_date
    dim_area = dims["Dim_Area"]
    dim_equipo = dims["Dim_Equipo"]
    dim_proyecto = dims["Dim_Proyecto"]
    dim_responsable = dims["Dim_Responsable"]
    dim_prioridad = dims["Dim_Prioridad"]

    area_by_name = dict(zip(dim_area["AreaName"], dim_area["AreaID"]))
    equipment_area = dim_equipo.set_index("EquipmentID")["AreaID"].to_dict()
    equipment_type = dim_equipo.set_index("EquipmentID")["EquipmentType"].to_dict()
    equipment_criticality = dim_equipo.set_index("EquipmentID")["Criticality"].to_dict()
    equipment_location = dim_equipo[["EquipmentID", "AreaID"]].merge(dim_area[["AreaID", "LocationID"]], on="AreaID").set_index("EquipmentID")["LocationID"].to_dict()
    priority_target = dim_prioridad.set_index("PriorityID")["TargetResolutionHours"].to_dict()

    pressure = {
        "training": {
            "delay": {_area_id_by_name(dim_area, "Chancado Primario"), _area_id_by_name(dim_area, "Transporte por Correas")},
            "cost": {_area_id_by_name(dim_area, "Transporte por Correas"), _area_id_by_name(dim_area, "Molienda")},
            "backlog": {_area_id_by_name(dim_area, "Taller Mina"), _area_id_by_name(dim_area, "Chancado Primario")},
            "sla": {_area_id_by_name(dim_area, "Chancado Primario"), _area_id_by_name(dim_area, "Transporte por Correas"), _area_id_by_name(dim_area, "Taller Planta")},
            "maintenance": {_area_id_by_name(dim_area, "Chancado Primario"), _area_id_by_name(dim_area, "Transporte por Correas")},
            "energy": {_area_id_by_name(dim_area, "Molienda")},
            "productivity": {_area_id_by_name(dim_area, "Chancado Primario"), _area_id_by_name(dim_area, "Molienda"), _area_id_by_name(dim_area, "Carguío y Transporte")},
            "safety": {_area_id_by_name(dim_area, "Taller Mina"), _area_id_by_name(dim_area, "Carguío y Transporte"), _area_id_by_name(dim_area, "Transporte por Correas")},
        },
        "project": {
            "delay": {_area_id_by_name(dim_area, "Despacho Mina"), _area_id_by_name(dim_area, "Espesamiento y Relaves")},
            "cost": {_area_id_by_name(dim_area, "Molienda"), _area_id_by_name(dim_area, "Espesamiento y Relaves")},
            "backlog": {_area_id_by_name(dim_area, "Planta Concentradora"), _area_id_by_name(dim_area, "Molienda"), _area_id_by_name(dim_area, "Espesamiento y Relaves")},
            "sla": {_area_id_by_name(dim_area, "Mina Rajo Abierto"), _area_id_by_name(dim_area, "Despacho Mina"), _area_id_by_name(dim_area, "Carguío y Transporte")},
            "maintenance": {_area_id_by_name(dim_area, "Molienda"), _area_id_by_name(dim_area, "Espesamiento y Relaves"), _area_id_by_name(dim_area, "Automatización OT")},
            "energy": {_area_id_by_name(dim_area, "Espesamiento y Relaves"), _area_id_by_name(dim_area, "Chancado Primario")},
            "productivity": {_area_id_by_name(dim_area, "Flotación"), _area_id_by_name(dim_area, "Espesamiento y Relaves"), _area_id_by_name(dim_area, "Planta Concentradora")},
            "safety": {_area_id_by_name(dim_area, "Espesamiento y Relaves"), _area_id_by_name(dim_area, "Planta Concentradora")},
        },
    }[dataset_kind]

    projects = dim_proyecto.copy()
    n_projects = len(projects)
    project_dates = _random_dates(rng, start, end, n_projects)
    planned_progress = rng.uniform(35, 100, n_projects).round(1)
    delay_mask = projects["AreaID"].isin(pressure["delay"]).to_numpy()
    delay_days = rng.poisson(4, n_projects) + (delay_mask * rng.integers(10, 42, n_projects))
    actual_progress = np.maximum(0, planned_progress - rng.uniform(0, 16, n_projects) - (delay_mask * rng.uniform(7, 24, n_projects))).round(1)
    planned_cost = rng.uniform(50_000, 750_000, n_projects).round(2)
    cost_mask = projects["AreaID"].isin(pressure["cost"]).to_numpy()
    actual_cost = (planned_cost * rng.normal(1.02, 0.14, n_projects) * np.where(cost_mask, rng.uniform(1.15, 1.55, n_projects), 1)).round(2)
    fact_proyectos = pd.DataFrame(
        {
            "ProjectFactID": _ids("PF", n_projects, 5),
            "ProjectID": projects["ProjectID"],
            "DateKey": project_dates.map(_date_key),
            "AreaID": projects["AreaID"],
            "ClientID": projects["ClientID"],
            "ResponsibleID": projects["ResponsibleID"],
            "StatusID": _choice(rng, ["S1", "S2", "S3", "S4"], n_projects, p=[0.08, 0.42, 0.17, 0.33]),
            "PriorityID": projects["PriorityID"],
            "PlannedProgressPct": planned_progress,
            "ActualProgressPct": actual_progress,
            "PlannedCost": planned_cost,
            "ActualCost": actual_cost,
            "RiskScore": np.clip(rng.normal(44, 18, n_projects) + delay_mask * rng.uniform(18, 34, n_projects) + cost_mask * rng.uniform(8, 20, n_projects), 1, 100).round(1),
            "DelayDays": delay_days.astype(int),
        }
    )

    wo_equipment = _choice(rng, dim_equipo["EquipmentID"], settings.n_work_orders)
    wo_area = np.array([equipment_area[eid] for eid in wo_equipment])
    wo_type = np.array([equipment_type[eid] for eid in wo_equipment])
    created_dates = _random_dates(rng, start, end, settings.n_work_orders)
    priority = _choice(rng, ["P1", "P2", "P3", "P4"], settings.n_work_orders, p=[0.16, 0.34, 0.34, 0.16])
    backlog_mask = np.isin(wo_area, list(pressure["backlog"]))
    status = []
    for is_pressure in backlog_mask:
        status.append(str(rng.choice(["S1", "S2", "S3", "S4", "S5"], p=[0.20, 0.26, 0.18, 0.32, 0.04] if is_pressure else [0.08, 0.18, 0.06, 0.64, 0.04])))
    work_type_ids = _choice(rng, dims["Dim_TipoTrabajo"]["WorkTypeID"], settings.n_work_orders, p=[0.18, 0.24, 0.12, 0.12, 0.07, 0.06, 0.07, 0.06, 0.03, 0.03, 0.01, 0.01])
    estimated = np.array([priority_target[p] for p in priority]) * rng.uniform(0.35, 0.9, settings.n_work_orders)
    corrective_mask = np.isin(work_type_ids, ["WT2", "WT7", "WT11", "WT12"])
    actual = estimated * rng.lognormal(mean=0.10, sigma=0.42, size=settings.n_work_orders) * np.where(backlog_mask | corrective_mask, rng.uniform(1.18, 1.55, settings.n_work_orders), 1.0)
    closed_dates = []
    for created, status_id, hours in zip(created_dates, status, actual):
        if status_id in {"S4", "S5"}:
            closed = min(pd.Timestamp(end), created + pd.to_timedelta(max(1, int(hours // 8) + 1), unit="D"))
            closed_dates.append(_date_key(closed))
        else:
            closed_dates.append(pd.NA)
    rework_pressure = np.char.find(wo_type.astype(str), "Correa") >= 0 if dataset_kind == "training" else ((np.char.find(wo_type.astype(str), "Molino") >= 0) | (np.char.find(wo_type.astype(str), "relaves") >= 0))
    fact_ordenes = pd.DataFrame(
        {
            "WorkOrderID": _ids("WO", settings.n_work_orders, 6),
            "CreatedDateKey": created_dates.map(_date_key),
            "ClosedDateKey": pd.array(closed_dates, dtype="Int64"),
            "AreaID": wo_area,
            "EquipmentID": wo_equipment,
            "ServiceID": _choice(rng, dims["Dim_Servicio"]["ServiceID"], settings.n_work_orders),
            "ResponsibleID": _choice(rng, dim_responsable["ResponsibleID"], settings.n_work_orders),
            "WorkTypeID": work_type_ids,
            "PriorityID": priority,
            "StatusID": status,
            "EstimatedHours": estimated.round(2),
            "ActualHours": actual.round(2),
            "IsCritical": np.isin(priority, ["P1", "P2"]) | np.isin([equipment_criticality[eid] for eid in wo_equipment], ["Crítica"]),
            "ReworkFlag": rng.random(settings.n_work_orders) < np.where(rework_pressure, 0.28, 0.09),
            "SourceSystem": _choice(rng, ["SAP PM", "Maximo", "SCADA", "Dispatch", "Excel Manual"], settings.n_work_orders, p=[0.36, 0.26, 0.16, 0.14, 0.08]),
        }
    )

    cost_projects = dim_proyecto.sample(settings.n_cost_records, replace=True, random_state=int(rng.integers(1, 999_999))).reset_index(drop=True)
    cost_equipment = _choice(rng, dim_equipo["EquipmentID"], settings.n_cost_records)
    cost_area = np.array([equipment_area[eid] for eid in cost_equipment])
    budget = rng.uniform(2_000, 160_000, settings.n_cost_records)
    cost_mask_records = np.isin(cost_area, list(pressure["cost"]))
    cost_factor = np.where(cost_mask_records, rng.uniform(1.14, 1.65, settings.n_cost_records), rng.normal(1.0, 0.16, settings.n_cost_records))
    cost_category = _choice(rng, ["Repuestos", "Mano de obra", "Contratistas", "Energía", "Neumáticos", "Lubricantes", "Componentes mayores", "Instrumentación", "Servicios externos", "Parada planta", "Seguridad", "Automatización", "Materiales de desgaste"], settings.n_cost_records)
    fact_costos = pd.DataFrame(
        {
            "CostID": _ids("CO", settings.n_cost_records, 6),
            "DateKey": _random_dates(rng, start, end, settings.n_cost_records).map(_date_key),
            "ProjectID": cost_projects["ProjectID"],
            "AreaID": cost_area,
            "EquipmentID": cost_equipment,
            "CostCategory": cost_category,
            "BudgetAmount": budget.round(2),
            "ActualAmount": (budget * cost_factor).round(2),
            "CommittedAmount": (budget * rng.uniform(0.2, 1.1, settings.n_cost_records)).round(2),
            "VendorType": _choice(rng, ["Interno", "Proveedor local", "Proveedor internacional", "Contratista minero"], settings.n_cost_records),
        }
    )

    sla_source = fact_ordenes.sample(settings.n_sla_records, replace=settings.n_sla_records > len(fact_ordenes), random_state=int(rng.integers(1, 999_999))).reset_index(drop=True)
    target_hours = np.array([priority_target[p] for p in sla_source["PriorityID"]])
    sla_mask = sla_source["AreaID"].isin(pressure["sla"]).to_numpy() | sla_source["PriorityID"].eq("P1").to_numpy()
    actual_hours = sla_source["ActualHours"].to_numpy() * np.where(sla_mask, rng.uniform(1.15, 1.65, settings.n_sla_records), rng.uniform(0.82, 1.12, settings.n_sla_records))
    breach = np.maximum(0, actual_hours - target_hours)
    committed = pd.to_datetime(sla_source["CreatedDateKey"].astype(str), format="%Y%m%d") + pd.to_timedelta((target_hours / 24).round().astype(int), unit="D")
    resolved = pd.to_datetime(sla_source["CreatedDateKey"].astype(str), format="%Y%m%d") + pd.to_timedelta(np.ceil(actual_hours / 24).astype(int), unit="D")
    resolved = resolved.clip(upper=pd.Timestamp(end))
    fact_sla = pd.DataFrame(
        {
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
        }
    )

    maint_equipment = _choice(rng, dim_equipo["EquipmentID"], settings.n_maintenance_records)
    maint_area = np.array([equipment_area[eid] for eid in maint_equipment])
    maint_type = np.array([equipment_type[eid] for eid in maint_equipment])
    critical_equipment = np.isin([equipment_criticality[eid] for eid in maint_equipment], ["Crítica", "Alta"])
    pressure_maint = np.isin(maint_area, list(pressure["maintenance"]))
    planned_flag = rng.random(settings.n_maintenance_records) > (0.30 + 0.22 * critical_equipment + 0.20 * pressure_maint)
    failure_rows = [_failure_mode_for_equipment(e_type, rng) for e_type in maint_type]
    downtime = rng.gamma(2.2, 2.4, settings.n_maintenance_records) * np.where(planned_flag, 0.62, 1.45) * np.where(pressure_maint, 1.45, 1.0)
    fact_mantenimiento = pd.DataFrame(
        {
            "MaintenanceID": _ids("MT", settings.n_maintenance_records, 6),
            "DateKey": _random_dates(rng, start, end, settings.n_maintenance_records).map(_date_key),
            "EquipmentID": maint_equipment,
            "AreaID": maint_area,
            "WorkTypeID": np.where(planned_flag, "WT1", "WT2"),
            "PriorityID": _choice(rng, ["P1", "P2", "P3", "P4"], settings.n_maintenance_records, p=[0.16, 0.34, 0.34, 0.16]),
            "FailureMode": [row[0] for row in failure_rows],
            "SystemCategory": [row[1] for row in failure_rows],
            "DowntimeHours": downtime.round(2),
            "RepairHours": (downtime * rng.uniform(0.38, 0.95, settings.n_maintenance_records)).round(2),
            "MaintenanceCost": (downtime * rng.uniform(450, 2400, settings.n_maintenance_records) * np.where(np.char.find(maint_type.astype(str), "CAEX") >= 0, 1.45, 1.0)).round(2),
            "PlannedFlag": planned_flag,
        }
    )

    incident_equipment = _choice(rng, dim_equipo["EquipmentID"], settings.n_incidents)
    incident_area = np.array([equipment_area[eid] for eid in incident_equipment])
    safety_mask = np.isin(incident_area, list(pressure["safety"]))
    action_status = [str(rng.choice(["Abierta", "En Proceso", "Cerrada", "Vencida"], p=[0.26, 0.26, 0.30, 0.18] if is_pressure else [0.12, 0.20, 0.62, 0.06])) for is_pressure in safety_mask]
    fact_incidentes = pd.DataFrame(
        {
            "IncidentID": _ids("IN", settings.n_incidents, 5),
            "DateKey": _random_dates(rng, start, end, settings.n_incidents).map(_date_key),
            "AreaID": incident_area,
            "EquipmentID": incident_equipment,
            "LocationID": [equipment_location[eid] for eid in incident_equipment],
            "Severity": [str(rng.choice(["Crítica", "Alta", "Media", "Baja"], p=[0.10, 0.30, 0.42, 0.18] if is_pressure else [0.03, 0.14, 0.38, 0.45])) for is_pressure in safety_mask],
            "IncidentType": _choice(rng, ["Casi accidente", "Incidente operacional", "Incidente de tránsito mina", "Evento HSE", "Condición subestándar", "Acto subestándar", "Derrame menor", "Exposición a energía", "Bloqueo y etiquetado", "Riesgo geotécnico", "Evento en correa", "Evento en taller", "Falla de control crítico"], settings.n_incidents),
            "CorrectiveActionStatus": action_status,
            "DaysOpen": [0 if s == "Cerrada" else int(rng.integers(5, 120)) for s in action_status],
            "LostTimeFlag": rng.choice([True, False], settings.n_incidents, p=[0.10, 0.90]),
            "RiskCategory": _choice(rng, ["Seguridad", "Operación", "Ambiente", "Calidad", "Geotecnia"], settings.n_incidents),
        }
    )

    energy_equipment = _choice(rng, dim_equipo["EquipmentID"], settings.n_energy_records)
    energy_area = np.array([equipment_area[eid] for eid in energy_equipment])
    energy_dates = _random_dates(rng, start, end, settings.n_energy_records)
    energy_shift = _choice(rng, ["Día", "Tarde", "Noche"], settings.n_energy_records)
    operating = rng.uniform(4, 24, settings.n_energy_records)
    base_kwh = operating * rng.uniform(80, 520, settings.n_energy_records)
    anomaly_month = 8 if dataset_kind == "training" else 3
    anomaly_mask = np.isin(energy_area, list(pressure["energy"])) & (energy_dates.dt.month.to_numpy() == anomaly_month)
    night_mask = energy_shift == "Noche"
    kwh = base_kwh * np.where(anomaly_mask, rng.uniform(1.35, 2.05, settings.n_energy_records), 1.0) * np.where(night_mask & anomaly_mask, 1.18, 1.0)
    output_units = rng.integers(100, 4200, settings.n_energy_records) * np.where(anomaly_mask, rng.uniform(0.65, 0.88, settings.n_energy_records), 1.0)
    fact_energia = pd.DataFrame(
        {
            "EnergyID": _ids("EN", settings.n_energy_records, 7),
            "DateKey": energy_dates.map(_date_key),
            "AreaID": energy_area,
            "EquipmentID": energy_equipment,
            "LocationID": [equipment_location[eid] for eid in energy_equipment],
            "kWh": kwh.round(2),
            "EnergyCost": (kwh * rng.uniform(0.09, 0.18, settings.n_energy_records)).round(2),
            "OperatingHours": operating.round(2),
            "OutputUnits": np.maximum(1, output_units.round(0).astype(int)),
            "Shift": energy_shift,
        }
    )

    prod_area = _choice(rng, dim_area["AreaID"], settings.n_productivity_records)
    prod_shift = _choice(rng, ["Día", "Tarde", "Noche"], settings.n_productivity_records)
    area_type_lookup = dim_area.set_index("AreaID")["AreaType"].to_dict()
    planned_output = np.array([rng.integers(2200, 8500) if area_type_lookup.get(a) == "Mina" else rng.integers(600, 4200) if area_type_lookup.get(a) == "Planta" else rng.integers(20, 260) for a in prod_area])
    prod_pressure = np.isin(prod_area, list(pressure["productivity"]))
    night_pressure = prod_shift == "Noche"
    ratio = rng.normal(0.96, 0.11, settings.n_productivity_records) * np.where(prod_pressure, rng.uniform(0.72, 0.92, settings.n_productivity_records), 1.0) * np.where(prod_pressure & night_pressure, 0.86, 1.0)
    actual_output = np.maximum(0, planned_output * ratio)
    labor = rng.uniform(6, 12, settings.n_productivity_records)
    non_productive = labor * rng.uniform(0.08, 0.32, settings.n_productivity_records) * np.where(prod_pressure, 1.35, 1.0)
    fact_productividad = pd.DataFrame(
        {
            "ProductivityID": _ids("PD", settings.n_productivity_records, 6),
            "DateKey": _random_dates(rng, start, end, settings.n_productivity_records).map(_date_key),
            "AreaID": prod_area,
            "ResponsibleID": _choice(rng, dim_responsable["ResponsibleID"], settings.n_productivity_records),
            "LocationID": _choice(rng, dims["Dim_Ubicacion"]["LocationID"], settings.n_productivity_records),
            "Shift": prod_shift,
            "PlannedOutput": planned_output,
            "ActualOutput": actual_output.round(0).astype(int),
            "LaborHours": labor.round(2),
            "ProductiveHours": np.maximum(0, labor - non_productive).round(2),
            "NonProductiveHours": non_productive.round(2),
        }
    )

    return {
        "Fact_Proyectos": fact_proyectos,
        "Fact_OrdenesTrabajo": fact_ordenes,
        "Fact_Costos": fact_costos,
        "Fact_SLA": fact_sla,
        "Fact_Mantenimiento": fact_mantenimiento,
        "Fact_Incidentes": fact_incidentes,
        "Fact_Energia": fact_energia,
        "Fact_Productividad": fact_productividad,
    }


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
        for name in ["Dim_Fecha", "Dim_Area", "Dim_Equipo", "Dim_Servicio", "Dim_Prioridad", "Dim_Estado", "Fact_OrdenesTrabajo", "Fact_SLA", "Fact_Costos"]:
            write_csv(clean_tables[name].head(250), sample_root / f"{name}.csv", root)

    scenario = "Dataset A de entrenamiento minero" if dataset_kind == "training" else "Dataset B de proyecto final minero"
    pattern = "Chancado, correas, molienda, taller mina y energía en molienda" if dataset_kind == "training" else "Dispatch, relaves, molienda, flota mina y OT planta"
    write_text(
        f"""# Escenario de negocio - {scenario}

Organización sintética Tech&Eng minera con operación de rajo abierto y planta concentradora. Gestiona flota mina, chancado, correas, molienda, flotación, relaves, mantenimiento, costos, SLA, seguridad HSE, energía y productividad por turno.

El dataset `{dataset_kind}` usa el mismo esquema común que el otro dataset. Sus patrones operacionales principales son: {pattern}. Los datos son 100% sintéticos y no representan faenas, empresas ni personas reales.
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
        "mining_context": True,
        "mining_pattern": pattern,
        "row_counts": {name: int(len(df)) for name, df in clean_tables.items()},
        "schema_tables": list(TABLE_COLUMNS),
        "raw_issues": issues,
        "notes": "Datos 100% sintéticos, sin credenciales, sin dependencias cloud y sin nombres reales de faenas.",
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
