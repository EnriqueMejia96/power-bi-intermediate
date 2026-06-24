PYTHON ?= python

.PHONY: help setup check-env lint-structure data data-training data-project data-dictionary validate-data profile-data session01-materials report test clean-local reset-data

help:
	@$(PYTHON) -c "print('Comandos: setup, check-env, lint-structure, data, data-training, data-project, data-dictionary, validate-data, profile-data, session01-materials, report, test, clean-local, reset-data')"

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
