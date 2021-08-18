FROM python:3.9-slim

# Initialize working directory
COPY . /build
WORKDIR /build

# Install python dependencies
RUN pip install pipenv --upgrade
RUN pipenv install --deploy --ignore-pipfile

EXPOSE 3001

CMD ["pipenv", "run", "python", "server.py"]