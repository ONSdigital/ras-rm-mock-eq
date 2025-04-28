.PHONY: build test start lint

build:
	pipenv install --dev

test:
	echo test

start:
	pipenv run python3 run.py

#remove -i 70612 once jinja2 is upgrade beyond v3.1.4
lint:
	pipenv run black --line-length 120 .
	pipenv run flake8
