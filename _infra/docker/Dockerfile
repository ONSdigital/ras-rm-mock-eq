# Dockerfile specifically for kubernetes
FROM python:3.12-slim

RUN apt update && apt install -y build-essential curl gunicorn
RUN pip install uv

WORKDIR /app

COPY . /app
RUN uv install --deploy --system

EXPOSE 8082
CMD ["gunicorn", "-c", "gunicorn.py", "mock_eq:app"]
