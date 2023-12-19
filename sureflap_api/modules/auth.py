# Built-in modules
import json
from uuid import uuid1

# PyPi modules
import requests
from cachetools import TTLCache
from fastapi import HTTPException

# Local modules
from sureflap_api.config import settings

cache = TTLCache(maxsize=128, ttl=86400)


def default_headers() -> dict[str, str]:
    return {
        "Host": "app.api.surehub.io",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en-GB;q=0.9",
        "Content-Type": "application/json",
        "Origin": "https://surepetcare.io",
        "Referer": "https://surepetcare.io",
        "X-Requested-With": "com.sureflap.surepetcare",
        "X-Device-Id": str(uuid1()),
    }


def auth_headers() -> dict[str, str]:
    return default_headers() | {
        "Authorization": f"Bearer {get_token()}",
    }


def get_token() -> str:
    token = cache.get("token")

    if token:
        return token
    else:
        uri = f"{settings.ENDPOINT}/api/auth/login"

        payload = {
            "email_address": settings.EMAIL,
            "password": settings.PASSWORD,
            "device_id": str(uuid1()),
        }

        response = requests.post(uri, json=payload, headers=default_headers())

        if response.ok:
            data = json.loads(response.text)['data']
            cache["token"] = data['token']

            return cache["token"]
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
