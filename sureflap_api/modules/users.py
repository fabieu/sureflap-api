# Bulit-in modules
import json

# PyPi modules
from fastapi import HTTPException
import requests

# Local modules
from sureflap_api.modules import auth
from sureflap_api.config import settings


def get_users_from_household(household_id: int) -> list:
    uri = f"{settings.ENDPOINT}/api/household/{household_id}/user"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


@DeprecationWarning
def get_user(user_id: int) -> dict:
    uri = f"{settings.ENDPOINT}/api/user/{user_id}"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


@DeprecationWarning
def get_user_photo(user_id: int) -> dict:
    userUri = f"{settings.ENDPOINT}/api/user/{user_id}"
    photoUri = f"{settings.ENDPOINT}/api/photo/"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(userUri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        photoUri += str(data['data']['photo_id'])

        response2 = requests.get(photoUri, headers=headers)

        if response2.ok:
            data = json.loads(response2.text)
            return data['data']
        else:
            raise HTTPException(status_code=response.status_code, detail=response2.text.replace("\"", "'"))
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
