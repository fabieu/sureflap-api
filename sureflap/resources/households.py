from resources import config, auth
from fastapi import HTTPException
import requests
import json


def getHouseholds():
    uri = config.ENDPOINT + "/api/household"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def getHouseholdByID(id):
    uri = config.ENDPOINT + "/api/household/" + str(id)

    headers = {'Authorization': f'Bearer {auth.getToken()}'}
    payload = {'with[]': ['pets', 'users']}

    response = requests.get(uri, headers=headers, params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
