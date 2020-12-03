from ressources import config
import requests
import random
import json
from cachetools import TTLCache
import time
from flask import abort

cache = TTLCache(maxsize=128, ttl=86400)

def getToken():
    try:
        _ = cache["token"]
    except KeyError:
        cache["token"] = None

    if not cache["token"] == None:
        return cache["token"]
    else:
        uri = config.endpoint + "/api/auth/login"

        postParams = {
            "email_address" : config.email,
            "password" : config.password,
            "device_id" : random.randrange(1000000000, 9999999999)
        }

        response = requests.post(uri, data=postParams)

        if response.ok:
            data = json.loads(response.text)
            cache["token"] = data['data']['token']
            
            while cache["token"] is None:
                time.sleep(0.3)
            
            return cache["token"]
        else:
            abort(response.status_code)
    