from datetime import datetime, time
from enum import Enum
from typing import Optional, Sequence, Union

from pydantic import BaseModel


# Multi-referenced models
class Device(BaseModel):
    firmware: Optional[float] = None
    hardware: Optional[float] = None


class Photo(BaseModel):
    created_at: Optional[datetime] = None
    id: Optional[float] = None
    location: Optional[str] = None
    updated_at: Optional[datetime] = None
    uploading_user_id: Optional[float] = None
    version: Optional[str] = None


# Pet Base Model
class Position(BaseModel):
    device_id: Optional[float] = None
    since: Optional[datetime] = None
    tag_id: Optional[float] = None
    where: Optional[float] = None


class Pet(BaseModel):
    comments: Optional[str] = None
    created_at: Optional[datetime] = None
    gender: Optional[float] = None
    household_id: Optional[float] = None
    id: Optional[float] = None
    name: Optional[str] = None
    photo: Optional[Photo] = None
    photo_id: Optional[float] = None
    position: Optional[Position] = None
    species_id: Optional[float] = None
    tag_id: Optional[float] = None
    updated_at: Optional[datetime] = None
    version: Optional[str] = None


# Pet Location Base Model
class PetLocation(BaseModel):
    location: Optional[str] = None
    pet_id: Optional[float] = None


class PetLocations(BaseModel):
    duration: Optional[str] = None
    location: Optional[str] = None
    name: Optional[str] = None
    since: Optional[datetime] = None


class PetLocationUpdate(BaseModel):
    pet_id: Optional[float] = None
    tag_id: Optional[float] = None
    user_id: Optional[float] = None
    where: Optional[float] = None
    since: Optional[datetime] = None


# User Base Model
class Notifications(BaseModel):
    animal_movement: Optional[bool] = None
    curfew: Optional[bool] = None
    device_status: Optional[bool] = None
    feeding_activity: Optional[bool] = None
    household_management: Optional[bool] = None
    intruder_movements: Optional[bool] = None
    low_battery: Optional[bool] = None
    new_device_pet: Optional[bool] = None
    photos: Optional[bool] = None


class User(BaseModel):
    country_id: Optional[float] = None
    created_at: Optional[datetime] = None
    email_adress: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[float] = None
    language_id: Optional[float] = None
    last_name: Optional[str] = None
    marketing_opt_in: Optional[bool] = None
    notifications: Optional[Notifications] = None
    terms_accepted: Optional[bool] = None
    time_format: Optional[float] = None
    updated_at: Optional[str] = None
    version: Optional[str] = None
    weight_units: Optional[float] = None


# Tag Base Model
class Tag(BaseModel):
    created_at: Optional[datetime] = None
    id: Optional[float] = None
    supported_product_ids: Optional[Sequence[float]] = None
    tag: Optional[str] = None
    updated_at: Optional[datetime] = None
    version: Optional[str] = None


# UserShort Base Model
class UserShort(BaseModel):
    created_at: Optional[datetime] = None
    id: Optional[float] = None
    owner: Optional[bool] = None
    updated_at: Optional[datetime] = None
    version: Optional[str] = None
    write: Optional[bool] = None


# UserDetail Base Model
class UserDetail(BaseModel):
    id: Optional[float] = None
    name: Optional[str] = None
    photo_id: Optional[float] = None


# HubShort Base Model
class HubShort(BaseModel):
    created_at: Optional[datetime] = None
    household_id: Optional[float] = None
    id: Optional[float] = None
    name: Optional[str] = None
    product_id: Optional[float] = None
    serial_number: Optional[str] = None
    updated_at: Optional[datetime] = None
    version: Optional[str] = None


# FlapShort Base Model
class FlapShort(BaseModel):
    created_at: Optional[datetime] = None
    household_id: Optional[float] = None
    id: Optional[float] = None
    index: Optional[float] = None
    name: Optional[str] = None
    pairing_at: Optional[datetime] = None
    parent_device_id: Optional[float] = None
    product_id: Optional[float] = None
    updated_at: Optional[datetime] = None
    version: Optional[str] = None


# HouseholdShort Base Model
class HouseholdShort(BaseModel):
    created_at: Optional[datetime] = None
    id: Optional[float] = None
    name: Optional[str] = None
    timezone_id: Optional[float] = None
    updated_at: Optional[datetime] = None
    version: Optional[str] = None


# PetShort Base Model
class PetShort(BaseModel):
    comments: Optional[str] = None
    created_at: Optional[datetime] = None
    gender: Optional[float] = None
    household_id: Optional[float] = None
    id: Optional[float] = None
    name: Optional[str] = None
    photo_id: Optional[float] = None
    species_id: Optional[float] = None
    tag_id: Optional[float] = None
    updated_at: Optional[datetime] = None
    version: Optional[str] = None


