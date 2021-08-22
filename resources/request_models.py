from datetime import datetime, time
from enum import Enum
from typing import Optional, Sequence, Union

from pydantic import BaseModel


class Direction(Enum):
    enum_1 = 1
    enum_2 = 2


class PetLocationSet(BaseModel):
    where: Direction
