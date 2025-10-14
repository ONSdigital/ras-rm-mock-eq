.PHONY: build test start lint

build:
	uv sync --locked --all-extras --dev

test:
	echo test

start:
	uv run --locked python3 run.py

lint:
	uv run --locked black --line-length 120 .
	uv run --locked flake8
