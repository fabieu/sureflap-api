import json
from datetime import datetime, timezone
from typing import List

import requests
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from sureflap_api.config import settings
from sureflap_api.models import surehub
from sureflap_api.modules import auth


def get_pets() -> List[surehub.Pet]:
    uri = f"{settings.endpoint}/api/pet"

    payload = {'with[]': ['photo', 'position']}

    response = requests.get(uri, headers=auth.auth_headers(), params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_pet(pet_id: int) -> surehub.Pet:
    uri = f"{settings.endpoint}/api/pet/{pet_id}"

    payload = {'with[]': ['photo', 'position']}

    response = requests.get(uri, headers=auth.auth_headers(), params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_pet_position(pet_id: int) -> surehub.PetPosition:
    pet = get_pet(pet_id)
    return pet['position']


def get_pet_positions() -> List[surehub.PetPosition]:
    pet_positions = []
    for pet in get_pets():
        pet_positions.append(pet['position'])

    return pet_positions


def set_pet_position(pet_id: int, pet_position: surehub.CreatePetPosition) -> surehub.PetPosition:
    uri = f"{settings.endpoint}/api/pet/{pet_id}/position"

    pet_position_dict = jsonable_encoder(pet_position)

    if not pet_position_dict['since']:
        pet_position_dict['since'] = datetime.now(timezone.utc).isoformat()

    response = requests.post(uri, headers=auth.auth_headers(), json=pet_position_dict)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