# Hub Base Model
class HubVersion(BaseModel):
    device: Optional[Device] = None


class HubStatus(BaseModel):
    led_mode: Optional[str] = None
    online: Optional[bool] = None
    pairing_mode: Optional[float] = None
    version: Optional[HubVersion] = None


class Control(BaseModel):
    led_mode: Optional[float] = None
    pairing_mode: Optional[float] = None


class Hub(BaseModel):
    children: Optional[Sequence[FlapShort]] = None
    control: Optional[Control] = None
    created_at: Optional[str] = None
    household_id: Optional[float] = None
    mac_adress: Optional[str] = None
    name: Optional[str] = None
    product_id: Optional[float] = None
    serial_number: Optional[str] = None
    status: Optional[HubStatus] = None
    updated_at: Optional[datetime] = None
    version: Optional[str] = None


# Flap Base Model
class Signal(BaseModel):
    device_rssi: Optional[str] = None
    hub_rssi: Optional[str] = None


class CurfewLock(BaseModel):
    delay_time: Optional[float] = None
    lock_time: Optional[time] = None
    locked: Optional[bool] = None
    permissions: Optional[float] = None
    unlock_time: Optional[time] = None


class Locking(BaseModel):
    curfew: Optional[CurfewLock] = None
    mode: Optional[float] = None


class FlapVersion(BaseModel):
    lcd: Optional[Device] = None
    rf: Optional[Device] = None


class FlapStatus(BaseModel):
    battery: Optional[float] = None
    learn_mode: Optional[bool] = None
    locking: Optional[Locking] = None
    online: Optional[bool] = None
    signal: Optional[Signal] = None
    version: Optional[FlapVersion] = None


class Curfew(BaseModel):
    enabled: Optional[bool] = None
    lock_time: Optional[time] = None


class FlapControl(BaseModel):
    curfew: Optional[Curfew] = None
    fast_polling: Optional[bool] = None


class Flap(BaseModel):
    control: Optional[FlapControl] = None
    created_at: Optional[datetime] = None
    household_id: Optional[float] = None
    id: Optional[float] = None
    index: Optional[float] = None
    mac_adress: Optional[str] = None
    name: Optional[str] = None
    pairing_at: Optional[datetime] = None
    parent: Optional[HubShort] = None
    parent_device_id: Optional[float] = None
    product_id: Optional[float] = None
    status: Optional[FlapStatus] = None
    updated_at: Optional[datetime] = None
    version: Optional[str] = None


# Household Base Model
class Household(BaseModel):
    created_at: Optional[datetime] = None
    id: Optional[float] = None
    name: Optional[str] = None
    pets: Optional[Sequence[PetShort]] = None
    share_code: Optional[str] = None
    timezone_id: Optional[float] = None
    updated_at: Optional[datetime] = None
    users: Optional[Sequence[UserShort]] = None
    version: Optional[str] = None


# Invite Base Model
class InviteUser(BaseModel):
    id: Optional[float] = None
    name: Optional[str] = None
    photo: Optional[Photo] = None
    photo_id: Optional[float] = None


class InviteRoles(BaseModel):
    acceptor: Optional[InviteUser] = None
    creator: Optional[InviteUser] = None


class Invite(BaseModel):
    acceptor_user_id: Optional[float] = None
    code: Optional[str] = None
    created_at: Optional[datetime] = None
    creator_user_id: Optional[float] = None
    email_adress: Optional[str] = None
    id: Optional[float] = None
    owner: Optional[bool] = None
    status: Optional[float] = None
    updated_at: Optional[datetime] = None
    user: Optional[InviteRoles] = None
    version: Optional[str] = None


# HouseholdDashboard Base Model
class HouseholdDashboard(BaseModel):
    created_at: Optional[datetime] = None
    id: Optional[float] = None
    invites: Optional[Sequence[Invite]] = None
    name: Optional[str] = None
    share_code: Optional[str] = None
    timezone_id: Optional[float] = None
    updated_at: Optional[datetime] = None
    users: Optional[Sequence[UserShort]] = None
    version: Optional[str] = None


# Dashboard Model
class Dashboard(BaseModel):
    devices: Optional[Sequence[Union[HubShort, FlapShort]]] = None
    households: Optional[Sequence[HouseholdDashboard]] = None
    pets: Optional[Sequence[Pet]] = None
    photos: Optional[Sequence[Photo]] = None
    tags: Optional[Sequence[Tag]] = None
    user: Optional[User] = None
