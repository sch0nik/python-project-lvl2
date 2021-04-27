install:
	poetry install

lint:
	poetry run flake8 gendiff

runh:
	poetry run python3 -m gendiff.scripts.gendiff --help

build: check
	poetry build

.PHONY: install test lint selfcheck check build