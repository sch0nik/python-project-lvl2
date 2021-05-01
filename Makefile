install:
	poetry install

lint:
	poetry run flake8 gendiff

runh:
	poetry run python3 -m gendiff.scripts.gendiff --help

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

runf:
	poetry run python3 -m gendiff.scripts.gendiff file1.json file2.json

start: build publish package-install

.PHONY: install lint runh build publsh package-install start runf
