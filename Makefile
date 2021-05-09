install:
	poetry install

lint:
	poetry run flake8 gendiff

runh:
	poetry run gen-diff --help

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

runf:
	poetry run gen-diff tests/fixtures/file1_recurs.json tests/fixtures/file2_recurs.json

test:
	poetry run pytest -vv gendiff tests

start: build publish package-install

.PHONY: install lint runh build publsh package-install start runf
