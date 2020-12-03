from ressources import config, auth
from flask import abort
import requests
import json
import math

def getTimeline(householdID):
    uri = config.endpoint + "/api/timeline/household/" + householdID
    result = []

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(uri, headers=headers, params={'page_size' : 100})

    if response.ok:
        data = json.loads(response.text)
        count = data['meta']['count']
        pageSize = data['meta']['page_size']

        requestCount = math.ceil(count / pageSize)

        for i in range(1, requestCount+1):
            payload = {'page_size' : 100, 'page' : i}
            response = requests.get(uri, headers=headers, params=payload)

            if response.ok:
                page = json.loads(response.text)
                result += page['data']
            else: 
                abort(response.status_code)

        return result
    else:
        abort(response.status_code)
        