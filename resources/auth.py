from resources import config
import requests
import random
import json
from cachetools import TTLCache
from fastapi import HTTPException

cache = TTLCache(maxsize=128, ttl=86400)


def getToken():
    try:
        _ = cache["token"]
    except KeyError:
        cache["token"] = None

    if cache["token"] is not None:
        return cache["token"]
    else:
        uri = config.ENDPOINT + "/api/auth/login"

        payload = {
            "email_address": config.EMAIL,
            "password": config.PASSWORD,
            "device_id": random.randrange(1000000000, 9999999999)
        }

        response = requests.post(uri, data=payload)

        if response.ok:
            data = json.loads(response.text)['data']
            cache["token"] = data['token']

            return data["token"]
        else:
            raise HTTPException(status_code=response.status_code)
