from __future__ import annotations

from pathlib import Path
import importlib.util
import sys

from src.config.settings import load_settings

REQUIRED_DIRS = [
    "ai_context", "docs", "session_01/lab", "data/training/raw", "data/training/clean",
    "data/project/raw", "data/project/clean", "src/data", "scripts/python", "powerbi/manual_steps",
    "ai_tools/prompt_library", "tests",
]
REQUIRED_FILES = ["README.md", "AGENTS.md", ".env.example", "Makefile", "requirements.txt"]
REQUIRED_MODULES = ["pandas", "numpy", "openpyxl", "yaml", "dotenv", "typer", "rich", "pytest"]


def check_environment(structure_only: bool = False, root: Path | None = None) -> list[str]:
    settings = load_settings(root)
    root = (root or settings.repo_root).resolve()
    errors: list[str] = []
    for directory in REQUIRED_DIRS:
        if not (root / directory).is_dir():
            errors.append(f"Falta carpeta {directory}")
    for filename in REQUIRED_FILES:
        if not (root / filename).is_file():
            errors.append(f"Falta archivo {filename}")
    if not structure_only:
        for module in REQUIRED_MODULES:
            if importlib.util.find_spec(module) is None:
                errors.append(f"Dependencia no disponible: {module}")
        if settings.powerbi_desktop_required:
            errors.append("POWERBI_DESKTOP_REQUIRED debe ser false para este repositorio.")
        if settings.create_pbix:
            errors.append("CREATE_PBIX debe ser false.")
        if settings.ai_api_calls_enabled or settings.allow_external_ai_calls:
            errors.append("Las llamadas externas de IA deben estar deshabilitadas.")
    return errors


def main(structure_only: bool = False) -> int:
    errors = check_environment(structure_only)
    if errors:
        print("\n".join(errors))
        return 1
    print("Entorno local verificado. No se requiere Power BI Desktop para las comprobaciones.")
    return 0


if __name__ == "__main__":
    sys.exit(main("--structure-only" in sys.argv))
