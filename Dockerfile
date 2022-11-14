FROM python:3.11-slim

RUN apt update && apt install -y build-essential curl
RUN pip install pipenv

WORKDIR /app
EXPOSE 8086

COPY . /app
RUN pipenv install --deploy --system

CMD ["python", "run.py"]
