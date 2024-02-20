FROM python:3.11-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update && \
    apk add --no-cache python3-dev \
    gcc \
    musl-dev \
    libpq-dev \
    nmap

ADD requirements.txt /app

RUN apk add libffi-dev

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
