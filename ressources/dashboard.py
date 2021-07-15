from ressources import config, auth
from flask import abort
import requests
import json


def getDashboard():
    uri = config.ENDPOINT + "/api/me/start"

    headers = {'Authorization': 'Bearer %s' % auth.getToken()}

    response = requests.get(uri, headers=headers)

    if response.ok:
        data = json.loads(response.text)
        return data['data']
    else:
        abort(response.status_code)
