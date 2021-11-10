.PHONY: build test start

build:
	pipenv install --dev

# lint:
# 	pipenv run flake8 --exclude=./scripts
# 	pipenv run isort .
# 	pipenv run black --line-length 120 .
#
# lint-check:
# 	pipenv run flake8 --exclude=./scripts
# 	pipenv run isort . --check-only
# 	pipenv run black --line-length 120 --check .

test:

start:
	pipenv run python3 run.py
