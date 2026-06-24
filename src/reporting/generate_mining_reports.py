from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from src.config.settings import load_settings
from src.data.schema import TABLE_COLUMNS
from src.utils.io import read_csv, write_text


MINING_TERMS = [
    "Mina",
    "Chancado",
    "Correas",
    "Molienda",
    "Flotación",
    "Relaves",
    "CAEX",
    "SCADA",
    "Dispatch",
    "HSE",
    "Energía",
    "correa",
    "chancador",
    "pulpa",
    "PLC",
    "vibración",
    "bomba",
    "geotécnico",
    "control crítico",
]


def _root(root: Path | None = None) -> Path:
    settings = load_settings(root)
    return (root or settings.repo_root).resolve()


def _table(root: Path, dataset_kind: str, table_name: str) -> pd.DataFrame:
    path = root / "data" / dataset_kind / "clean" / f"{table_name}.csv"
    if not path.exists():
        return pd.DataFrame(columns=TABLE_COLUMNS.get(table_name, []))
    return read_csv(path)


def _contains_terms(values: pd.Series, terms: list[str]) -> list[str]:
    text = " ".join(values.dropna().astype(str).tolist()).lower()
    return [term for term in terms if term.lower() in text]


def generate_gap_assessment(root: Path | None = None) -> Path:
    repo = _root(root)
    output = repo / "reports" / "dataset_profile" / "MINING_GAP_ASSESSMENT.md"
    write_text(
        """# Mining gap assessment

## Estado antes de la mejora
- El repositorio ya tenia una arquitectura didactica clara para Power BI: Dataset A para entrenamiento, Dataset B para proyecto final, datos raw/clean, validaciones, diccionario y materiales de sesion.
- El enfoque era Tech&Eng industrial, con algunas referencias a mineria, mantenimiento, energia y seguridad.
- El schema ya estaba validado por tests y debia preservarse.

## Gaps detectados
- Las dimensiones necesitaban vocabulario minero explicito: mina, planta concentradora, chancado, molienda, flotacion, relaves, HSE y OT.
- Los hechos necesitaban patrones operacionales diferenciados para backlog, SLA, downtime, energia, productividad, incidentes, costos y proyectos.
- El diccionario describia campos de forma demasiado generica y no explicaba como interpretar metricas como ActualOutput, OutputUnits, DelayDays o RiskScore.
- Los materiales del Modulo 1 necesitaban un caso minero mas concreto para blueprint, preguntas, KPIs, audiencia y wireframes.
- Faltaban tests de cobertura minera y reportes de perfil minero.

## Cambios aplicados sin romper schema
- Se mantienen las mismas tablas y columnas principales de Dataset A y Dataset B.
- Dataset A conserva uso de entrenamiento y Dataset B conserva uso de proyecto final.
- Raw mantiene problemas controlados para Power Query; clean queda listo para modelo estrella.
- Se agregan valores mineros, documentacion, reportes, Make targets y tests sin crear PBIX ni llamar servicios externos.

## Cambios opcionales futuros
- Agregar columnas opcionales como OutputUnit, CrewName o MaterialType solo si un modulo posterior lo requiere y actualiza schema, tests y diccionario.
- Implementar medidas DAX en Modulo 4 usando el backlog de KPIs mineros.
- Crear paginas Power BI manualmente en Modulos 5-6 sin versionar archivos PBIX.
""",
        output,
        repo,
    )
    return output


def generate_domain_coverage_report(root: Path | None = None) -> Path:
    repo = _root(root)
    lines = ["# Mining domain coverage report", ""]
    for dataset_kind in ["training", "project"]:
        lines.append(f"## {dataset_kind}")
        for table, column in [
            ("Dim_Area", "AreaName"),
            ("Dim_Equipo", "EquipmentType"),
            ("Dim_Servicio", "ServiceName"),
            ("Dim_Ubicacion", "LocationName"),
            ("Dim_TipoTrabajo", "WorkTypeName"),
            ("Dim_Proyecto", "ProjectName"),
            ("Fact_Mantenimiento", "FailureMode"),
            ("Fact_Incidentes", "IncidentType"),
            ("Fact_Energia", "Shift"),
            ("Fact_Productividad", "Shift"),
        ]:
            df = _table(repo, dataset_kind, table)
            if df.empty or column not in df:
                lines.append(f"- {table}.{column}: archivo no disponible.")
                continue
            if column == "Shift":
                sample = ", ".join(df[column].dropna().astype(str).drop_duplicates().head(6).tolist())
                lines.append(f"- {table}.{column}: turnos operacionales cubiertos; ejemplos={sample}")
                continue
            found = _contains_terms(df[column], MINING_TERMS)
            sample = ", ".join(df[column].dropna().astype(str).drop_duplicates().head(6).tolist())
            lines.append(f"- {table}.{column}: términos detectados={', '.join(found) if found else 'revisar'}; ejemplos={sample}")
        lines.append("")

    lines.extend(
        [
            "## Lectura esperada",
            "- Dataset A debe sentirse como operación minera de entrenamiento con foco en chancado, correas, taller mina, molienda y energía.",
            "- Dataset B debe conservar el mismo schema, pero mover los problemas hacia dispatch, relaves, molienda, flota mina y OT.",
            "- Ningún nombre corresponde a faenas, empresas o personas reales.",
        ]
    )
    output = repo / "reports" / "dataset_profile" / "MINING_DOMAIN_COVERAGE_REPORT.md"
    write_text("\n".join(lines), output, repo)
    return output


