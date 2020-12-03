# SureFlap API

## Getting started

### Installation

Clone this repository to any directory on your linux machine

```bash
git clone https://gitlab.com/home-automation-fabieu/sureflap-rest-api.git
```

Move into the cloned repository via:

```bash
cd ./sureflap-rest-api
```

If you dont want to install the packages in your main package repository you can use a virtual environment. For more instructions visit the [official Python documentation](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

Installing required dependencies:

```python
pip install -r requirements.txt
```

### Configuration

Before you can start exploring the API you have to rename the `config.ini.sample` in the root of the cloned repository to `config.ini` and edit the email and password settings. Here you need to insert the credentials for your SureFlap Petcare Account.

### PM2 Setup (Optional)

Install the daemon process manager PM2 that will help you manage and keep your application online:

```bash
npm install pm2 -g
```

Add the application to PM2:

```bash
pm2 start server.py --watch --log /var/log/sureflap.log --time --name SureFlap
```

Enable PM2 to restart the application on reboot:

```bash
pm2 startup

pm2 save
```

## Usage

For the usage of the REST API take a look at the provided OpenAPI Specification on the main page of the webserver (http://localhost:3001). There you can find everything you need to know about the given methods and how to call them.

## Roadmap

- **[ACTIVE]** Complete the OpenAPI specification
- Improve error handling to provide correct HTTP error codes
- Usage of a WSGI server for better stability and performance

## Special Thanks

Thanks to [alextoft](https://github.com/alextoft) and [hdurdle](https://github.com/hdurdle) for their GitHub projects and shared ressources about the SureFlap API.  
You can look at the projects following the links below:

- https://github.com/alextoft/sureflap
- https://github.com/hdurdle/sureflap

## Licence

Copyright 2020 Fabian Eulitz

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Disclaimer

### This project isn’t endorsed by SureFlap Ltd. and doesn’t reflect the views or opinions of SureFlap Ltd. or anyone officially involved in producing or managing Sure Petcare.
