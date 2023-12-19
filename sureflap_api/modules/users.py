import json

import requests
from fastapi import HTTPException

from sureflap_api.config import settings
from sureflap_api.modules import auth


def get_users_from_household(household_id: int) -> list:
    uri = f"{settings.ENDPOINT}/api/household/{household_id}/user"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


@DeprecationWarning
def get_user(user_id: int) -> dict:
    uri = f"{settings.ENDPOINT}/api/user/{user_id}"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


@DeprecationWarning
def get_user_photo(user_id: int) -> dict:
    userUri = f"{settings.ENDPOINT}/api/user/{user_id}"
    photoUri = f"{settings.ENDPOINT}/api/photo/"

    response = requests.get(userUri, headers=auth.auth_headers())

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
