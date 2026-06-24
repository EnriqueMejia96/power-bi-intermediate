from __future__ import annotations

import json

import pandas as pd

from src.config.settings import load_settings
from src.data.generate_techeng_dataset import generate_dataset


def _generate_all(local_tmp_path):
    settings = load_settings(local_tmp_path).with_small_counts()
    generate_dataset("training", settings, local_tmp_path)
    generate_dataset("project", settings, local_tmp_path)
    return local_tmp_path / "data"


def test_training_and_project_have_distinct_mining_patterns(local_tmp_path):
    root = _generate_all(local_tmp_path)
    training_manifest = json.loads((root / "training" / "metadata" / "manifest.json").read_text(encoding="utf-8"))
    project_manifest = json.loads((root / "project" / "metadata" / "manifest.json").read_text(encoding="utf-8"))

    assert training_manifest["mining_context"] is True
    assert project_manifest["mining_context"] is True
    assert training_manifest["mining_pattern"] != project_manifest["mining_pattern"]
    assert "Chancado" in training_manifest["mining_pattern"]
    assert "relaves" in project_manifest["mining_pattern"].lower()


def test_facts_contain_mining_operational_signals(local_tmp_path):
    root = _generate_all(local_tmp_path) / "training"
    maintenance = pd.read_csv(root / "clean" / "Fact_Mantenimiento.csv")
    incidents = pd.read_csv(root / "clean" / "Fact_Incidentes.csv")
    energy = pd.read_csv(root / "clean" / "Fact_Energia.csv")
    productivity = pd.read_csv(root / "clean" / "Fact_Productividad.csv")
    areas = pd.read_csv(root / "clean" / "Dim_Area.csv")

    assert maintenance["FailureMode"].str.contains("chancador|correa|pulpa|PLC|vibración", case=False, regex=True).any()
    assert incidents["IncidentType"].str.contains("HSE|geotécnico|correa|control crítico", case=False, regex=True).any()
    assert set(energy["Shift"]).issubset({"Día", "Tarde", "Noche"})
    assert set(productivity["Shift"]).issubset({"Día", "Tarde", "Noche"})
    assert set(energy["AreaID"]).intersection(set(areas.loc[areas["AreaType"].isin(["Mina", "Planta"]), "AreaID"]))


def test_raw_keeps_controlled_quality_issues_and_clean_is_standardized(local_tmp_path):
    root = _generate_all(local_tmp_path) / "training"
    raw_priority = pd.read_csv(root / "raw" / "Dim_Prioridad.csv")
    raw_service = pd.read_csv(root / "raw" / "Dim_Servicio.csv")
    clean_status = pd.read_csv(root / "clean" / "Dim_Estado.csv")

    assert {"CRITICAL", "HIGH"}.intersection(set(raw_priority["PriorityName"]))
    assert raw_service["ServiceName"].str.contains("Mant.|Insp.|Disp.", regex=True).any()
    assert (root / "raw" / "Fact_Energia_Wide.csv").exists()
    assert set(clean_status["StatusName"]) == {"Abierta", "En Proceso", "Vencida", "Cerrada", "Cancelada"}
