import json

import requests
from fastapi import HTTPException

from sureflap_api.config import settings
from sureflap_api.modules import auth


def get_households() -> list:
    uri = f"{settings.endpoint}/api/household"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def get_household_by_id(household_id: int) -> dict:
    uri = f"{settings.endpoint}/api/household/{household_id}"

    payload = {'with[]': ['pets', 'users']}

    response = requests.get(uri, headers=auth.auth_headers(), params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
