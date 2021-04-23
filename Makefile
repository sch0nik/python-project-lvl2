install:
	poetry install

lint:
	poetry run flake8 gendiff

build: check
	poetry build

.PHONY: install test lint selfcheck check build