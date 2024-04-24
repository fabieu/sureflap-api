from typing import Sequence, Union

import uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from typing_extensions import Annotated

from sureflap_api import __version__
from sureflap_api.config import settings
from sureflap_api.enums import LockMode
from sureflap_api.models import response as response_models, request as request_models
from sureflap_api.modules import devices, households, dashboard, pets, users, report

# FastAPI configuration
app = FastAPI(
    title="Unofficial SureFlap API",
    version=__version__,
    description="SureFlap API is a simple, yet powerful RESTful API for products from [Sure Petcare](https://www.surepetcare.com).",
    license_info={
        "name": "Apache 2.0",
        "identifier": "Apache-2.0",
    }
)


# Redirect default url to docs
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url='/docs')


# Dashboard
@app.get('/dashboard', response_model=response_models.Dashboard, tags=["Dashboard"])
def get_dashboard():
    return dashboard.get_dashboard()


@app.get('/devices', response_model=Sequence[Union[response_models.HubShort, response_models.FlapShort]],
         tags=["Device"])
def get_devices():
    return devices.get_devices()


@app.get('/devices/{device_id}', response_model=Union[response_models.Hub, response_models.Flap], tags=["Device"])
def get_device_by_id(device_id: int):
    return devices.get_devices_by_id(device_id)


@app.patch('/devices/{device_id}/control', response_model=response_models.FlapControl, tags=["Device"])
async def set_device_lock_mode(device_id: int, lock_mode: Annotated[LockMode, Query(
    description="**none** = Pets can enter and leave the house \n\n"
                "**out** = Pets can leave the house but can no longer enter it \n\n"
                "**in** = Pets can enter the house but can no longer leave it \n\n"
                "**both** = Pets can no longer enter and leave the house \n\n")
]):
    return devices.set_lock_mode(device_id, lock_mode)


# Households
@app.get('/households', response_model=Sequence[response_models.HouseholdShort], tags=["Household"])
def get_households():
    return households.get_households()


@app.get('/households/{household_id}', response_model=response_models.Household, tags=["Household"])
def get_household_by_id(household_id: int):
    return households.get_household_by_id(household_id)


# Pets
@app.get('/households/{household_id}/pets', response_model=Sequence[response_models.PetShort], tags=["Pet"])
def get_pets_from_household(household_id: int):
    return pets.get_pets_from_household(household_id)


@app.get('/households/{household_id}/pets/{pet_id}/location', response_model=response_models.PetLocation, tags=["Pet"])
def get_pet_location(household_id: int, pet_id: int):
    return pets.get_pet_location(pet_id)


@app.post('/households/{household_id}/pets/{pet_id}/location', response_model=response_models.PetLocationUpdate,
          tags=["Pet"])
def set_pet_location(household_id: int, pet_id: int, payload: request_models.PetLocationSet):
    return pets.set_pet_location(pet_id, payload)


@app.get('/households/{household_id}/pets/location', response_model=Sequence[response_models.PetLocations],
         tags=["Pet"])
def get_pets_locations(household_id: int):
    return pets.get_pets_location(household_id)


@app.get('/households/{household_id}/pets/{pet_id}', response_model=response_models.Pet, tags=["Pet"])
def get_pet(household_id: int, pet_id: int):
    return pets.get_pet(household_id, pet_id)


# Users
@app.get('/households/{household_id}/users', response_model=Sequence[response_models.UserShort], tags=["User"])
def get_users_from_household(household_id: int):
    return users.get_users_from_household(household_id)


@app.get('/households/{household_id}/users/{user_id}', response_model=response_models.User, tags=["User"],
         deprecated=True)
def get_user(household_id: int, user_id: int):
    return users.get_user(user_id)


@app.get('/households/{household_id}/users/{user_id}/photo', response_model=response_models.Photo, tags=["User"],
         deprecated=True)
def get_user_photo(household_id: int, user_id: int):
    return users.get_user_photo(user_id)


# Reports
@app.get('/report/household/{household_id}/pet/{pet_id}', response_model=response_models.AggregatedReport, tags=["Report"])
def get_aggregate_report(household_id: int, pet_id: int):
    return report.get_aggregated_report(household_id, pet_id)


def main():
    # CORS
    if settings.cors:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.cors.split(","),
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    uvicorn.run("main:app", port=settings.port, host="0.0.0.0", log_level=settings.loglevel, reload=settings.debug)


if __name__ == '__main__':
    main()
