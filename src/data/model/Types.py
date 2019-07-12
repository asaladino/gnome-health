from enum import Enum, unique


@unique
class Gender(Enum):
    NOT_SET = 0
    OTHER = 1
    MALE = 2
    FEMALE = 3


class SkinType(Enum):
    """
    The Fitzpatrick scale is a numerical classification for skin color based on the skins response to sun exposure in
    terms of the degree of burning and tanning.
    """

    NOT_SET = 0
    # Either the user’s skin type is not set, or the user has not granted your app permission to read the skin type.

    TYPE_I = 1
    # Pale white skin that always burns easily in the sun and never tans.

    TYPE_II = 2
    # White skin that burns easily and tans minimally.

    TYPE_III = 3
    # White to light brown skin that burns moderately and tans uniformly.

    TYPE_IV = 4
    # Beige-olive, lightly tanned skin that burns minimally and tans moderately.

    TYPE_V = 5
    # Brown skin that rarely burns and tans profusely.

    TYPE_VI = 6
    # Dark brown to black skin that never burns and tans profusely.


class BloodType(Enum):
    """
    Constants indicating the user’s blood type.
    """

    NOT_SET = 0
    # Either the user’s blood type is not set, or the user has not granted your app permission to read the blood type.

    A_POSITIVE = 1
    # The user has an A+ blood type.

    A_NEGATIVE = 2
    # The user has an A– blood type.

    B_POSITIVE = 3
    # The user has an B+ blood type.

    B_NEGATIVE = 4
    # The user has an B– blood type.

    AB_POSITIVE = 5
    # The user has an AB+ blood type.

    AB_NEGATIVE = 6
    # The user has an AB– blood type.

    O_POSITIVE = 7
    # The user has an O+ blood type.

    O_NEGATIVE = 8
    # The user has an O– blood type.
