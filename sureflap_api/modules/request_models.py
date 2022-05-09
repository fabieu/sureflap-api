# Bulit-in modules

# PyPi modules

# Local modules
from enum import Enum
from pydantic import BaseModel

class Direction(Enum):
    enum_1 = 1
    enum_2 = 2
    
class PetLocationSet(BaseModel):
    where: Direction
