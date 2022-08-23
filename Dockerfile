FROM python:3.10-alpine3.16

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.1.15

RUN apk add --no-cache --virtual build-deps curl gcc musl-dev libffi-dev && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apk del build-deps
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /usr/src/app/
COPY sureflap_api ./sureflap_api
COPY poetry.lock pyproject.toml README.md ./

RUN poetry config virtualenvs.create false &&\
    poetry install --no-interaction --no-ansi --no-dev

ENTRYPOINT ["python", "sureflap_api/main.py"]