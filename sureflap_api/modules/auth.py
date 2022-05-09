# Built-in modules
import random
import json

# PyPi modules
import requests
from cachetools import TTLCache
from fastapi import HTTPException

# Local modules
from sureflap_api.config import settings

cache = TTLCache(maxsize=128, ttl=86400)


def getToken() -> str:
    if cache.get("token"):
        return cache.get("token")
    else:
        uri = f"{settings.ENDPOINT}/api/auth/login"

        payload = {
            "email_address": settings.EMAIL,
            "password": settings.PASSWORD,
            "device_id": random.randrange(1000000000, 9999999999)
        }

        response = requests.post(uri, data=payload)

        if response.ok:
            data = json.loads(response.text)['data']
            cache["token"] = data['token']

            return cache["token"]
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
