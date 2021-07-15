from ressources import config, auth
from flask import abort
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
        abort(response.status_code)


def getHouseholdByID(id):
    uri = config.ENDPOINT + "/api/household/" + id

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}
    payload = {'with[]': ['pets', 'users']}

    response = requests.get(uri, headers=headers, params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        abort(response.status_code)
