# Python modules
from os import environ

# Pip modules
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
import uvicorn
from typing import Sequence, Union

# Custom modules
from resources import config, devices, households, dashboard, pets, users, response_models, request_models
from _version import __version__


# FastAPI configration
app = FastAPI()


# Redirect default url to docs
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url='/redoc')


# Dashboard
@app.get('/dashboard', response_model=response_models.Dashboard)
def get_dashboard():
    return dashboard.getDashboard()


@app.get('/devices', response_model=Sequence[Union[response_models.HubShort, response_models.FlapShort]])
def get_devices():
    return devices.getDevices()


@app.get('/devices/{id}', response_model=Union[response_models.Hub, response_models.Flap])
def get_device_by_ID(id: int):
    return devices.getDeviceByID(id)


# Households
@app.get('/households', response_model=Sequence[response_models.HouseholdShort])
def get_households():
    return households.getHouseholds()


@app.get('/households/{householdID}', response_model=response_models.Household)
def get_household_by_ID(householdID: int):
    return households.getHouseholdByID(householdID)


# Pets
@app.get('/households/{householdID}/pets', response_model=Sequence[response_models.PetShort])
def get_pets_from_household(householdID: int):
    return pets.getPetsFromHousehold(householdID)


@app.get('/households/{householdID}/pets/{petID}', response_model=response_models.Pet)
def get_pet(householdID: int, petID: int):
    return pets.getPet(householdID, petID)


@app.get('/households/{householdID}/pets/{petID}/location', response_model=response_models.PetLocation)
def get_pet_location(householdID: int, petID: int):
    return pets.getPetLocation(petID)


@app.post('/households/{householdID}/pets/{petID}/location', response_model=response_models.PetLocationUpdate)
def set_pet_location(householdID: int, petID: int, payload: request_models.PetLocationSet):
    return pets.setPetLocation(petID, payload)


@app.get('/households/{householdID}/pets/location', response_model=Sequence[response_models.PetLocations])
def get_pets_locations(householdID: int):
    return pets.getPetsLocations(householdID)


# Users
@app.get('/households/{householdID}/users', response_model=Sequence[response_models.UserShort])
def get_users_from_household(householdID: int):
    return users.getUsersFromHousehold(householdID)


@app.get('/households/{householdID}/users/{userID}', response_model=response_models.User)
def get_user(householdID: int, userID: int):
    return users.getUser(userID)


@app.get('/households/{householdID}/users/{userID}/photo', response_model=response_models.Photo)
def get_user_photo(householdID: int, userID: int):
    return users.getUserPhoto(userID)


def init_FastAPI():
    # CORS Configuration
    if config.CORS is not None:
        origins = config.CORS.split(",")

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


# Extending the automatically generated OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Unofficial SureFlap API",
        version=__version__,
        description="SureFlap API is a standalone RESTful API for products from [Sure Petcare](https://www.surepetcare.com). The main functionality of this API is to provide a wrapper for the official SureFlap API for maintainability, simplicity and connectivity. This enables a variety of IoT devices and other applications to connect to SureFlap devices more easily.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi


def main():
    # Set config variables
    config.EMAIL = environ.get("SUREFLAP_EMAIL")
    config.PASSWORD = environ.get("SUREFLAP_PASSWORD")
    config.PORT = environ.get("SUREFLAP_PORT", 3001)
    config.LOGLEVEL = environ.get("SUREFLAP_LOGLEVEL", "warning")
    config.CORS = environ.get("SUREFLAP_CORS", None)
    config.validate()

    # Call method to configure FastAPI
    init_FastAPI()

    # Run ASGI server
    uvicorn.run("server:app", port=config.PORT, host="0.0.0.0", log_level=config.LOGLEVEL)


if __name__ == '__main__':
    main()
