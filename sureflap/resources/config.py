# Python modules
import logging

# Global configuration variables
ENDPOINT = "https://app.api.surehub.io"
PORT = None
CORS = None
EMAIL = None
PASSWORD = None
LOGLEVEL = None


def validate():
    loglevel_values = ['critical', 'error', 'warning', 'info', 'debug', 'trace']

    if not EMAIL:
        logging.error("Environment variable SUREFLAP_EMAIL needs to be set - Description: Email of the SurePetcare account used to connect to the official API")

    if not PASSWORD:
        logging.error("Environment variable SUREFLAP_PASSWORD needs to be set - Description: Password of the SurePetcare account used to connect to the official API")
    
    if not LOGLEVEL in loglevel_values:
        logging.error(f"Invalid loglevel provided - Only one of the following is allowed: {loglevel_values}")