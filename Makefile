.PHONY: build test start

build:
	pipenv install --dev


test:

start:
	pipenv run python3 run.py
