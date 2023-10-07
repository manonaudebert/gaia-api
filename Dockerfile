#!/bin/bash
FROM python:3.10.7-slim

RUN apt-get -y update && \
    apt-get -y install build-essential postgresql libpq-dev curl

RUN mkdir gaia-api

WORKDIR /gaia-api

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN curl -sSL https://install.python-poetry.org | python3

ENV PATH="/root/.local/bin:$PATH"

ENV PATH="/gaia-api/.venv/bin:${PATH}"

COPY poetry.lock poetry.toml pyproject.toml ./

RUN poetry install --no-dev

EXPOSE 8080

COPY . .
