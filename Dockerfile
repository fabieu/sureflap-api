FROM python:3.10-alpine

COPY Pipfile.lock /app/
COPY sureflap /app/

WORKDIR /app/

RUN pip3 install pipenv && \
    pipenv install --ignore-pipfile

ENTRYPOINT [ "pipenv", "run", "--", "python", "server.py"]