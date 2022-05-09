# Bulit-in modules
import json

# PyPi modules
from fastapi import HTTPException
import requests

# Local modules
from sureflap_api.modules import auth
from sureflap_api.config import settings


def get_devices() -> dict:
    uri = f"{settings.ENDPOINT}/api/device"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_devices_by_id(device_id: int) -> dict:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}
    payload = {'with[]': ['children', 'status', 'control']}

    response = requests.get(uri, headers=headers, params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
