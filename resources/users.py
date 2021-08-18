from resources import config, auth
from fastapi import HTTPException
import requests
import json


def getUsersFromHousehold(householdID):
    uri = config.ENDPOINT + "/api/household/" + str(householdID) + "/user"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def getUser(userID):
    uri = config.ENDPOINT + "/api/user/" + str(userID)

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def getUserPhoto(userID):
    userUri = config.ENDPOINT + "/api/user/" + str(userID)
    photoUri = config.ENDPOINT + "/api/photo/"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(userUri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        photoUri += str(data['data']['photo_id'])

        response2 = requests.get(photoUri, headers=headers)

        if response2.ok:
            data = json.loads(response2.text)
            return data['data']
        else:
            raise HTTPException(status_code=response.status_code, detail=response2.text.replace("\"", "'"))
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
