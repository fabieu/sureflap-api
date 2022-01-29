<div align="center">
  <img width="256" heigth="256" src="https://github.com/fabieu/sureflap-api/blob/main/assets/logo.jpg" alt="logo">
</div>

![Docker Pulls](https://img.shields.io/docker/pulls/fabieu/sureflap-api) ![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/fabieu/sureflap-api) ![GitHub last commit](https://img.shields.io/github/last-commit/fabieu/sureflap-api) [![GitHub issues](https://img.shields.io/github/issues/fabieu/sureflap-api)](https://github.com/fabieu/sureflap-api/issues) [![GitHub license](https://img.shields.io/github/license/fabieu/sureflap-api)](https://github.com/fabieu/sureflap-api/blob/main/LICENSE)

# SureFlap API

SureFlap API is a standalone RESTful wrapper API for products from [Sure Petcare](https://www.surepetcare.com).

# Install

## Docker (recommended)

```bash
docker run -d -p 8080:3001 -e SUREFLAP_EMAIL={YOUR_SUREFLAP_EMAIL} -e SUREFLAP_PASSWORD={YOUR_SUREFLAP_EMAIL} fabieu/sureflap-api:latest
```

> For all available options take a look at the [Configuration](#configuration) section.

## Manual install

Clone this repository to your system and move into the sureflap project subfolder:

```bash
git clone https://github.com/fabieu/sureflap-api.git
```

```bash
cd ./sureflap-api/sureflap
```

This project utilizes **Pipenv**, a production-ready tool that aims to bring the best of all packaging worlds to the Python world. It harnesses Pipfile, pip, and virtualenv into one single command. You can read more about Pipenv [here](https://pipenv-fork.readthedocs.io/en/latest/).

Install pipenv via pip:

```bash
pip install --user pipenv
```

Installing required dependencies and move into the virtual environment created by Pipenv:

```bash
pipenv install
```

Set at least the required environment variables:

```bash
export SUREFLAP_EMAIL={YOUR_SUREFLAP_EMAIL}
export SUREFLAP_PASSWORD={YOUR_SUREFLAP_PASSWORD}
```

Start the integrated webserver with the following command:

```bash
pipenv run python server.py
```

> For all available options take a look at the [Configuration](#configuration) section.

# Configuration

The configuration is done via environment variables. The following options are available:

### `SUREFLAP_EMAIL` (required)

Email of your _Sure Petcare_ account. Make sure to use an account with control privileges if you want to use the full capabilities of this API. You can change the privileges on the official Sure Petcare website.

### `SUREFLAP_PASSWORD` (required)

Password of the in `SUREFLAP_EMAIL` specified _Sure Petcare_ account.

### `SUREFLAP_LOGLEVEL` (optional)

> Default: warning

The `SUREFLAP_LOGLEVEL` option controls the level of log output and can be changed to be more or less verbose, which might be useful when you are dealing with an unknown issue.

- `trace`: Show every detail, like all called internal functions.
- `debug`: Shows detailed debug information.
- `info`: Normal (usually) interesting events.
- `warning`: Exceptional occurrences that are not errors.
- `error`: Runtime errors that do not require immediate action.
- `fatal`: Something went terribly wrong. Add-on becomes unusable.

### `SUREFLAP_PORT` (optional)

> Default: 3001

The port for the ASGI server. This is the same as the port used for API requests. Please make sure that the specified port isn't used by another application.

### `SUREFLAP_CORS` (optional)

> Default: None

Enables CORS (Cross-Origin Resource Sharing) for the specified domain names or ip adresses. Define a comma-seperated list of fully qualified domain names or ip adresses or `*` to enable CORS for all domains. The latter is not recommended from a security perspective.

# Usage

For details about the API endpoints take a look at the automatically generated OpenAPI Dokumentation at `http(s)://{IP_ADDRESS}:{PORT}/docs` or `http(s)://{IP_ADRESS}:{PORT}/redoc`. There you can find everything you need to know about the endpoints and how to call them correctly. I am going to add an external documentation in the future. For this I ask for a little patience.

If you have additional questions feel free to open an issue here on GitHub.

# Changelog & Releases

This repository keeps a changelog using GitHub's releases functionality.

Releases are based on Semantic Versioning, and use the format of `MAJOR.MINOR.PATCH`. In short, the version will be incremented based on the following:

- `MAJOR`: Incompatible or major changes.
- `MINOR`: Backwards-compatible new features and enhancements.
- `PATCH`: Backwards-compatible bugfixes and package updates.

# Special Thanks

Thanks to [alextoft](https://github.com/alextoft) and [hdurdle](https://github.com/hdurdle) for their GitHub projects and shared resources about the SureFlap API.  
You can look at the projects following the links below:

- https://github.com/alextoft/sureflap
- https://github.com/hdurdle/sureflap

# Licence

Copyright 2020-2021 Fabian Eulitz

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

# Disclaimer

### This project isn’t endorsed by SureFlap Ltd. and doesn’t reflect the views or opinions of SureFlap Ltd. or anyone officially involved in producing or managing Sure Petcare.
