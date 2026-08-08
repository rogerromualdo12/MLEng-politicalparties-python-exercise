SHELL := /bin/bash
PYTHON ?= python3
VENV_DIR := .venv
ACTIVATE := source $(VENV_DIR)/bin/activate
export PYTHONPATH := src

.PHONY: install venv test generate-sample generate-large demo-etl lint-check clean help

help:
	@echo "Comandos del taller:"
	@echo "  make install           Instala dependencias en .venv"
	@echo "  make test              Ejecuta pruebas"
	@echo "  make generate-sample   Genera dataset sintético pequeño"
	@echo "  make generate-large    Genera dataset sintético grande"
	@echo "  make demo-etl          Corre el pipeline ETL de demo"
	@echo "  make clean             Limpia artefactos"

install: venv

venv: $(VENV_DIR)/bin/activate

$(VENV_DIR)/bin/activate: requirements.txt
	test -d $(VENV_DIR) || $(PYTHON) -m venv $(VENV_DIR)
	$(ACTIVATE) && pip install --upgrade pip && pip install -r requirements.txt
	touch $(VENV_DIR)/bin/activate

test:
	$(ACTIVATE) && PYTHONPATH=src pytest -q tests

generate-sample:
	$(ACTIVATE) && PYTHONPATH=src python scripts/generate_data.py --rows 5000 --output data/generated/eventos_sample.csv

generate-large:
	$(ACTIVATE) && PYTHONPATH=src python scripts/generate_data.py --rows 500000 --output data/generated/eventos_large.csv

demo-etl:
	$(ACTIVATE) && PYTHONPATH=src python scripts/run_etl_demo.py

clean:
	rm -rf $(VENV_DIR) .pytest_cache
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf data/generated/* data/processed/* data/warehouse
	touch data/generated/.gitkeep data/processed/.gitkeep