from ressources import config, auth, devices
from flask import abort
import requests
import json
import humanize
from dateutil import tz
from datetime import datetime

def getPetsFromHousehold(householdID):
    uri = config.endpoint + "/api/household/" + householdID + "/pet"

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}
    payload = {'with[]': ['position']}

    response = requests.get(uri, headers=headers, params=payload)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        abort(response.status_code)

def getPet(householdID, petID):
    uri = config.endpoint + "/api/household/" + householdID + "/pet"

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}
    payload = {'with[]': ['photo', 'position']} 

    response = requests.get(uri, headers=headers, params=payload)
    
    if response.ok: 
        data = json.loads(response.text)

        for pet in data['data']:
            if str(pet['id']) == str(petID):
                return pet
            else:
                return {"error": "Pet not found!"}, 404
    else:
        abort(response.status_code)

def getPetLocation(petID):
    uri = config.endpoint + "/api/pet/" + petID + "/position"

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)

        if data['data']['where'] == 1:
            petLocation = {
                "pet_id" : data['data']['pet_id'],
                "location": "Inside"
            }
        else:
            petLocation = {
                "pet_id" : data['data']['pet_id'],
                "location": "Outside"
            }

        return petLocation
    else:
        abort(response.status_code)

def getPetsLocations(householdID):
    petInfo = []
    flaps = []

    deviceList = devices.getDevices()
    for device in deviceList:
        if 'parent_device_id' in device:
            flaps.append(device)

    pets = getPetsFromHousehold(householdID)
    for pet in pets:
        sinceUTC = datetime.strptime(pet['position']['since'], "%Y-%m-%dT%H:%M:%S+00:00").replace(tzinfo=tz.tzutc())
        since = sinceUTC.astimezone(tz.tzlocal())
        now = datetime.now().replace(tzinfo=tz.tzlocal())
        duration = str(now - since)
        duration = duration[0:duration.index('.')]
        #duration = humanize.precisedelta((datetime.now() - since), format="%0.0f")
        
        if pet['position']['where'] == 1:
            location = "Inside"
        else:
            location = "Outside"

        petDict = {
            "name": pet['name'],
            "location": location,
            "since": since,
            "duration": duration
        }

        petInfo.append(petDict)
    return petInfo


def setPetLocation(petID, form):
    uri = config.endpoint + "/api/pet/" + petID + "/position"

    try:
        _ = form['where']
    except KeyError:
        return {"error": "No valid location provided. For more information visit: {ADD LINK TO DOCU}"}, 400

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}
    body = {
        "where": form['where'], #  1 = inside (default), 2 = outside
        "since": datetime.datetime.now().strftime("%Y-%m-%d %X")
    }

    response = requests.post(uri, headers=headers, data=body)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        abort(response.status_code)