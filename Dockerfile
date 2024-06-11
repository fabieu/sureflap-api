FROM python:3.12.1-alpine3.19

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3

RUN apk add --no-cache --virtual build-deps curl gcc musl-dev libffi-dev && \
    pip install --upgrade pip poetry==$POETRY_VERSION && \
    apk del build-deps

ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /usr/src/app/
COPY sureflap_api ./sureflap_api
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false &&\
    poetry install --no-interaction --no-ansi --only main

EXPOSE 3001

ENTRYPOINT ["python", "sureflap_api/main.py"]