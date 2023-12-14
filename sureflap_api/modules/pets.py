# Bulit-in modules
import json
from datetime import datetime, timedelta, timezone

# PyPi modules
from fastapi import HTTPException
import requests

# Local modules
from sureflap_api.modules import auth, request_models
from sureflap_api.config import settings


def get_pets_from_household(household_id: int) -> list:
    uri = f"{settings.ENDPOINT}/api/household/{household_id}/pet"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_pet(household_id: int, pet_id: int) -> dict:
    uri = f"{settings.ENDPOINT}/api/household/{household_id}/pet"

    payload = {'with[]': ['photo', 'position']}

    response = requests.get(uri, headers=auth.auth_headers(), params=payload)

    if response.ok:
        data = json.loads(response.text)

        for pet in data['data']:
            if str(pet['id']) == str(pet_id):
                return pet
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_pet_location(pet_id: int) -> dict:
    uri = f"{settings.ENDPOINT}/api/pet/{pet_id}/position"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)

        if data['data']['where'] == 1:
            petLocation = {
                "pet_id": data['data']['pet_id'],
                "location": "inside"
            }
        else:
            petLocation = {
                "pet_id": data['data']['pet_id'],
                "location": "outside"
            }

        return petLocation
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_pets_location(household_id: int) -> list:
    pets = []
    petInfo = []

    for pet in get_pets_from_household(household_id):
        pets.append(get_pet(household_id, pet['id']))

    for pet in pets:
        since = datetime.strptime(pet['position']['since'], "%Y-%m-%dT%H:%M:%S+00:00").replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        duration = now - since

        # Remove microseconds from timedelta object
        duration = duration - timedelta(microseconds=duration.microseconds)

        if pet['position']['where'] == 1:
            location = "inside"
        else:
            location = "outside"

        petDict = {
            "name": pet['name'],
            "location": location,
            "since": since.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
            "duration": str(duration)
        }

        petInfo.append(petDict)
    return petInfo


def set_pet_location(pet_id: int, pet_location: request_models.PetLocationSet) -> dict:
    uri = f"{settings.ENDPOINT}/api/pet/{pet_id}/position"

    body = {
        "where": pet_location.where.value,  # 1 = inside, 2 = outside
        "since": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    }

    response = requests.post(uri, headers=auth.auth_headers(), data=body)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
