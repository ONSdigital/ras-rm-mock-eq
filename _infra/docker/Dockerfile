# Dockerfile specifically for kubernetes
FROM python:3.12-slim

RUN pip install uv

WORKDIR /app

COPY . /app
RUN uv sync --frozen --no-dev

EXPOSE 8086
CMD ["uv", "run", "--no-dev", "--frozen", "gunicorn", "-c", "gunicorn.py", "mock_eq:app"]
