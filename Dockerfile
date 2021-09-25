FROM python:3.9-slim

COPY Pipfile.lock /app/
COPY sureflap /app/

WORKDIR /app/

RUN pip3 install pipenv
RUN pipenv install --ignore-pipfile

ENTRYPOINT [ "pipenv", "run", "--", "python", "server.py"]