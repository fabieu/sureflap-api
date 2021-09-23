from resources import config, auth
from fastapi import HTTPException
import requests
import json


def getDevices():
    uri = config.ENDPOINT + "/api/device"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def getDeviceByID(id):
    uri = config.ENDPOINT + "/api/device/" + str(id)

    headers = {'Authorization': f'Bearer {auth.getToken()}'}
    payload = {'with[]': ['children', 'status', 'control']}

    response = requests.get(uri, headers=headers, params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
