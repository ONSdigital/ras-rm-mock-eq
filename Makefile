.PHONY: build test start lint

build:
	uv sync --dev

test:
	echo test

start:
	uv run python3 run.py

lint:
	uv run black --line-length 120 .
	uv run flake8
