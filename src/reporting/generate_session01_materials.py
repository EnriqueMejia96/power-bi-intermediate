from __future__ import annotations

from src.config.settings import load_settings
from src.utils.io import write_text


def main() -> None:
    settings = load_settings()
    root = settings.repo_root
    manifest = root / "artifacts" / "manifests" / "session01_materials_manifest.md"
    report = root / "reports" / "session_01" / "materials_checklist.md"
    body = """# Manifest de materiales Sesión 01

    - Guía de laboratorio.
    - Plantillas de blueprint, KPIs, audiencia y wireframe.
    - Prompt library y checklist de IA.
    - Guías manuales de Power BI Desktop.
    """
    write_text(body, manifest, root)
    write_text(body.replace("Manifest", "Checklist"), report, root)
    print(manifest)


if __name__ == "__main__":
    main()
