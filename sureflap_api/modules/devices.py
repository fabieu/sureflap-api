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


def set_lock_mode(device_id: int, lock_mode: str) -> dict:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/control"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    # Set lock mode
    lock_mode_id = None

    match lock_mode:
        case "in":
            lock_mode_id = 2  # Pets can enter the house but can no longer leave it
        case "out":
            lock_mode_id = 1  # Pets can leave the house but can no longer enter it
        case "both":
            lock_mode_id = 3  # Pets can no longer enter and leave the house
        case "none":
            lock_mode_id = 0  # Pets can enter and leave the house
        case _:
            raise HTTPException(
                status_code=400, detail="Invalid lock mode - Only 'in', 'out', 'both' or 'none' are allowed")

    data = {
        "locking": lock_mode_id
    }

    response = requests.put(uri, headers=headers,  data=data)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
