from pydantic import BaseModel

from sureflap_api.enums import DirectionEnum


class PetLocationSet(BaseModel):
    where: DirectionEnum
