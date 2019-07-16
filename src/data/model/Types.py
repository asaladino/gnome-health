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


class QuantityType(Enum):
    """
    https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier?language=objc
    Todo: Need to add types like: HKQuantityTypeIdentifierBodyMassIndex
    """

    """
    Body Measurements
    """
    HEIGHT = 0
    # A quantity sample type that measures the user’s height.

    BODY_MASS = 1
    # A quantity sample type that measures the user’s weight.

    Body_Mass_Index = 2
    # A quantity sample type that measures the user’s body mass index.

    BODY_MASS_INDEX = 3
    # A quantity sample type that measures the user’s lean body mass.

    BODY_FAT_PERCENTAGE = 4
    # A quantity sample type that measures the user’s body fat percentage.

    WAIST_CIRCUMFERENCE = 5
    # A quantity sample type that measures the user’s waist circumference.

    """
    Vital Signs
    """
    HEART_RATE = 6
    # A quantity sample type that measures the user’s heart rate.

    RESTING_HEART_RATE = 7
    # A quantity sample type that measures the user’s resting heart rate.

    WALKING_HEART_RATE_AVERAGE = 8
    # A quantity sample type that measures the user’s heart rate while walking.

    HEART_RATE_VARIABILITY_SDNN = 9
    # A quantity sample type that measures the standard deviation of heartbeat intervals.

    OXYGEN_SATURATION = 10
    # A quantity sample type that measures the user’s oxygen saturation.

    BODY_TEMPERATURE = 11
    # A quantity sample type that measures the user’s body temperature.

    BLOOD_PRESSURE_DIASTOLIC = 12
    # A quantity sample type that measures the user’s diastolic blood pressure.

    BLOOD_PRESSURE_SYSTOLIC = 13
    # A quantity sample type that measures the user’s systolic blood pressure.

    RESPIRATORY_RATE = 14
    # A quantity sample type that measures the user’s respiratory rate.

    VO2_MAX = 15
    # A quantity sample that measures the maximal oxygen consumption during incremental exercise.

    """
    Lab and Test Results
    """

    BLOOD_ALCOHOL_CONTENT = 16
    # A quantity sample type that measures the user’s blood alcohol content.

    BLOOD_GLUCOSE = 17
    # Blood Glucose
    # A quantity sample type that measures the user’s blood glucose level.

    ELECTRODERMAL_ACTIVITY = 18
    # Electrodermal Activity
    # A quantity sample type that measures electrodermal activity.

    FORCED_EXPIRATORY_VOLUME_1 = 19
    # Forced Expiratory Volume 1
    # A quantity sample type that measures the amount of air that can be forcibly exhaled from the lungs during the first second of a forced exhalation.

    FORCED_VITAL_CAPACITY = 20
    # Forced Vital Capacity
    # A quantity sample type that measures the amount of air that can be forcibly exhaled from the lungs after taking the deepest breath possible.

    INHALER_USAGE = 21
    # Inhaler Usage
    # A quantity sample type that measures the number of puffs the user takes from their inhaler.

    INSULIN_DELIVERY = 22
    # Insulin Delivery
    # A quantity sample that measures the amount of insulin delivered.

    NUMBER_OF_TIMES_FALLEN = 23
    # Number Of Times Fallen
    # A quantity sample type that measures the number of times the user has fallen.

    PEAK_EXPIRATORY_FLOW_RATE = 24
    # Peak Expiratory Flow Rate
    # A quantity sample type that measures the user’s maximum flow rate generated during a forceful exhalation.

    PERIPHERAL_PERFUSION_INDEX = 25
    # Peripheral Perfusion Index
    # A quantity sample type that measures the user’s peripheral perfusion index.

    """
    Nutrition
    """
    DIETARY_BIOTIN = 26
    # Dietary Biotin
    # A quantity sample type that measures the amount of biotin (vitamin B7) consumed.

    DIETARY_CAFFEINE = 27
    # Dietary Caffeine
    # A quantity sample type that measures the amount of caffeine consumed.

    DIETARY_CALCIUM = 28
    # Dietary Calcium = 28
    # A quantity sample type that measures the amount of calcium consumed.

    DIETARY_CARBOHYDRATES = 29
    # Dietary Carbohydrates
    # A quantity sample type that measures the amount of carbohydrates consumed.

    DIETARY_CHLORIDE = 30
    # Dietary Chloride
    # A quantity sample type that measures the amount of chloride consumed.

    DIETARY_CHOLESTEROL = 31
    # Dietary Cholesterol
    # A quantity sample type that measures the amount of cholesterol consumed.

    DIETARY_CHROMIUM = 32
    # Dietary Chromium
    # A quantity sample type that measures the amount of chromium consumed.

    DIETARY_COPPER = 33
    # Dietary Copper
    # A quantity sample type that measures the amount of copper consumed.

    DIETARY_ENERGY_CONSUMED = 34
    # Dietary Energy Consumed
    # A quantity sample type that measures the amount of energy consumed.

    DIETARY_FAT_MONOUNSATURATED = 35
    # Dietary Fat Monounsaturated
    # A quantity sample type that measures the amount of monounsaturated fat consumed.

    DIETARY_FAT_POLYUNSATURATED = 36
    # Dietary Fat Polyunsaturated
    # A quantity sample type that measures the amount of polyunsaturated fat consumed.

    DIETARY_FAT_SATURATED = 37
    # Dietary Fat Saturated
    # A quantity sample type that measures the amount of saturated fat consumed.

    DIETARY_FAT_TOTAL = 38
    # Dietary Fat Total
    # A quantity sample type that measures the total amount of fat consumed.

    DIETARY_FIBER = 39
    # Dietary Fiber
    # A quantity sample type that measures the amount of fiber consumed.

    DIETARY_FOLATE = 40
    # Dietary Folate
    # A quantity sample type that measures the amount of folate (folic acid) consumed.

    DIETARY_IODINE = 41
    # Dietary Iodine
    # A quantity sample type that measures the amount of iodine consumed.

    DIETARY_IRON = 42
    # Dietary Iron = 42
    # A quantity sample type that measures the amount of iron consumed.

    DIETARY_MAGNESIUM = 43
    # Dietary Magnesium = 43
    # A quantity sample type that measures the amount of magnesium consumed.

    DIETARY_MANGANESE = 44
    # Dietary Manganese
    # A quantity sample type that measures the amount of manganese consumed.

    DIETARY_MOLYBDENUM = 45
    # Dietary Molybdenum
    # A quantity sample type that measures the amount of molybdenum consumed.

    DIETARY_NIACIN = 46
    # Dietary Niacin
    # A quantity sample type that measures the amount of niacin (vitamin B3) consumed.

    DIETARY_PANTOTHENIC_ACID = 47
    # Dietary Pantothenic Acid
    # A quantity sample type that measures the amount of pantothenic acid (vitamin B5) consumed.

    DIETARY_PHOSPHORUS = 48
    # Dietary Phosphorus
    # A quantity sample type that measures the amount of phosphorus consumed.

    DIETARY_POTASSIUM = 49
    # Dietary Potassium
    # A quantity sample type that measures the amount of potassium consumed.

    DIETARY_PROTEIN = 50
    # Dietary Protein
    # A quantity sample type that measures the amount of protein consumed.

    Dietary_Riboflavin = 51
    # A quantity sample type that measures the amount of riboflavin (vitamin B2) consumed.

    Dietary_Selenium = 52
    # A quantity sample type that measures the amount of selenium consumed.

    Dietary_Sodium = 53
    # A quantity sample type that measures the amount of sodium consumed.

    Dietary_Sugar = 54
    # A quantity sample type that measures the amount of sugar consumed.

    Dietary_Thiamin = 55
    # A quantity sample type that measures the amount of thiamin (vitamin B1) consumed.

    Dietary_Vitamin_A = 56
    # A quantity sample type that measures the amount of vitamin A consumed.

    Dietary_Vitamin_B12 = 57
    # A quantity sample type that measures the amount of cyanocobalamin (vitamin B12) consumed.

    Dietary_Vitamin_B6 = 58
    # A quantity sample type that measures the amount of pyridoxine (vitamin B6) consumed.

    Dietary_Vitamin_C = 59
    # A quantity sample type that measures the amount of vitamin C consumed.

    Dietary_Vitamin_D = 60
    # A quantity sample type that measures the amount of vitamin D consumed.

    Dietary_Vitamin_E = 61
    # A quantity sample type that measures the amount of vitamin E consumed.

    Dietary_Vitamin_K = 62
    # A quantity sample type that measures the amount of vitamin K consumed.

    Dietary_Water = 63
    # A quantity sample type that measures the amount of water consumed.

    Dietary_Zinc = 64
    # A quantity sample type that measures the amount of zinc consumed.

    """
    Activity
    """
    Step_Count = 65
    # A quantity sample type that measures the number of steps the user has taken.

    Distance_Walking_Running = 66
    # A quantity sample type that measures the distance the user has moved by walking or running.

    Distance_Cycling = 67
    # A quantity sample type that measures the distance the user has moved by cycling.

    Push_Count = 68
    # A quantity sample type that measures the number of pushes that the user has performed while using a wheelchair.

    Distance_Wheelchair = 69
    # A quantity sample type that measures the distance the user has moved using a wheelchair.

    Swimming_Stroke_Count = 70
    # A quantity sample type that measures the number of strokes performed while swimming.

    Distance_Swimming = 71
    # A quantity sample type that measures the distance the user has moved while swimming.

    Distance_Downhill_Snow_Sports = 72
    # A quantity sample type that measures the distance the user has traveled while skiing or snowboarding.

    Basal_Energy_Burned = 73
    # A quantity sample type that measures the resting energy burned by the user.

    Active_Energy_Burned = 74
    # A quantity sample type that measures the amount of active energy the user has burned.

    Flights_Climbed = 75
    # A quantity sample type that measures the number flights of stairs that the user has climbed.

    Nike_Fuel = 76
    # A quantity sample type that measures the number of NikeFuel points the user has earned.

    Apple_Exercise_Time = 77
    # A quantity sample type that measures the amount of time the user spent exercising.

    Apple_Stand_Time = 78
    # A quantity sample type that measures the amount of time the user has spent standing.

    """
    Reproductive Health
    """
    Basal_Body_Temperature = 79
    # A quantity sample type that measures the user’s basal body temperature.

    """
    UV Exposure
    """
    UV_Exposure = 80
    # A quantity sample type that measures the user’s exposure to UV radiation.

    """
    Audio Exposure
    """
    Environmental_Audio_Exposure = 81
    # A quantity sample type that measures audio exposure to sounds in the environment.

    Headphone_Audio_Exposure = 82
    # A quantity sample type that measures audio exposure from headphones.
