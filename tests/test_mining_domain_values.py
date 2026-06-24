from __future__ import annotations

import pandas as pd

from src.config.settings import load_settings
from src.data.generate_techeng_dataset import generate_dataset


def _generate_training(local_tmp_path):
    settings = load_settings(local_tmp_path).with_small_counts()
    generate_dataset("training", settings, local_tmp_path)
    return local_tmp_path / "data" / "training"


def test_mining_dimensions_have_expected_domain_values(local_tmp_path):
    root = _generate_training(local_tmp_path)
    areas = pd.read_csv(root / "clean" / "Dim_Area.csv")
    equipment = pd.read_csv(root / "clean" / "Dim_Equipo.csv")
    services = pd.read_csv(root / "clean" / "Dim_Servicio.csv")
    locations = pd.read_csv(root / "clean" / "Dim_Ubicacion.csv")

    assert {"Chancado Primario", "Molienda", "Espesamiento y Relaves", "Automatización OT"}.issubset(set(areas["AreaName"]))
    assert {"Camión CAEX", "Correa transportadora", "Molino SAG"}.issubset(set(equipment["EquipmentType"]))
    assert {"Mantenimiento Planta", "Soporte Dispatch", "Gestión de Relaves", "Soporte SCADA"}.issubset(set(services["ServiceName"]))
    assert {"Pit Norte", "Faja CV-101", "Molino SAG", "Relavera Principal"}.issubset(set(locations["LocationName"]))


def test_no_known_real_mine_names_are_used(local_tmp_path):
    root = _generate_training(local_tmp_path)
    joined = "\n".join(path.read_text(encoding="utf-8") for path in (root / "clean").glob("*.csv"))
    forbidden = ["Chuquicamata", "Escondida", "Collahuasi", "Antamina", "Quellaveco", "Cerro Verde"]
    assert not any(name.lower() in joined.lower() for name in forbidden)
