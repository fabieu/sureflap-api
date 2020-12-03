from ressources import config, auth
from flask import abort
import requests
import json

def getDevices():
    uri = config.endpoint + "/api/device"

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        abort(response.status_code)


def getDeviceByID(id):
    uri = config.endpoint + "/api/device/" + id

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}
    payload = {'with[]': ['children', 'status', 'control']}

    response = requests.get(uri, headers=headers, params=payload)
   
    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        abort(response.status_code)
