from enum import Enum, IntEnum


class DirectionEnum(IntEnum):
    IN = 1
    OUT = 2


class LockMode(Enum):
    NONE = "none"
    BOTH = "both"
    IN = "in"
    OUT = "out"
