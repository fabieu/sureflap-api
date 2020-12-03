from ressources import config, auth
from flask import abort
import requests
import json

def getUsersFromHousehold(householdID):
    uri = config.endpoint + "/api/household/" + householdID + "/user"

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        abort(response.status_code)

def getUser(userID):
    uri = config.endpoint + "/api/user/" + userID

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        abort(response.status_code)

def getUserPhoto(userID):
    userUri = config.endpoint + "/api/user/" + userID
    photoUri = config.endpoint + "/api/photo/"

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(userUri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        photoUri += str(data['data']['photo_id'])

        response = requests.get(photoUri, headers=headers)

        if response.ok:
            data =json.loads(response.text)
            return data['data']
        else:
            abort(response.status_code)
    else:
        abort(response.status_code)