import json

import requests
from fastapi import HTTPException

from sureflap_api.config import settings
from sureflap_api.modules import auth


def get_dashboard() -> dict:
    uri = f"{settings.endpoint}/api/me/start"

    response = requests.get(uri, headers=auth.auth_headers())

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
