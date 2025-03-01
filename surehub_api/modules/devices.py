import json
from typing import List

import requests
from fastapi import HTTPException
from surehub_api.config import settings
from surehub_api.models import surehub
from surehub_api.models.custom import LockMode
from surehub_api.models.surehub import SpecialProfile
from surehub_api.modules import auth


def get_devices() -> List[surehub.Device]:
    uri = f"{settings.endpoint}/api/device"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_devices_by_id(device_id: int) -> surehub.Device:
    uri = f"{settings.endpoint}/api/device/{device_id}"

    payload = {'with[]': ['children', 'status', 'control']}

    response = requests.get(uri, headers=auth.auth_headers(), params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def set_lock_mode(device_id: int, lock_mode: LockMode) -> surehub.DeviceControl:
    uri = f"{settings.endpoint}/api/device/{device_id}/control"

    match lock_mode:
        case LockMode.NONE:
            lock_mode_id = 0  # Pets can enter and leave the house
        case LockMode.IN:
            lock_mode_id = 1  # Pets can enter the house but can no longer leave it
        case LockMode.OUT:
            lock_mode_id = 2  # Pets can leave the house but can no longer enter it
        case LockMode.BOTH:
            lock_mode_id = 3  # Pets can no longer enter and leave the house
        case _:
            raise HTTPException(status_code=400, detail="Invalid lock mode")

    data = {
        "locking": lock_mode_id
    }

    response = requests.put(uri, headers=auth.auth_headers(), json=data)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_tags_of_device(device_id: int) -> List[surehub.Tag]:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/tag"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_tag_of_device(device_id: int, tag_id: int) -> surehub.Tag:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/tag/{tag_id}"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def assign_tag_to_device(device_id: int, tag_id: int) -> surehub.Tag:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/tag/{tag_id}"

    data = {
        "profile": SpecialProfile.SPECIAL_PROFILE_0  # It is currently not known what this is for
    }

    response = requests.put(uri, headers=auth.auth_headers(), json=data)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def remove_tag_from_device(device_id: int, tag_id: int) -> surehub.Tag:
    uri = f"{settings.ENDPOINT}/api/device/{device_id}/tag/{tag_id}"

    response = requests.delete(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
