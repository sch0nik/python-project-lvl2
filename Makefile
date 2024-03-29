install:
	poetry install

lint:
	poetry run flake8 gendiff
build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

run:
	poetry run gen-diff -f stylish tests/fixtures/file1.json tests/fixtures/file2.json

test:
	poetry run pytest -vv gendiff tests

coverage:
	poetry run coverage run -m pytest
	poetry run coverage xml
	poetry run coverage html

start: build publish package-install

.PHONY: install lint runh build publsh package-install start runf
