import json
import math

import requests
from fastapi import HTTPException

from surehub_api.config import settings
from surehub_api.modules import auth


def get_timeline_of_household(household_id: int) -> list:
    uri = f"{settings.endpoint}/api/timeline/household/{household_id}"
    result = []

    response = requests.get(uri, headers=auth.auth_headers(), params={'page_size': 100})

    if response.ok:
        data = json.loads(response.text)
        count = data['meta']['count']
        page_size = data['meta']['page_size']

        request_count = math.ceil(count / page_size)

        for i in range(1, request_count + 1):
            payload = {'page_size': 1000, 'page': i}
            response2 = requests.get(uri, headers=auth.auth_headers(), params=payload)

            if response2.ok:
                page = json.loads(response2.text)
                result += page['data']
            else:
                raise HTTPException(status_code=response.status_code, detail=response2.text.replace("\"", "'"))

        return result
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text.replace("\"", "'"))
