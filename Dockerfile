FROM python:3.10-alpine3.15

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --virtual build-deps curl gcc musl-dev libffi-dev && \
    curl -sSL https://install.python-poetry.org | python3 - --version 1.1.13 && \
    apk del build-deps
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /usr/src/app/
COPY sureflap_api ./sureflap_api
COPY poetry.lock pyproject.toml README.md ./

RUN poetry config virtualenvs.create false &&\
    poetry install --no-interaction --no-ansi --no-dev

ENTRYPOINT ["python", "sureflap_api/main.py"]