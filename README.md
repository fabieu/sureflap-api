<div align="center">
  <img width="256" heigth="256" src="https://gitlab.com/fabieu-ci/sureflap-api/-/raw/main/docs/assets/logo.png" alt="logo">
</div>

[![Docker Image Version (latest by date)](https://img.shields.io/docker/v/fabieu/sureflap-api?arch=amd64&sort=semver&style=for-the-badge)](https://hub.docker.com/repository/docker/fabieu/sureflap-api)
[![Docker Image Size (tag)](https://img.shields.io/docker/image-size/fabieu/sureflap-api/latest?style=for-the-badge)](https://hub.docker.com/repository/docker/fabieu/sureflap-api)
[![Gitlab pipeline status](https://img.shields.io/gitlab/pipeline-status/fabieu-ci/sureflap-api?branch=main&style=for-the-badge)](https://gitlab.com/fabieu-ci/sureflap-api/-/pipelines)
[![GitLab issues](https://img.shields.io/gitlab/issues/open/fabieu-ci/sureflap-api?style=for-the-badge)](https://gitlab.com/fabieu-ci/sureflap-api/-/issues)
[![GitLab merge requests](https://img.shields.io/gitlab/merge-requests/open-raw/fabieu-ci/sureflap-api?style=for-the-badge)](https://gitlab.com/fabieu-ci/sureflap-api/-/merge_requests)
[![GitLab](https://img.shields.io/gitlab/license/fabieu-ci/sureflap-api?style=for-the-badge)](https://gitlab.com/fabieu-ci/sureflap-api/-/blob/main/LICENSE)

# SureFlap API

SureFlap API is a simple, yet powerful RESTful API for products from [Sure Petcare](https://www.surepetcare.com).

<div align="center">
  <a href="https://fabieu-ci.gitlab.io/sureflap-api/" target="_blank" style="font-weight: bold;">
    OpenAPI documentation
  </a>
</div>

# Install

## Docker (recommended)

```bash
docker run -d -p 8080:3001 -e SUREFLAP_EMAIL={YOUR_SUREFLAP_EMAIL} -e SUREFLAP_PASSWORD={YOUR_SUREFLAP_EMAIL} fabieu/sureflap-api:latest
```

> For all available options take a look at the [Configuration](#configuration) section.

## Manual install

Clone this repository to your system and move into the sureflap project subfolder:

```bash
git clone https://gitlab.com/fabieu-ci/sureflap-api.git
```

This project utilizes **Poetry**, a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you (https://python-poetry.org/).

Install poetry via pip:

```bash
pip install --user poetry
```

Installing required dependencies and move into the virtual environment created by Pipenv:

```bash
poetry install
```

Set at least the required environment variables:

```bash
export SUREFLAP_EMAIL={YOUR_SUREFLAP_EMAIL}
export SUREFLAP_PASSWORD={YOUR_SUREFLAP_PASSWORD}
```

Start the integrated webserver with the following command:

```bash
poetry run python .\sureflap_api\main.py
```

> For all available options take a look at the [Configuration](#configuration) section.

# Configuration

The configuration is done via environment variables. The following options are available:

### `SUREFLAP_EMAIL` (required)

Email of your _Sure Petcare_ account. Make sure to use an account with control privileges if you want to use the full capabilities of this API. You can change the privileges on the official Sure Petcare website.

### `SUREFLAP_PASSWORD` (required)

Password of the in `SUREFLAP_EMAIL` specified _Sure Petcare_ account.

### `SUREFLAP_LOGLEVEL` (optional)

> Default: info

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

For details about all API endpoints and the corresponding request and response models take a look at the automatically generated OpenAPI documentation:

- **https://fabieu-ci.gitlab.io/sureflap-api/**

Here you will find everything you need to know about the available endpoints and how to call them.

If you have additional questions feel free to open an issue here on GitLab.

# Changelog & Releases

This repository keeps a changelog using GitLab's releases functionality.

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
