# Bulit-in modules
import json

# PyPi modules
from fastapi import HTTPException
import requests

# Local modules
from sureflap_api.modules import auth
from sureflap_api.config import settings


def get_dashboard() -> dict:
    uri = f"{settings.ENDPOINT}/api/me/start"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
