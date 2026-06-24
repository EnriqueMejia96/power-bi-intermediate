from __future__ import annotations

import numpy as np
import pandas as pd


def inject_raw_issues(
    tables: dict[str, pd.DataFrame],
    dataset_kind: str,
    rng: np.random.Generator,
) -> tuple[dict[str, pd.DataFrame], dict[str, pd.DataFrame], list[str]]:
    raw = {name: df.copy() for name, df in tables.items()}
    issues: list[str] = []
    for name, df in raw.items():
        df["_SourceFile"] = f"{dataset_kind}_{name.lower()}_export.csv"
        df["_ExportedAt"] = "2026-06-23T00:00:00"
        df["_LegacyRowNumber"] = range(1, len(df) + 1)

    if "Dim_Area" in raw:
        df = raw["Dim_Area"]
        if len(df) >= 3:
            df.loc[df.index[0], "AreaName"] = str(df.loc[df.index[0], "AreaName"]).upper()
            df.loc[df.index[1], "AreaName"] = str(df.loc[df.index[1], "AreaName"]) + " "
            df.loc[df.index[2], "AreaName"] = str(df.loc[df.index[2], "AreaName"]).replace("á", "a")
            issues.append("Nombres de área inconsistentes en Dim_Area.")

    if "Dim_Prioridad" in raw:
        df = raw["Dim_Prioridad"]
        replacements = ["HIGH", "High", "Alta", "medium"]
        for idx, value in zip(df.index[: len(replacements)], replacements):
            df.loc[idx, "PriorityName"] = value
        issues.append("Prioridades mezclan español, inglés y mayúsculas.")

    if "Dim_Estado" in raw:
        df = raw["Dim_Estado"]
        if len(df) >= 4:
            df.loc[df.index[-2], "StatusName"] = "Closed"
            df.loc[df.index[-1], "StatusName"] = "Done"
            issues.append("Estados inconsistentes: Closed, Done y Cerrado.")

    if "Dim_Proyecto" in raw:
        df = raw["Dim_Proyecto"]
        sample_idx = df.sample(min(5, len(df)), random_state=11).index
        df.loc[sample_idx, "PlannedStartDate"] = pd.to_datetime(df.loc[sample_idx, "PlannedStartDate"]).dt.strftime("%d/%m/%Y")
        issues.append("Fechas de proyecto exportadas como texto en formatos mixtos.")

    if "Fact_OrdenesTrabajo" in raw:
        df = raw["Fact_OrdenesTrabajo"]
        duplicate_count = max(3, min(25, len(df) // 40))
        duplicates = df.head(duplicate_count).copy()
        duplicates["_SourceFile"] = f"{dataset_kind}_workorders_duplicate_export.csv"
        raw["Fact_OrdenesTrabajo"] = pd.concat([df, duplicates], ignore_index=True)
        issues.append("Duplicados controlados en órdenes de trabajo.")
        open_idx = raw["Fact_OrdenesTrabajo"].sample(min(20, len(raw["Fact_OrdenesTrabajo"])), random_state=12).index
        raw["Fact_OrdenesTrabajo"].loc[open_idx, "ClosedDateKey"] = pd.NA
        issues.append("Fechas de cierre nulas en órdenes abiertas.")

    if "Fact_Costos" in raw:
        df = raw["Fact_Costos"]
        outlier_count = max(2, min(20, len(df) // 60))
        idx = df.sample(outlier_count, random_state=13).index
        df.loc[idx, "ActualAmount"] = (pd.to_numeric(df.loc[idx, "ActualAmount"]) * rng.uniform(3.0, 5.5, len(idx))).round(2)
        df["UnusedERPColumn"] = "legacy-cost-center"
        issues.append("Costos outliers y columna innecesaria exportada desde ERP.")

    if "Fact_Mantenimiento" in raw and "Dim_Equipo" in raw:
        maint = raw["Fact_Mantenimiento"]
        eq = raw["Dim_Equipo"][["EquipmentID", "EquipmentName"]].drop_duplicates()
        maint = maint.merge(eq, on="EquipmentID", how="left")
        maint.rename(columns={"EquipmentName": "EquipmentName_Source"}, inplace=True)
        sample_idx = maint.sample(min(15, len(maint)), random_state=14).index
        maint.loc[sample_idx, "EquipmentID"] = pd.NA
        raw["Fact_Mantenimiento"] = maint
        issues.append("Algunos mantenimientos referencian equipo por nombre y no por ID.")

    extras: dict[str, pd.DataFrame] = {}
    if "Fact_Energia" in raw:
        energy = raw["Fact_Energia"].copy()
        wide = energy.pivot_table(
            index=["DateKey", "AreaID", "LocationID"],
            columns="Shift",
            values="kWh",
            aggfunc="sum",
            fill_value=0,
        ).reset_index()
        wide.columns = [str(col) for col in wide.columns]
        extras["Fact_Energia_Wide"] = wide
        issues.append("Archivo adicional de energía en formato ancho por turno.")

    return raw, extras, issues