def generate_data_quality_report(root: Path | None = None) -> Path:
    repo = _root(root)
    lines = ["# Mining data quality report", ""]
    for dataset_kind in ["training", "project"]:
        path = repo / "data" / dataset_kind / "metadata" / "data_quality_issues.md"
        issues = path.read_text(encoding="utf-8").strip() if path.exists() else "No existe metadata de calidad."
        lines.append(f"## {dataset_kind}")
        lines.append(issues)
        lines.append("")
    lines.extend(
        [
            "## Raw vs clean",
            "- `raw` conserva fechas como texto, estados mixtos, prioridades inconsistentes, duplicados, nulos, outliers, columnas extra y energia en formato ancho.",
            "- `clean` mantiene columnas estables, llaves consistentes y valores estandarizados para modelo estrella.",
            "- Estos problemas estan diseñados para el Modulo 2; no deben eliminarse sin actualizar materiales y tests.",
        ]
    )
    output = repo / "reports" / "dataset_profile" / "MINING_DATA_QUALITY_REPORT.md"
    write_text("\n".join(lines), output, repo)
    return output


def generate_root_cause_patterns(root: Path | None = None) -> Path:
    repo = _root(root)
    output = repo / "reports" / "dataset_profile" / "MINING_ROOT_CAUSE_PATTERNS_INSTRUCTOR.md"
    write_text(
        """# Mining root cause patterns - instructor-only

**INSTRUCTOR-ONLY. No copiar este archivo a carpetas student ni usarlo como handout.**

## Dataset A - entrenamiento
- Chancado Primario y Transporte por Correas concentran brechas de SLA, órdenes críticas y eventos de mantenimiento.
- Molienda muestra consumo energético anormal y brecha entre output planificado y real.
- Taller Mina concentra backlog y acciones HSE abiertas.
- Costos altos aparecen en correas, molienda y componentes de flota CAEX.

## Dataset B - proyecto final
- Dispatch, Relaves, Molienda y Automatización OT concentran problemas distintos.
- Relaves y planta tienen mayor riesgo HSE y acciones vencidas.
- Molienda y relaves concentran sobrecostos y downtime.
- La causa raíz no debe revelarse de forma directa; se espera que el estudiante la infiera con KPIs, segmentación y narrativa.

## Tablas donde observar patrones
- `Fact_OrdenesTrabajo`: backlog, estado, criticidad, retrabajo, sistema fuente.
- `Fact_SLA`: cumplimiento, breach hours, prioridad y servicio.
- `Fact_Mantenimiento`: failure mode, downtime, repair hours y costo.
- `Fact_Energia`: kWh, output units, turno y equipo.
- `Fact_Productividad`: plan vs real y horas productivas.
- `Fact_Incidentes`: severidad, estado de acción correctiva y días abiertos.
- `Fact_Costos`: categoría, presupuesto, real y comprometido.
- `Fact_Proyectos`: avance, costo, riesgo y retraso.

## Guía didáctica
- Hacer preguntas, no entregar respuestas: "¿qué cambia cuando filtras por turno?", "¿el problema es costo, downtime o SLA?", "¿la señal aparece en más de una tabla?".
- Pedir validaciones humanas: confirmar definiciones, revisar outliers, separar correlación de causalidad y explicar supuestos.
""",
        output,
        repo,
    )
    return output


def generate_session01_readiness(root: Path | None = None) -> Path:
    repo = _root(root)
    required = [
        "session_01/README_SESSION_01.md",
        "session_01/lab/LAB_GUIDE.md",
        "session_01/lab/LAB_STEPS.md",
        "session_01/student/STUDENT_HANDOUT.md",
        "session_01/templates/BI_SOLUTION_BLUEPRINT_TEMPLATE.md",
        "session_01/prompts/AI_PROMPT_LIBRARY_SESSION_01.md",
        "data/training/clean/Dim_Area.csv",
        "data/training/dictionary/data_dictionary.md",
    ]
    lines = ["# Mining session 01 readiness", ""]
    for item in required:
        path = repo / item
        status = "OK" if path.exists() else "FALTA"
        mining_hint = ""
        if path.exists() and path.suffix == ".md":
            text = path.read_text(encoding="utf-8").lower()
            mining_hint = " mineria=OK" if "min" in text and ("minería" in text or "minero" in text or "minera" in text) else " mineria=REVISAR"
        lines.append(f"- {status}: `{item}`{mining_hint}")
    lines.extend(
        [
            "",
            "## Actividad final esperada",
            "Los estudiantes diseñan un blueprint BI para una operación minera en riesgo por bajo rendimiento en chancado, backlog de mantenimiento, consumo energético anormal y acciones HSE pendientes.",
        ]
    )
    output = repo / "reports" / "session_01" / "MINING_SESSION_01_READINESS.md"
    write_text("\n".join(lines), output, repo)
    return output


def generate_all(root: Path | None = None) -> list[Path]:
    return [
        generate_gap_assessment(root),
        generate_domain_coverage_report(root),
        generate_data_quality_report(root),
        generate_root_cause_patterns(root),
        generate_session01_readiness(root),
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", choices=["all", "gap", "coverage", "quality", "root-cause", "session01"], default="all")
    args = parser.parse_args()
    if args.report == "all":
        outputs = generate_all()
    elif args.report == "gap":
        outputs = [generate_gap_assessment()]
    elif args.report == "coverage":
        outputs = [generate_domain_coverage_report()]
    elif args.report == "quality":
        outputs = [generate_data_quality_report()]
    elif args.report == "root-cause":
        outputs = [generate_root_cause_patterns()]
    else:
        outputs = [generate_session01_readiness()]
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
