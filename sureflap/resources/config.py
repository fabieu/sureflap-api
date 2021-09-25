# Pipenv modules
from typer import BadParameter

# Global configuration variables
ENDPOINT = "https://app.api.surehub.io"
PORT = None
CORS = None
EMAIL = None
PASSWORD = None
LOGLEVEL = None


def validate_loglevel(value: str):
    loglevel_values = ['critical', 'error', 'warning', 'info', 'debug', 'trace']
    if value not in loglevel_values:
        raise BadParameter(f"Only one of the following is allowed: {loglevel_values}")
    return value
