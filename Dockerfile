FROM python:3.10-slim

COPY sureflap_api /app/
COPY poetry.lock pyproject.toml /app/

WORKDIR /app/

RUN pip3 install poetry && \
    poetry install --no-dev

ENTRYPOINT [ "poetry", "run", "--", "python", "main.py"]