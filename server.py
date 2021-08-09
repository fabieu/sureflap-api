from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from resources import config, devices, households, timeline, dashboard, pets, users
import uvicorn

__version__ = "1.0.0"

# FastAPI configration
app = FastAPI()


# Dashboard
@app.get('/')
async def get_dashboard():
    return dashboard.getDashboard()


@app.get('/devices')
async def get_devices():
    return devices.getDevices()


@app.get('/devices/{id}')
async def get_device_by_ID(id: int):
    return devices.getDeviceByID(id)


# Households
@app.get('/households')
async def get_households():
    return households.getHouseholds()


@app.get('/households/{householdID}')
async def get_household_by_ID(householdID: int):
    return households.getHouseholdByID(householdID)


# Pets
@app.get('/households/{householdID}/pets')
async def get_pets_from_household(householdID: int):
    return pets.getPetsFromHousehold(householdID)


@app.get('/households/{householdID}/pets/{petID}')
async def get_pet(householdID: int, petID: int):
    return pets.getPet(householdID, petID)


@app.get('/households/{householdID}/pets/{petID}/location')
async def get_pet_location(householdID: int, petID: int):
    return pets.getPetLocation(petID)


@app.get('/households/{householdID}/pets/{petID}/location')
async def set_pet_location(householdID: int, petID: int):
    return pets.setPetLocation(petID, request.form)


@app.get('/households/{householdID}/pets/location')
async def get_pets_locations(householdID: int):
    return pets.getPetsLocations(householdID)


# Users
@app.get('/households/{householdID}/users')
async def get_users_from_household(householdID: int):
    return users.getUsersFromHousehold(householdID)


@app.get('/households/{householdID}/users/{userID}')
async def get_user(householdID: int, userID: int):
    return users.getUser(userID)


@app.get('/households/{householdID}/users/{userID}/photo')
async def get_user_photo(householdID: int, userID: int):
    return users.getUserPhoto(userID)

""" 
# Currently disabled due to timeout on large timelines
# Timeline
@app.get('/households/{householdID}/timeline')
async def get_timeline(householdID: int):
    return timeline.getTimeline(householdID)
"""


def init_FastAPI():
    # Custom OpenAPI Schema
    app.openapi = custom_openapi

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
        description="This provides a standalone RESTful API for [SureFlap Products](https://www.surepetcare.com).The main functionality of this API is to provide a wrapper for the official SureFlap API for maintainability, simplicity and connectivity. This enables you to call the API from a variance of IoT devices and other applications more easily.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


if __name__ == '__main__':
    # Validate and initialize configuration by file (config.ini)
    config.init_config()

    # Call method to configure FastAPI
    init_FastAPI()

    # Run ASGI server
    uvicorn.run("server:app", port=int(config.PORT), reload=False)
