from resources import config, auth
from fastapi import HTTPException
import requests
import json


def getDashboard():
    uri = config.ENDPOINT + "/api/me/start"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
