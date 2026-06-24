from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import os

try:
    from dotenv import load_dotenv
except Exception:  # pragma: no cover
    load_dotenv = None


REPO_ROOT = Path(__file__).resolve().parents[2]


def _bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "si", "sí"}


def _int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        return default
    return int(value)


@dataclass(frozen=True)
class Settings:
    repo_root: Path = REPO_ROOT
    lab_name: str = "powerbi-techeng-session01"
    lab_env: str = "dev"
    language: str = "es"
    random_seed: int = 42
    generate_training_dataset: bool = True
    generate_project_dataset: bool = True
    training_dataset_name: str = "techeng_training"
    project_dataset_name: str = "techeng_project"
    training_start_date: str = "2024-01-01"
    training_end_date: str = "2024-12-31"
    project_start_date: str = "2025-01-01"
    project_end_date: str = "2025-06-30"
    n_areas: int = 6
    n_equipment: int = 40
    n_clients: int = 20
    n_projects: int = 80
    n_responsibles: int = 30
    n_work_orders: int = 5000
    n_cost_records: int = 2500
    n_sla_records: int = 4000
    n_maintenance_records: int = 1800
    n_incidents: int = 500
    n_energy_records: int = 12000
    n_productivity_records: int = 4000
    include_raw_data_quality_issues: bool = True
    include_clean_dataset: bool = True
    include_project_dataset: bool = True
    export_csv: bool = True
    export_excel_dictionary: bool = True
    export_sample_files: bool = True
    dry_run: bool = False
    overwrite_data: bool = False
    powerbi_desktop_required: bool = False
    create_pbix: bool = False
    ai_api_calls_enabled: bool = False
    allow_external_ai_calls: bool = False

    def with_small_counts(self) -> "Settings":
        return replace(
            self,
            n_equipment=12,
            n_clients=8,
            n_projects=16,
            n_responsibles=10,
            n_work_orders=120,
            n_cost_records=80,
            n_sla_records=90,
            n_maintenance_records=70,
            n_incidents=35,
            n_energy_records=180,
            n_productivity_records=90,
        )


def load_settings(repo_root: Path | None = None) -> Settings:
    root = (repo_root or REPO_ROOT).resolve()
    env_file = root / ".env"
    if load_dotenv and env_file.exists():
        load_dotenv(env_file)
    return Settings(
        repo_root=root,
        lab_name=os.getenv("LAB_NAME", "powerbi-techeng-session01"),
        lab_env=os.getenv("LAB_ENV", "dev"),
        language=os.getenv("LANGUAGE", "es"),
        random_seed=_int("RANDOM_SEED", 42),
        generate_training_dataset=_bool("GENERATE_TRAINING_DATASET", True),
        generate_project_dataset=_bool("GENERATE_PROJECT_DATASET", True),
        training_dataset_name=os.getenv("TRAINING_DATASET_NAME", "techeng_training"),
        project_dataset_name=os.getenv("PROJECT_DATASET_NAME", "techeng_project"),
        training_start_date=os.getenv("TRAINING_START_DATE", "2024-01-01"),
        training_end_date=os.getenv("TRAINING_END_DATE", "2024-12-31"),
        project_start_date=os.getenv("PROJECT_START_DATE", "2025-01-01"),
        project_end_date=os.getenv("PROJECT_END_DATE", "2025-06-30"),
        n_areas=_int("N_AREAS", 6),
        n_equipment=_int("N_EQUIPMENT", 40),
        n_clients=_int("N_CLIENTS", 20),
        n_projects=_int("N_PROJECTS", 80),
        n_responsibles=_int("N_RESPONSIBLES", 30),
        n_work_orders=_int("N_WORK_ORDERS", 5000),
        n_cost_records=_int("N_COST_RECORDS", 2500),
        n_sla_records=_int("N_SLA_RECORDS", 4000),
        n_maintenance_records=_int("N_MAINTENANCE_RECORDS", 1800),
        n_incidents=_int("N_INCIDENTS", 500),
        n_energy_records=_int("N_ENERGY_RECORDS", 12000),
        n_productivity_records=_int("N_PRODUCTIVITY_RECORDS", 4000),
        include_raw_data_quality_issues=_bool("INCLUDE_RAW_DATA_QUALITY_ISSUES", True),
        include_clean_dataset=_bool("INCLUDE_CLEAN_DATASET", True),
        include_project_dataset=_bool("INCLUDE_PROJECT_DATASET", True),
        export_csv=_bool("EXPORT_CSV", True),
        export_excel_dictionary=_bool("EXPORT_EXCEL_DICTIONARY", True),
        export_sample_files=_bool("EXPORT_SAMPLE_FILES", True),
        dry_run=_bool("DRY_RUN", False),
        overwrite_data=_bool("OVERWRITE_DATA", False),
        powerbi_desktop_required=_bool("POWERBI_DESKTOP_REQUIRED", False),
        create_pbix=_bool("CREATE_PBIX", False),
        ai_api_calls_enabled=_bool("AI_API_CALLS_ENABLED", False),
        allow_external_ai_calls=_bool("ALLOW_EXTERNAL_AI_CALLS", False),
    )
