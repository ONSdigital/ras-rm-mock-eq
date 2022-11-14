.PHONY: build test start lint

build:
	pipenv install --dev

test:
	echo test

start:
	pipenv run python3 run.py

lint:
	pipenv check -i 51499
	pipenv run black --line-length 120 .
	pipenv run flake8
