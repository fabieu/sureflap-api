from resources import config, auth
from fastapi import HTTPException
import requests
import json


def getHouseholds():
    uri = config.ENDPOINT + "/api/household"

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code)


def getHouseholdByID(id):
    uri = config.ENDPOINT + "/api/household/" + str(id)

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}
    payload = {'with[]': ['pets', 'users']}

    response = requests.get(uri, headers=headers, params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code)
