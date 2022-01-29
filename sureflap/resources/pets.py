from resources import config, auth, devices
from fastapi import HTTPException
import requests
import json
from datetime import datetime, timezone


def getPetsFromHousehold(householdID):
    uri = config.ENDPOINT + "/api/household/" + str(householdID) + "/pet"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def getPet(householdID, petID):
    uri = config.ENDPOINT + "/api/household/" + str(householdID) + "/pet"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}
    payload = {'with[]': ['photo', 'position']}

    response = requests.get(uri, headers=headers, params=payload)

    if response.ok:
        data = json.loads(response.text)

        for pet in data['data']:
            if str(pet['id']) == str(petID):
                return pet
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def getPetLocation(petID):
    uri = config.ENDPOINT + "/api/pet/" + str(petID) + "/position"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)

        if data['data']['where'] == 1:
            petLocation = {
                "pet_id": data['data']['pet_id'],
                "location": "Inside"
            }
        else:
            petLocation = {
                "pet_id": data['data']['pet_id'],
                "location": "Outside"
            }

        return petLocation
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))


def getPetsLocations(householdID):
    petInfo = []
    flaps = []
    pets = []

    deviceList = devices.getDevices()
    for device in deviceList:
        if 'parent_device_id' in device:
            flaps.append(device)

    petList = getPetsFromHousehold(householdID)
    for pet in petList:
        pets.append(getPet(householdID, pet['id']))

    for pet in pets:
        since = datetime.strptime(pet['position']['since'], "%Y-%m-%dT%H:%M:%S+00:00").replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        duration = str(now - since)
        duration = duration[0:duration.index('.')]  # Remove milliseconds

        if pet['position']['where'] == 1:
            location = "Inside"
        else:
            location = "Outside"

        petDict = {
            "name": pet['name'],
            "location": location,
            "since": since.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
            "duration": duration
        }

        petInfo.append(petDict)
    return petInfo


def setPetLocation(petID, form):
    uri = config.ENDPOINT + "/api/pet/" + str(petID) + "/position"

    headers = {'Authorization': f'Bearer {auth.getToken()}'}
    body = {
        "where": form.where.value,  # 1 = inside, 2 = outside
        "since": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    }

    response = requests.post(uri, headers=headers, data=body)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
