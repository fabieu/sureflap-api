import json
from typing import List

import requests
from fastapi import HTTPException

from surehub_api.config import settings
from surehub_api.models import surehub
from surehub_api.modules import auth


def get_households() -> list:
    uri = f"{settings.endpoint}/api/household"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_household_by_id(household_id: int) -> surehub.Household:
    uri = f"{settings.endpoint}/api/household/{household_id}"

    payload = {'with[]': ['pets', 'users']}

    response = requests.get(uri, headers=auth.auth_headers(), params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_users_of_household(household_id: int) -> List[surehub.HouseholdUser]:
    uri = f"{settings.endpoint}/api/household/{household_id}/user"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_user_of_household(household_id: int, user_id: int) -> surehub.HouseholdUser:
    uri = f"{settings.endpoint}/api/household/{household_id}/user/{user_id}"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_pets_of_household(household_id: int) -> List[surehub.Pet]:
    uri = f"{settings.endpoint}/api/household/{household_id}/pet"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_pet_of_household(household_id: int, pet_id: int) -> surehub.Pet:
    uri = f"{settings.endpoint}/api/household/{household_id}/pet/{pet_id}"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_devices_of_household(household_id: int) -> list:
    uri = f"{settings.endpoint}/api/household/{household_id}/device"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_device_of_household(household_id: int, device_id: int) -> surehub.Device:
    uri = f"{settings.endpoint}/api/household/{household_id}/device/{device_id}"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
