# Resumen de Fuente

## Propósito
Registrar qué material fuente fue inspeccionado y cómo se usó para construir el repositorio del Módulo 1.

## PDF inspeccionado
El archivo `docs/1_Arquitectura_analitica_recap_powerbi.pdf` fue localizado y preservado en su ubicación original. No se movió ni renombró. La extracción textual directa no fue posible con el tooling local disponible: no estaban instalados `pypdf`, `PyPDF2`, `pdfplumber` ni `pdftotext`.

## Qué se pudo extraer
Se inspeccionó la carpeta `docs/` y se leyeron documentos Word complementarios existentes junto al PDF. Esos documentos describen la narrativa del módulo, notas del instructor, briefing, FAQ, glosario, casos de uso y matriz de decisión para IA.

## Qué no se pudo extraer
No se extrajo texto interno del PDF. Por tanto, este repositorio no afirma que ningún contenido específico provenga del PDF salvo su existencia, nombre y ubicación.

## Temas detectados
- Arquitectura analítica en Power BI para entornos Tech&Eng.
- Transición de reportes aislados a ecosistemas de decisión.
- Power Query, modelo semántico, DAX y visualización como capas separadas.
- Preguntas de negocio medibles y KPIs alineados a decisiones.
- Uso de IA como copiloto de diseño analítico, con validación humana.
- Riesgos de privacidad, gobernanza y deuda técnica.

## Cómo se usó el material fuente
El contenido disponible se usó para alinear README, guías de laboratorio, plantillas, prompts, documentación de IA responsable y el enfoque de dataset sintético integrado.

## Limitaciones
La lectura del PDF debe repetirse si se instala una herramienta de extracción PDF. Cualquier ajuste derivado del PDF debe documentarse aquí, sin sobrescribir la distinción entre material inspeccionado y material inferido.
