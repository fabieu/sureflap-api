from resources import config, auth
from fastapi import HTTPException
import requests
import json


def getDevices():
    uri = config.ENDPOINT + "/api/device"

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code)


def getDeviceByID(id):
    uri = config.ENDPOINT + "/api/device/" + str(id)

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}
    payload = {'with[]': ['children', 'status', 'control']}

    response = requests.get(uri, headers=headers, params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code)
