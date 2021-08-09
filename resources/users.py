from resources import config, auth
from fastapi import HTTPException
import requests
import json


def getUsersFromHousehold(householdID):
    uri = config.ENDPOINT + "/api/household/" + str(householdID) + "/user"

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code)


def getUser(userID):
    uri = config.ENDPOINT + "/api/user/" + str(userID)

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code)


def getUserPhoto(userID):
    userUri = config.ENDPOINT + "/api/user/" + str(userID)
    photoUri = config.ENDPOINT + "/api/photo/"

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(userUri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        photoUri += str(data['data']['photo_id'])

        response = requests.get(photoUri, headers=headers)

        if response.ok:
            data = json.loads(response.text)
            return data['data']
        else:
            raise HTTPException(status_code=response.status_code)
    else:
        raise HTTPException(status_code=response.status_code)
