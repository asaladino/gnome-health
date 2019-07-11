from enum import Enum, unique


@unique
class Gender(Enum):
    NOT_SET = 0
    OTHER = 1
    MALE = 2
    FEMALE = 3


class BloodType(Enum):
    """
    Constants indicating the user’s blood type.
    """

    NOT_SET = 0
    """
    Either the user’s blood type is not set, or the user has not granted your app permission to read the blood type.
    """

    A_POSITIVE = 1
    """
    The user has an A+ blood type.
    """

    A_NEGATIVE = 2
    """
    The user has an A– blood type.
    """

    B_POSITIVE = 3
    """
    The user has an B+ blood type.
    """

    B_NEGATIVE = 4
    """
    The user has an B– blood type.
    """

    AB_POSITIVE = 5
    """
    The user has an AB+ blood type.
    """

    AB_NEGATIVE = 6
    """
    The user has an AB– blood type.
    """

    O_POSITIVE = 7
    """
    The user has an O+ blood type.
    """

    O_NEGATIVE = 8
    """
    The user has an O– blood type.
    """
