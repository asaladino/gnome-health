from enum import Enum, unique


@unique
class Gender(Enum):
    NOT_SET = 0
    OTHER = 1
    MALE = 2
    FEMALE = 3
