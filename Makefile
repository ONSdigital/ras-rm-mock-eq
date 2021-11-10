.PHONY: build test start

build:
	pipenv install --dev

<<<<<<< HEAD

test:
=======
lint:
	pipenv run flake8 --exclude=./scripts
	pipenv run isort .
	pipenv run black --line-length 120 .

lint-check:
	pipenv run flake8 --exclude=./scripts
	pipenv run isort . --check-only
	pipenv run black --line-length 120 --check .

test: lint-check
	APP_SETTINGS=TestingConfig pipenv run pytest test --cov ras_party --cov-report term-missing
>>>>>>> 0464596cf7b2f68a728e4f25387475c54b334c7f

start:
	pipenv run python3 run.py
