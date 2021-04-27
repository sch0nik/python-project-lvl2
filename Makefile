install:
	poetry install

lint:
	poetry run flake8 gendiff

runh:
	poetry run python3 -m gendiff.scripts.gendiff --help

runf:
	poetry run python3 -m gendiff.scripts.gendiff file1.json file2.json

build: check
	poetry build

.PHONY: install test lint selfcheck check build