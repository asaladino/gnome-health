from enum import Enum, unique


@unique
class Gender(Enum):
    NOT_SET = 0
    # Not Set

    OTHER = 1
    # Other

    MALE = 2
    # Male

    FEMALE = 3
    # Female


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
    # Not Set
    # Either the user’s blood type is not set, or the user has not granted your app permission to read the blood type.

    A_POSITIVE = 1
    # A+ Blood
    # The user has an A+ blood type.

    A_NEGATIVE = 2
    # A– Blood
    # The user has an A– blood type.

    B_POSITIVE = 3
    # B+ Blood
    # The user has an B+ blood type.

    B_NEGATIVE = 4
    # B– Blood
    # The user has an B– blood type.

    AB_POSITIVE = 5
    # AB+ Blood
    # The user has an AB+ blood type.

    AB_NEGATIVE = 6
    # AB– Blood
    # The user has an AB– blood type.

    O_POSITIVE = 7
    # O+ Blood
    # The user has an O+ blood type.

    O_NEGATIVE = 8
    # O– Blood
    # The user has an O– blood type.


class QuantityType(Enum):
    """
    Used to define the identifiers that create quantity type objects.
    """

    """
    Body Measurements
    """
    HEIGHT = 0
    # Height
    # A quantity sample type that measures the user’s height.

    BODY_MASS = 1
    # Body Mass
    # A quantity sample type that measures the user’s weight.

    BODY_MASS_INDEX = 2
    # Body Mass Index
    # A quantity sample type that measures the user’s body mass index.

    LEAN_BODY_MASS = 3
    # Lean Body Mass
    # A quantity sample type that measures the user’s lean body mass.

    BODY_FAT_PERCENTAGE = 4
    # Body Fat Percentage
    # A quantity sample type that measures the user’s body fat percentage.

    WAIST_CIRCUMFERENCE = 5
    # Wait Circumference
    # A quantity sample type that measures the user’s waist circumference.

    """
    Vital Signs
    """
    HEART_RATE = 6
    # Heart Rate
    # A quantity sample type that measures the user’s heart rate.

    RESTING_HEART_RATE = 7
    # Resting Heart Rate
    # A quantity sample type that measures the user’s resting heart rate.

    WALKING_HEART_RATE_AVERAGE = 8
    # Walking Heart Rate Average
    # A quantity sample type that measures the user’s heart rate while walking.

    HEART_RATE_VARIABILITY_SDNN = 9
    # Heart Rate Variability SDNN
    # A quantity sample type that measures the standard deviation of heartbeat intervals.

    OXYGEN_SATURATION = 10
    # Oxygen Saturation
    # A quantity sample type that measures the user’s oxygen saturation.

    BODY_TEMPERATURE = 11
    # Body Temperature
    # A quantity sample type that measures the user’s body temperature.

    BLOOD_PRESSURE_DIASTOLIC = 12
    # Blood Pressure Diastolic
    # A quantity sample type that measures the user’s diastolic blood pressure.

    BLOOD_PRESSURE_SYSTOLIC = 13
    # Blood Pressure Systolic
    # A quantity sample type that measures the user’s systolic blood pressure.

    RESPIRATORY_RATE = 14
    # Respiratory Rate
    # A quantity sample type that measures the user’s respiratory rate.

    VO2_MAX = 15
    # VO2 Max
    # A quantity sample that measures the maximal oxygen consumption during incremental exercise.

    """
    Lab and Test Results
    """

    BLOOD_ALCOHOL_CONTENT = 16
    # Blood Alcohol Content
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

    DIETARY_RIBOFLAVIN = 51
    # Dietary Riboflavin
    # A quantity sample type that measures the amount of riboflavin (vitamin B2) consumed.

    DIETARY_SELENIUM = 52
    # Dietary Selenium
    # A quantity sample type that measures the amount of selenium consumed.

    DIETARY_SODIUM = 53
    # Dietary Sodium
    # A quantity sample type that measures the amount of sodium consumed.

    DIETARY_SUGAR = 54
    # Dietary Sugar
    # A quantity sample type that measures the amount of sugar consumed.

    DIETARY_THIAMIN = 55
    # Dietary Thiamin
    # A quantity sample type that measures the amount of thiamin (vitamin B1) consumed.

    DIETARY_VITAMIN_A = 56
    # Dietary Vitamin A
    # A quantity sample type that measures the amount of vitamin A consumed.

    DIETARY_VITAMIN_B12 = 57
    # Dietary Vitamin B12
    # A quantity sample type that measures the amount of cyanocobalamin (vitamin B12) consumed.

    DIETARY_VITAMIN_B6 = 58
    # Dietary Vitamin B6
    # A quantity sample type that measures the amount of pyridoxine (vitamin B6) consumed.

    DIETARY_VITAMIN_C = 59
    # Dietary Vitamin C
    # A quantity sample type that measures the amount of vitamin C consumed.

    DIETARY_VITAMIN_D = 60
    # Dietary Vitamin D
    # A quantity sample type that measures the amount of vitamin D consumed.

    DIETARY_VITAMIN_E = 61
    # Dietary Vitamin E
    # A quantity sample type that measures the amount of vitamin E consumed.

    DIETARY_VITAMIN_K = 62
    # Dietary Vitamin K
    # A quantity sample type that measures the amount of vitamin K consumed.

    DIETARY_WATER = 63
    # Dietary Water
    # A quantity sample type that measures the amount of water consumed.

    DIETARY_ZINC = 64
    # Dietary Zinc
    # A quantity sample type that measures the amount of zinc consumed.

    """
    Activity
    """
    STEP_COUNT = 65
    # Step Count = 65
    # A quantity sample type that measures the number of steps the user has taken.

    DISTANCE_WALKING_RUNNING = 66
    # Distance Walking Running
    # A quantity sample type that measures the distance the user has moved by walking or running.

    DISTANCE_CYCLING = 67
    # Distance Cycling
    # A quantity sample type that measures the distance the user has moved by cycling.

    PUSH_COUNT = 68
    # Push Count
    # A quantity sample type that measures the number of pushes that the user has performed while using a wheelchair.

    DISTANCE_WHEELCHAIR = 69
    # Distance Wheelchair
    # A quantity sample type that measures the distance the user has moved using a wheelchair.

    SWIMMING_STROKE_COUNT = 70
    # Swimming Stroke Count
    # A quantity sample type that measures the number of strokes performed while swimming.

    DISTANCE_SWIMMING = 71
    # Distance Swimming
    # A quantity sample type that measures the distance the user has moved while swimming.

    DISTANCE_DOWNHILL_SNOW_SPORTS = 72
    # Distance Downhill Snow Sports
    # A quantity sample type that measures the distance the user has traveled while skiing or snowboarding.

    BASAL_ENERGY_BURNED = 73
    # Basal Energy Burned
    # A quantity sample type that measures the resting energy burned by the user.

    ACTIVE_ENERGY_BURNED = 74
    # Active Energy Burned
    # A quantity sample type that measures the amount of active energy the user has burned.

    FLIGHTS_CLIMBED = 75
    # Flights Climbed
    # A quantity sample type that measures the number flights of stairs that the user has climbed.

    NIKE_FUEL = 76
    # Nike Fuel
    # A quantity sample type that measures the number of NikeFuel points the user has earned.

    APPLE_EXERCISE_TIME = 77
    # Apple Exercise Time
    # A quantity sample type that measures the amount of time the user spent exercising.

    APPLE_STAND_TIME = 78
    # Apple Stand Time = 78
    # A quantity sample type that measures the amount of time the user has spent standing.

    """
    Reproductive Health
    """
    BASAL_BODY_TEMPERATURE = 79
    # Basal Body Temperature
    # A quantity sample type that measures the user’s basal body temperature.

    """
    UV Exposure
    """
    UV_EXPOSURE = 80
    # UV Exposure
    # A quantity sample type that measures the user’s exposure to UV radiation.

    """
    Audio Exposure
    """
    ENVIRONMENTAL_AUDIO_EXPOSURE = 81
    # Environmental Audio Exposure
    # A quantity sample type that measures audio exposure to sounds in the environment.

    HEADPHONE_AUDIO_EXPOSURE = 82
    # Headphone Audio Exposure
    # A quantity sample type that measures audio exposure from headphones.


class QuantityTypeInfo:
    info = dict()
    info[QuantityType.HEIGHT] = {
        'name': 'Height',
        'description': 'A quantity sample type that measures the user’s height.'
    }
    info[QuantityType.HEART_RATE] = {
        'name': 'Heart Rate',
        'description': 'A quantity sample type that measures the user’s heart rate.'
    }
    info[QuantityType.DISTANCE_WALKING_RUNNING] = {
        'name': 'Distance Walking Running',
        'description': 'A quantity sample type that measures the distance the user has moved by walking or running.'
    }
    info[QuantityType.STEP_COUNT] = {
        'name': 'Step Count',
        'description': 'A quantity sample type that measures the number of steps the user has taken.'
    }