FROM python:3.12.1-alpine3.19

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.7.1

RUN apk add --no-cache --virtual build-deps curl gcc musl-dev libffi-dev && \
    apk del build-deps && \
    pip install poetry==$POETRY_VERSION
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /usr/src/app/
COPY sureflap_api ./sureflap_api
COPY poetry.lock pyproject.toml README.md ./

RUN poetry config virtualenvs.create false &&\
    poetry install --no-interaction --no-ansi --only main

ENTRYPOINT ["python", "sureflap_api/main.py"]