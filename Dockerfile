FROM python:3.11.4

RUN mkdir /clinic

WORKDIR /clinic

COPY poetry.lock .
COPY pyproject.toml .

COPY . .