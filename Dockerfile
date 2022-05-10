FROM python:3.10-alpine3.15

COPY sureflap_api /app/
COPY poetry.lock pyproject.toml /app/

WORKDIR /app/

RUN apk add --no-cache --virtual build-deps gcc musl-dev libffi-dev && \
    pip3 install 'poetry>=1.1.0,<1.2.0' && \
    apk del build-deps

RUN poetry install --no-dev

ENTRYPOINT [ "poetry", "run", "--", "python", "main.py"]