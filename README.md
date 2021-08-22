# SureFlap API

SureFlap API is a standalone RESTful API for products from [Sure Petcare](https://www.surepetcare.com). The main functionality of this API is to provide a wrapper for the official SureFlap API for maintainability, simplicity and connectivity. This enables a variety of IoT devices and other applications to connect to SureFlap devices more easily. The API is completly written in Python. And the best is, you can get started within minutes.

![SureFlap APi Features](./docs/sureflap_api_features.jpg)

## Requirements

- Python >= 3.5

## Installation

Clone this repository to your system and move into the root folder:

```bash
git clone https://github.com/fabieu/sureflap-api.git && cd ./sureflap-api
```

This project utilizes **Pipenv**, a production-ready tool that aims to bring the best of all packaging worlds to the Python world. It harnesses Pipfile, pip, and virtualenv into one single command. You can read more about Pipenv [here](https://pipenv-fork.readthedocs.io/en/latest/).

Install pipenv via Pip:

```bash
pip install --user pipenv
```

Installing required dependencies in a virtual environment with Pipenv:

```bash
pipenv install
```

## Configuration

Before you can start exploring the API you have to rename the `config.ini.sample` in the root of the cloned repository to `config.ini` and edit the email and password settings. Here you need to insert the credentials for your SureFlap Petcare account.

Examle configuration:

```ini
[api]
log_level = info
debug = false
port = 3001

[user]
email = {SureFlap Account E-Mail}
password = {SureFlap Account Password}
```

> Note: This is just an example, don't copy and paste it! Please create your own!

### **Section: `[api]`**

### Option: `log_level`

The `log_level` option controls the level of log output and can be changed to be more or less verbose, which might be useful when you are dealing with an unknown issue.

- `trace`: Show every detail, like all called internal functions.
- `debug`: Shows detailed debug information.
- `info`: Normal (usually) interesting events.
- `warning`: Exceptional occurrences that are not errors.
- `error`: Runtime errors that do not require immediate action.
- `fatal`: Something went terribly wrong. Add-on becomes unusable.

By default, the log_level is set to `info`, which is the recommended setting unless you are troubleshooting.

### Option: `port`

The port for the ASGI server. This is the same as the port used for API requests. Please make sure that the specified port isn't used by another application.

### Option: `debug`

Enables/disables "Debug mode". This is useful for development or testing purposes. Currently this only changes the automatic reload of the ASGI server if a file change is detected. Set `true` to enable it, `false` otherwise.

### Option: `cors` (optional)

Enables CORS (Cross-Origin Resource Sharing) for the specified domain names or ip adresses. Define a comma-seperated list of fully qualified domain names or ip adresses or `*` to enable for CORS for all domains. This is not recommended from a security perspective.

### **Section: `[auth]`**

### Option: `email`

Email of a _Sure Petcare_ account. Make sure to use an account with control privileges if you want to use the full capabilities of this API. You can change the privileges on the official Sure Petcare website. Please specifiy the email without quotes!

### Option: `password`

Password of the in `email` specified _Sure Petcare_ account. Please specifiy the password without quotes!

## Usage

Start the ASGI server with the following command:

```bash
pipenv run python server.py
```

For the usage and details of the REST API take a look at the provided OpenAPI Specification (`http://{IP_ADRESS}:{PORT}/docs` or `http://{IP_ADRESS}:{PORT}/redoc`). There you can find everything you need to know about the provided methods and how to call them correctly.

### PM2 Setup (Optional)

Install the daemon process manager PM2 that will help you manage and keep your application online ([Read more](https://pm2.keymetrics.io/)):

#### Requirements

- NodeJS
- NPM

Install the PM2 daemon globally:

```bash
npm install pm2 -g
```

Add the application to PM2:

```bash
pm2 start pipenv run server.py --watch --time --name SureFlap_API
```

## Changelog & Releases

This repository keeps a changelog using GitHub's releases functionality.

Releases are based on Semantic Versioning, and use the format of `MAJOR.MINOR.PATCH`. In short, the version will be incremented based on the following:

- `MAJOR`: Incompatible or major changes.
- `MINOR`: Backwards-compatible new features and enhancements.
- `PATCH`: Backwards-compatible bugfixes and package updates.

## Special Thanks

Thanks to [alextoft](https://github.com/alextoft) and [hdurdle](https://github.com/hdurdle) for their GitHub projects and shared resources about the SureFlap API.  
You can look at the projects following the links below:

- https://github.com/alextoft/sureflap
- https://github.com/hdurdle/sureflap

## Licence

Copyright 2020-2021 Fabian Eulitz

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## Disclaimer

### This project isn’t endorsed by SureFlap Ltd. and doesn’t reflect the views or opinions of SureFlap Ltd. or anyone officially involved in producing or managing Sure Petcare.
