from ressources import config, auth
from flask import abort
import requests
import json

def getHouseholds():
    uri = config.endpoint + "/api/household"

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(uri, headers=headers).json()
    
    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        abort(response.status_code)

def getHouseholdByID(id):
    uri = config.endpoint + "/api/household/" + id

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}
    payload = {'with[]': ['pets', 'users']}

    response = requests.get(uri, headers=headers, params=payload)
   
    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        abort(response.status_code)