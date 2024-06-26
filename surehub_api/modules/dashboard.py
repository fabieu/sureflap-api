import json

import requests
from fastapi import HTTPException

from surehub_api.config import settings
from surehub_api.models import surehub
from surehub_api.modules import auth


def get_dashboard() -> surehub.MeStart:
    uri = f"{settings.endpoint}/api/me/start"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
