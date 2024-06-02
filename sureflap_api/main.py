from typing import List

import uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from typing import Sequence, Union
from typing_extensions import Annotated

from sureflap_api import __version__
from sureflap_api.config import settings
from sureflap_api.models import surehub, custom
from sureflap_api.modules import devices, households, dashboard, pets

# FastAPI configuration
app = FastAPI(
    title="Unofficial SureFlap API",
    version=__version__,
    description="SureFlap API is a simple, yet powerful RESTful-API for products from [Sure Petcare](https://www.surepetcare.com).",
    license_info={
        "name": "Apache 2.0",
        "identifier": "Apache-2.0",
    }
)


# Redirect default url to docs
@app.get("/",
         include_in_schema=False)
async def root():
    return RedirectResponse(url='/docs')


# Dashboard
@app.get('/dashboard',
         response_model_exclude_none=True,
         tags=["Dashboard"])
async def get_dashboard() -> surehub.MeStart:
    return dashboard.get_dashboard()


@app.get('/devices',
         response_model_exclude_none=True,
         tags=["Device"])
async def get_devices() -> List[surehub.Device]:
    return devices.get_devices()


@app.get('/devices/{device_id}',
         response_model_exclude_none=True,
         tags=["Device"])
async def get_device_by_id(device_id: int) -> surehub.Device:
    return devices.get_devices_by_id(device_id)


@app.patch('/devices/{device_id}/control',
           response_model_exclude_none=True,
           tags=["Device"])
async def set_device_lock_mode(device_id: int, lock_mode: Annotated[custom.LockMode, Query(
    description="**none** = Pets can enter and leave the house \n\n"
                "**out** = Pets can leave the house but can no longer enter it \n\n"
                "**in** = Pets can enter the house but can no longer leave it \n\n"
                "**both** = Pets can no longer enter and leave the house \n\n")
]) -> surehub.DeviceControl:
    return devices.set_lock_mode(device_id, lock_mode)


@app.put('/devices/{device_id}/tag/{pet_id}', response_model=Union[response_models.Flap], tags=["Device"])
def assign_pet_to_device(device_id: int, pet_id: int):
    return devices.assign_pet_to_device(device_id, pet_id)


@app.delete('/devices/{device_id}/tag/{pet_id}', status_code=204, tags=["Device"])
def remove_pet_from_device(device_id: int, pet_id: int):
    return devices.remove_pet_from_device(device_id, pet_id)


# Household
@app.get('/households',
         response_model_exclude_none=True,
         tags=["Household"])
async def get_households() -> List[surehub.Household]:
    return households.get_households()


@app.get('/households/{household_id}',
         response_model_exclude_none=True,
         tags=["Household"])
async def get_household_by_id(household_id: int) -> surehub.Household:
    return households.get_household_by_id(household_id)


@app.get('/households/{household_id}/users',
         response_model_exclude_none=True,
         tags=["Household"])
async def get_users_of_household(household_id: int) -> List[surehub.HouseholdUser]:
    return households.get_users_of_household(household_id)


@app.get('/households/{household_id}/users/{user_id}',
         response_model_exclude_none=True,
         tags=["Household"])
async def get_user(household_id: int, user_id: int) -> surehub.HouseholdUser:
    return households.get_user_of_household(household_id, user_id)


@app.get('/households/{household_id}/pets',
         response_model_exclude_none=True,
         tags=["Household"])
async def get_pets_of_household(household_id: int) -> List[surehub.Pet]:
    return households.get_pets_of_household(household_id)


@app.get('/households/{household_id}/pets/{pet_id}',
         response_model_exclude_none=True,
         tags=["Household"])
async def get_pet_of_household(household_id: int, pet_id: int) -> surehub.Pet:
    return households.get_pet_of_household(household_id, pet_id)


@app.get('/households/{household_id}/devices',
         response_model_exclude_none=True,
         tags=["Household"])
async def get_devices_of_household(household_id: int) -> List[surehub.Device]:
    return households.get_devices_of_household(household_id)


@app.get('/households/{household_id}/devices/{device_id}',
         response_model_exclude_none=True,
         tags=["Household"])
async def get_device_of_household(household_id: int, device_id: int) -> surehub.Device:
    return households.get_device_of_household(household_id, device_id)


# Pet
@app.get('/pets',
         response_model_exclude_none=True,
         tags=["Pet"])
async def get_all_pets() -> List[surehub.Pet]:
    return pets.get_pets()


@app.get('/pets/position',
         response_model_exclude_none=True,
         tags=["Pet"])
async def get_all_pets_positions() -> List[surehub.PetPosition]:
    return pets.get_pet_positions()


@app.get('/pets/{pet_id}',
         response_model_exclude_none=True,
         tags=["Pet"])
def get_pet(pet_id: int) -> surehub.Pet:
    return pets.get_pet(pet_id)


@app.get('/pets/{pet_id}/position',
         response_model_exclude_none=True,
         tags=["Pet"])
async def get_pet_position(pet_id: int) -> surehub.PetPosition:
    return pets.get_pet_position(pet_id)


@app.post('/pets/{pet_id}/position',
          response_model_exclude_none=True,
          tags=["Pet"],
          description="""
          Parameter `where`: **1** = Inside, **2** = Outside
          """)
async def set_pet_position(pet_id: int, payload: surehub.CreatePetPosition) -> surehub.PetPosition:
    return pets.set_pet_position(pet_id, payload)


@app.get('/households/{household_id}/pets/{pet_id}/location',
         response_model_exclude_none=True,
         tags=["Pet"],
         description="Use GET `/pets/{pet_id}/position` instead.",
         deprecated=True)
async def get_pet_location(household_id: int, pet_id: int) -> surehub.PetPosition:
    return pets.get_pet_position(pet_id)


@app.post('/households/{household_id}/pets/{pet_id}/location',
          response_model_exclude_none=True,
          tags=["Pet"],
          description="Use POST `/pets/{pet_id}/position` instead.",
          deprecated=True)
async def set_pet_location(household_oid: int, pet_id: int, payload: surehub.CreatePetPosition) -> surehub.PetPosition:
    return pets.set_pet_position(pet_id, payload)


@app.get('/households/{household_id}/pets/location',
         response_model_exclude_none=True,
         tags=["Pet"],
         description="Use GET `/pets/positions` instead.",
         deprecated=True)
async def get_pets_locations() -> List[surehub.PetPosition]:
    return pets.get_pet_positions()


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
