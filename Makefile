PYTHON ?= python

.PHONY: help setup check-env lint-structure data data-training data-project data-dictionary validate-data profile-data mining-gap mining-upgrade data-mining validate-mining profile-mining mining-report session01-materials report test clean-local reset-data

help:
	@$(PYTHON) -c "print('Comandos: setup, check-env, lint-structure, data, data-training, data-project, data-dictionary, validate-data, profile-data, mining-gap, mining-upgrade, data-mining, validate-mining, profile-mining, mining-report, session01-materials, report, test, clean-local, reset-data')"

setup:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

check-env:
	$(PYTHON) scripts/python/check_env.py

lint-structure:
	$(PYTHON) scripts/python/check_env.py --structure-only

data:
	$(PYTHON) scripts/python/generate_data.py --dataset all

data-training:
	$(PYTHON) scripts/python/generate_data.py --dataset training

data-project:
	$(PYTHON) scripts/python/generate_data.py --dataset project

data-dictionary:
	$(PYTHON) scripts/python/generate_dictionary.py --dataset all

validate-data:
	$(PYTHON) scripts/python/validate_data.py --dataset all

profile-data:
	$(PYTHON) scripts/python/profile_data.py --dataset all

mining-gap:
	$(PYTHON) -m src.reporting.generate_mining_reports --report gap

mining-upgrade:
	$(PYTHON) scripts/python/check_env.py --structure-only
	$(PYTHON) -m py_compile src/data/generate_techeng_dataset.py src/data/data_quality_injector.py src/reporting/generate_data_dictionary.py src/reporting/generate_mining_reports.py

data-mining:
	$(PYTHON) scripts/python/generate_data.py --dataset all

validate-mining:
	$(PYTHON) -m pytest tests/test_mining_domain_values.py tests/test_mining_dataset_patterns.py tests/test_training_project_same_schema.py tests/test_mining_data_dictionary.py tests/test_mining_session01_materials.py

profile-mining:
	$(PYTHON) -m src.reporting.generate_mining_reports --report coverage

mining-report:
	$(PYTHON) -m src.reporting.generate_mining_reports --report all

session01-materials:
	$(PYTHON) -m src.reporting.generate_session01_materials

report:
	$(PYTHON) -m src.reporting.generate_dataset_report --dataset all

test:
	$(PYTHON) -m pytest

clean-local:
	$(PYTHON) -c "from pathlib import Path; import shutil; p=Path('artifacts/local/tmp'); shutil.rmtree(p, ignore_errors=True); p.mkdir(parents=True, exist_ok=True); print('Limpieza local segura completada')"

reset-data:
	$(PYTHON) scripts/python/generate_data.py --dataset all --require-overwrite
