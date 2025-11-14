# Dockerfile specifically for kubernetes
FROM python:3.12-slim

#COPY ../../Cisco_Umbrella_Root_CA.pem /usr/local/share/ca-certificates/Cisco_Umbrella_Root_CA.pem
#RUN apt-get update && apt-get install -y ca-certificates
#RUN update-ca-certificates
#RUN apt update && apt install -y build-essential curl gunicorn
#ENV PIP_CERT=/usr/local/share/ca-certificates/Cisco_Umbrella_Root_CA.pem
#ENV SSL_CERT_FILE=/usr/local/share/ca-certificates/Cisco_Umbrella_Root_CA.pem

RUN pip install uv

WORKDIR /app

COPY . /app
RUN uv sync --frozen --no-dev

EXPOSE 8080
CMD ["uv", "run", "--no-dev", "--frozen", "gunicorn", "-c", "gunicorn.py", "mock_eq:app"]
