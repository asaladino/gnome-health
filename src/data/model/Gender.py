from enum import Enum, unique


@unique
class Gender(Enum):
    OTHER = 0
    MALE = 1
    FEMALE = 2
