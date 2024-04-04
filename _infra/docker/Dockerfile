# Dockerfile specifically for kubernetes
FROM python:3.11-slim

RUN apt update && apt install -y build-essential curl gunicorn
RUN pip install pipenv

WORKDIR /app

COPY . /app
RUN pipenv install --deploy --system

EXPOSE 8086
CMD ["gunicorn", "-c", "0.0.0.0:8080", "gunicorn.py", "mock_eq:app"]
