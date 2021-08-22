from resources import config, auth
from fastapi import HTTPException
import requests
import json
import math


def getTimeline(householdID):
    uri = config.ENDPOINT + "/api/timeline/household/" + str(householdID)
    result = []

    headers = {'Authorization': f'Bearer {auth.getToken()}'}

    response = requests.get(uri, headers=headers, params={'page_size': 100})

    if response.ok:
        data = json.loads(response.text)
        count = data['meta']['count']
        pageSize = data['meta']['page_size']

        requestCount = math.ceil(count / pageSize)

        for i in range(1, requestCount+1):
            payload = {'page_size': 1000, 'page': i}
            response2 = requests.get(uri, headers=headers, params=payload)

            if response2.ok:
                page = json.loads(response2.text)
                result += page['data']
            else:
                raise HTTPException(status_code=response.status_code, detail=response2.text.replace("\"", "'"))

        return result
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
