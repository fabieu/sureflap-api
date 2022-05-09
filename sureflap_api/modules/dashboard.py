# Bulit-in modules
import json

# PyPi modules
from fastapi import HTTPException
import requests

# Local modules
from sureflap_api.modules import auth
from sureflap_api.config import settings


def getDashboard() -> str:
    uri = f"{settings.ENDPOINT}/api/me/start"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
