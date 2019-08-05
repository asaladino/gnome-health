from xml.dom import minidom
import os

from src.data.model.Me import Me
from src.data.model.Record import Record
from src.data.model.Types import Gender, BloodType, SkinType, QuantityType


class RecordsAppleHealthXmlRepository:
    data = None

    def __init__(self, location):
        self.location = location

    def load_data(self):
        self.data = minidom.parse(os.path.abspath(self.location))

    def find_me(self):
        mrs = self.data.getElementsByTagName('Me')
        if len(mrs) > 0:
            r = mrs[0]
            me = Me()
            me.set_birth(self._get_attribute_value(r, 'HKCharacteristicTypeIdentifierDateOfBirth'))
            gender = self._get_attribute_value(r, 'HKCharacteristicTypeIdentifierBiologicalSex')
            me.biological_gender = self._get_gender(gender)
            blood_type = self._get_attribute_value(r, 'HKCharacteristicTypeIdentifierBloodType')
            me.blood_type = self._get_blood_type(blood_type)
            skin_type = self._get_attribute_value(r, 'HKCharacteristicTypeIdentifierFitzpatrickSkinType')
            me.fitzpatrick_skin_type = self._get_skin_type(skin_type)
            return me
        return None

    def find_all_records(self, last_id=None):
        results = {}  # need to use a dictionary to remove any duplicate entries.
        rs = self.data.getElementsByTagName('Record')
        for r in rs:
            record = Record()
            if last_id is not None:
                last_id += 1
                record.id = last_id
            r_type = self._get_attribute_value(r, 'type')
            record.type = self._get_quantity_type(r_type)
            record.source_name = self._get_attribute_value(r, 'sourceName')
            record.source_version = self._get_attribute_value(r, 'sourceVersion')
            record.unit = self._get_attribute_value(r, 'unit')
            record.set_created(self._get_attribute_value(r, 'creationDate'))
            record.set_start(self._get_attribute_value(r, 'startDate'))
            record.set_end(self._get_attribute_value(r, 'endDate'))
            record.value = self._get_attribute_value(r, 'value')
            # not every value is a number. In the case of sleep, the value corresponds to an enum
            if self._is_number(record.value):
                record.set_hash()
                results[record.hash] = record
        return results

    '''
    https://developer.apple.com/documentation/healthkit/hkcategoryvalue
    sqlalchemy.exc.StatementError: (builtins.ValueError) could not convert string to float: 'HKCategoryValueSleepAnalysisInBed'
    [SQL: INSERT INTO record (id, hash, source_name, source_version, created, start, "end", value) VALUES (?, ?, ?, ?, ?, ?, ?, ?)]
    [parameters: [{'id': 1458981, 'source_version': '50', 'value': 'HKCategoryValueSleepAnalysisInBed', 'created': datetime.datetime(2017, 4, 13, 5, 50, 9, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'start': datetime.datetime(2017, 4, 12, 22, 50, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'hash': 'ce9efdff2a4dfdf653bd738208ae3086097b7243283ddd384bd96393', 'end': datetime.datetime(2017, 4, 13, 5, 9, 44, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'source_name': 'Clock'}, {'id': 1458982, 'source_version': '50', 'value': 'HKCategoryValueSleepAnalysisInBed', 'created': datetime.datetime(2017, 4, 13, 5, 50, 9, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'start': datetime.datetime(2017, 4, 13, 5, 22, 4, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'hash': '6a69a6f81097f3653dd96b2ef5ca711c922d42f64c2856593fec137f', 'end': datetime.datetime(2017, 4, 13, 5, 45, 4, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'source_name': 'Clock'}, {'id': 1458983, 'source_version': '50', 'value': 'HKCategoryValueSleepAnalysisInBed', 'created': datetime.datetime(2017, 4, 13, 5, 50, 9, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'start': datetime.datetime(2017, 4, 13, 5, 46, 20, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'hash': 'aaac55c01828bc85554b5bf542bfefb5f683c3355422048d4522a69f', 'end': datetime.datetime(2017, 4, 13, 5, 50, 9, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'source_name': 'Clock'}, {'id': 1458984, 'source_version': '50', 'value': 'HKCategoryValueSleepAnalysisInBed', 'created': datetime.datetime(2017, 4, 14, 5, 51, 6, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'start': datetime.datetime(2017, 4, 13, 22, 50, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'hash': '4f81e697f1624fea62e5bbeb8477ff98e1bcc3834b33bd28b4eb0a6d', 'end': datetime.datetime(2017, 4, 14, 2, 32, 40, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'source_name': 'Clock'}, {'id': 1458985, 'source_version': '50', 'value': 'HKCategoryValueSleepAnalysisInBed', 'created': datetime.datetime(2017, 4, 14, 5, 51, 6, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'start': datetime.datetime(2017, 4, 14, 2, 33, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'hash': 'c3c8735603b7efd3dfb6b916c88b3974f1151ab3afeba6ecbc3a0bfe', 'end': datetime.datetime(2017, 4, 14, 3, 0, 8, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'source_name': 'Clock'}, {'id': 1458986, 'source_version': '50', 'value': 'HKCategoryValueSleepAnalysisInBed', 'created': datetime.datetime(2017, 4, 14, 5, 51, 6, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'start': datetime.datetime(2017, 4, 14, 3, 1, 52, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'hash': '4e6bd601268f356858f5b4072c99a252462fb5793f0fa70c54c91ea2', 'end': datetime.datetime(2017, 4, 14, 3, 20, 28, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'source_name': 'Clock'}, {'id': 1458987, 'source_version': '50', 'value': 'HKCategoryValueSleepAnalysisInBed', 'created': datetime.datetime(2017, 4, 14, 5, 51, 6, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'start': datetime.datetime(2017, 4, 14, 3, 21, 44, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'hash': '0e179ceefe313e71db81e1a6c2827f316dd7106d5f2453ac024ee94c', 'end': datetime.datetime(2017, 4, 14, 3, 31, 52, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'source_name': 'Clock'}, {'id': 1458988, 'source_version': '50', 'value': 'HKCategoryValueSleepAnalysisInBed', 'created': datetime.datetime(2017, 4, 14, 5, 51, 6, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'start': datetime.datetime(2017, 4, 14, 3, 32, 20, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'hash': '61401a8ac1440f717eb009a25d7499be6222b486ff5caa07513bddef', 'end': datetime.datetime(2017, 4, 14, 5, 51, 4, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'source_name': 'Clock'}  ... displaying 10 of 11105 total bound parameter sets ...  {'id': 1470084, 'source_version': '5.2.1', 'value': 'HKCategoryValueAppleStandHourStood', 'created': datetime.datetime(2019, 6, 22, 19, 25, 48, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'start': datetime.datetime(2019, 6, 22, 19, 0, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'hash': 'ea2585a39728b547b23b4caf6c8ce3cae9c5404f20fc26ef08e6389c', 'end': datetime.datetime(2019, 6, 22, 20, 0, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'source_name': 'Adam’s Apple\xa0Watch'}, {'id': 1470085, 'source_version': '5.2.1', 'value': 'HKCategoryValueAppleStandHourStood', 'created': datetime.datetime(2019, 6, 22, 20, 8, 38, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'start': datetime.datetime(2019, 6, 22, 20, 0, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'hash': 'd8ade6fc11246d467d2224f17ac7442dd45771c39d3d0ac070c61f1e', 'end': datetime.datetime(2019, 6, 22, 21, 0, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 'source_name': 'Adam’s Apple\xa0Watch'}]]
    '''

    @staticmethod
    def _is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def _get_attribute_value(record, attribute):
        if attribute in record.attributes:
            return record.attributes[attribute].value
        return None

    @staticmethod
    def _get_gender(gender):
        """
        Get the gender based on apple developer enum
        https://developer.apple.com/documentation/healthkit/hkbiologicalsex?language=objc
        :param gender: as apple text representation.
        :return: Gender
        """
        if gender == "HKBiologicalSexNotSet":
            return Gender.NOT_SET
        if gender == "HKBiologicalSexMale":
            return Gender.MALE
        if gender == "HKBiologicalSexFemale":
            return Gender.MALE
        return Gender.OTHER

    @staticmethod
    def _get_blood_type(blood_type):
        """
        Get the blood type based on apple developer enum
        https://developer.apple.com/documentation/healthkit/hkbloodtype?language=objc
        :param blood_type: as apple text representation.
        :return: BloodType
        """
        if blood_type == "HKBloodTypeNotSet":
            return BloodType.NOT_SET
        if blood_type == "HKBloodTypeANegative":
            return BloodType.A_NEGATIVE
        if blood_type == "HKBloodTypeAPositive":
            return BloodType.A_POSITIVE
        if blood_type == "HKBloodTypeBNegative":
            return BloodType.B_NEGATIVE
        if blood_type == "HKBloodTypeBPositive":
            return BloodType.B_POSITIVE
        if blood_type == "HKBloodTypeABNegative":
            return BloodType.AB_NEGATIVE
        if blood_type == "HKBloodTypeABPositive":
            return BloodType.AB_POSITIVE
        if blood_type == "HKBloodTypeONegative":
            return BloodType.O_NEGATIVE
        if blood_type == "HKBloodTypeOPositive":
            return BloodType.O_POSITIVE
        return BloodType.NOT_SET

    @staticmethod
    def _get_skin_type(skin_type):
        """
        Get the skin type based on apple developer enum
        https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype?language=objc
        :param skin_type: as apple text representation.
        :return: SkinType
        """
        if skin_type == "HKFitzpatrickSkinTypeNotSet":
            return SkinType.NOT_SET
        if skin_type == "HKFitzpatrickSkinTypeI":
            return SkinType.TYPE_I
        if skin_type == "HKFitzpatrickSkinTypeII":
            return SkinType.TYPE_II
        if skin_type == "HKFitzpatrickSkinTypeIII":
            return SkinType.TYPE_III
        if skin_type == "HKFitzpatrickSkinTypeIV":
            return SkinType.TYPE_IV
        if skin_type == "HKFitzpatrickSkinTypeV":
            return SkinType.TYPE_V
        if skin_type == "HKFitzpatrickSkinTypeVI":
            return SkinType.TYPE_VI
        return SkinType.NOT_SET

    @staticmethod
    def _get_quantity_type(quantity_type):
        """
        Used to define the identifiers that create quantity type objects.
        https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier?language=objc
        :param quantity_type: as apple text representation.
        :return: QuantityType
        """

        """
        Body Measurements
        """
        if quantity_type == "HKQuantityTypeIdentifierHeight":
            return QuantityType.HEIGHT
        if quantity_type == "HKQuantityTypeIdentifierBodyMass":
            return QuantityType.BODY_MASS
        if quantity_type == "HKQuantityTypeIdentifierBodyMassIndex":
            return QuantityType.BODY_MASS_INDEX
        if quantity_type == "HKQuantityTypeIdentifierLeanBodyMass":
            return QuantityType.LEAN_BODY_MASS
        if quantity_type == "HKQuantityTypeIdentifierBodyFatPercentage":
            return QuantityType.BODY_FAT_PERCENTAGE
        if quantity_type == "HKQuantityTypeIdentifierWaitCircumference":
            return QuantityType.WAIST_CIRCUMFERENCE

        """
        Vital Signs
        """
        if quantity_type == "HKQuantityTypeIdentifierHeartRate":
            return QuantityType.HEART_RATE
        if quantity_type == "HKQuantityTypeIdentifierRestingHeartRate":
            return QuantityType.RESTING_HEART_RATE
        if quantity_type == "HKQuantityTypeIdentifierWalkingHeartRateAverage":
            return QuantityType.WALKING_HEART_RATE_AVERAGE
        if quantity_type == "HKQuantityTypeIdentifierHeartRateVariabilitySDNN":
            return QuantityType.HEART_RATE_VARIABILITY_SDNN
        if quantity_type == "HKQuantityTypeIdentifierOxygenSaturation":
            return QuantityType.OXYGEN_SATURATION
        if quantity_type == "HKQuantityTypeIdentifierBodyTemperature":
            return QuantityType.BODY_TEMPERATURE
        if quantity_type == "HKQuantityTypeIdentifierBloodPressureDiastolic":
            return QuantityType.BLOOD_PRESSURE_DIASTOLIC
        if quantity_type == "HKQuantityTypeIdentifierBloodPressureSystolic":
            return QuantityType.BLOOD_PRESSURE_SYSTOLIC
        if quantity_type == "HKQuantityTypeIdentifierRespiratoryRate":
            return QuantityType.RESPIRATORY_RATE
        if quantity_type == "HKQuantityTypeIdentifierVO2Max":
            return QuantityType.VO2_MAX

        """
        Lab and Test Results
        """
        if quantity_type == "HKQuantityTypeIdentifierBloodAlcoholContent":
            return QuantityType.BLOOD_ALCOHOL_CONTENT
        if quantity_type == "HKQuantityTypeIdentifierBloodGlucose":
            return QuantityType.BLOOD_GLUCOSE
        if quantity_type == "HKQuantityTypeIdentifierElectrodermalActivity":
            return QuantityType.ELECTRODERMAL_ACTIVITY
        if quantity_type == "HKQuantityTypeIdentifierForcedExpiratoryVolume1":
            return QuantityType.FORCED_EXPIRATORY_VOLUME_1
        if quantity_type == "HKQuantityTypeIdentifierForcedVitalCapacity":
            return QuantityType.FORCED_VITAL_CAPACITY
        if quantity_type == "HKQuantityTypeIdentifierInhalerUsage":
            return QuantityType.INHALER_USAGE
        if quantity_type == "HKQuantityTypeIdentifierInsulinDelivery":
            return QuantityType.INSULIN_DELIVERY
        if quantity_type == "HKQuantityTypeIdentifierNumberOfTimesFallen":
            return QuantityType.NUMBER_OF_TIMES_FALLEN
        if quantity_type == "HKQuantityTypeIdentifierPeakExpiratoryFlowRate":
            return QuantityType.PEAK_EXPIRATORY_FLOW_RATE
        if quantity_type == "HKQuantityTypeIdentifierPeripheralPerfusionIndex":
            return QuantityType.PERIPHERAL_PERFUSION_INDEX

        """
        Nutrition
        """
        if quantity_type == "HKQuantityTypeIdentifierDietaryBiotin":
            return QuantityType.DIETARY_BIOTIN
        if quantity_type == "HKQuantityTypeIdentifierDietaryCaffeine":
            return QuantityType.DIETARY_CAFFEINE
        if quantity_type == "HKQuantityTypeIdentifierDietaryCalcium":
            return QuantityType.DIETARY_CALCIUM
        if quantity_type == "HKQuantityTypeIdentifierDietaryCarbohydrates":
            return QuantityType.DIETARY_CARBOHYDRATES
        if quantity_type == "HKQuantityTypeIdentifierDietaryChloride":
            return QuantityType.DIETARY_CHLORIDE
        if quantity_type == "HKQuantityTypeIdentifierDietaryCholesterol":
            return QuantityType.DIETARY_CHOLESTEROL
        if quantity_type == "HKQuantityTypeIdentifierDietaryChromium":
            return QuantityType.DIETARY_CHROMIUM
        if quantity_type == "HKQuantityTypeIdentifierDietaryCopper":
            return QuantityType.DIETARY_COPPER
        if quantity_type == "HKQuantityTypeIdentifierDietaryEnergyConsumed":
            return QuantityType.DIETARY_ENERGY_CONSUMED
        if quantity_type == "HKQuantityTypeIdentifierDietaryFatMonounsaturated":
            return QuantityType.DIETARY_FAT_MONOUNSATURATED
        if quantity_type == "HKQuantityTypeIdentifierDietaryFatPolyunsaturated":
            return QuantityType.DIETARY_FAT_POLYUNSATURATED
        if quantity_type == "HKQuantityTypeIdentifierDietaryFatSaturated":
            return QuantityType.DIETARY_FAT_SATURATED
        if quantity_type == "HKQuantityTypeIdentifierDietaryFatTotal":
            return QuantityType.DIETARY_FAT_TOTAL
        if quantity_type == "HKQuantityTypeIdentifierDietaryFiber":
            return QuantityType.DIETARY_FIBER
        if quantity_type == "HKQuantityTypeIdentifierDietaryFolate":
            return QuantityType.DIETARY_FOLATE
        if quantity_type == "HKQuantityTypeIdentifierDietaryIodine":
            return QuantityType.DIETARY_IODINE
        if quantity_type == "HKQuantityTypeIdentifierDietaryIron":
            return QuantityType.DIETARY_IRON
        if quantity_type == "HKQuantityTypeIdentifierDietaryMagnesium":
            return QuantityType.DIETARY_MAGNESIUM
        if quantity_type == "HKQuantityTypeIdentifierDietaryManganese":
            return QuantityType.DIETARY_MANGANESE
        if quantity_type == "HKQuantityTypeIdentifierDietaryMolybdenum":
            return QuantityType.DIETARY_MOLYBDENUM
        if quantity_type == "HKQuantityTypeIdentifierDietaryNiacin":
            return QuantityType.DIETARY_NIACIN
        if quantity_type == "HKQuantityTypeIdentifierDietaryPantothenicAcid":
            return QuantityType.DIETARY_PANTOTHENIC_ACID
        if quantity_type == "HKQuantityTypeIdentifierDietaryPhosphorus":
            return QuantityType.DIETARY_PHOSPHORUS
        if quantity_type == "HKQuantityTypeIdentifierDietaryPotassium":
            return QuantityType.DIETARY_POTASSIUM
        if quantity_type == "HKQuantityTypeIdentifierDietaryProtein":
            return QuantityType.DIETARY_PROTEIN
        if quantity_type == "HKQuantityTypeIdentifierDietaryRiboflavin":
            return QuantityType.DIETARY_RIBOFLAVIN
        if quantity_type == "HKQuantityTypeIdentifierDietarySelenium":
            return QuantityType.DIETARY_SELENIUM
        if quantity_type == "HKQuantityTypeIdentifierDietarySodium":
            return QuantityType.DIETARY_SODIUM
        if quantity_type == "HKQuantityTypeIdentifierDietarySugar":
            return QuantityType.DIETARY_SUGAR
        if quantity_type == "HKQuantityTypeIdentifierDietaryThiamin":
            return QuantityType.DIETARY_THIAMIN
        if quantity_type == "HKQuantityTypeIdentifierDietaryVitaminA":
            return QuantityType.DIETARY_VITAMIN_A
        if quantity_type == "HKQuantityTypeIdentifierDietaryVitaminB12":
            return QuantityType.DIETARY_VITAMIN_B12
        if quantity_type == "HKQuantityTypeIdentifierDietaryVitaminB6":
            return QuantityType.DIETARY_VITAMIN_B6
        if quantity_type == "HKQuantityTypeIdentifierDietaryVitaminC":
            return QuantityType.DIETARY_VITAMIN_C
        if quantity_type == "HKQuantityTypeIdentifierDietaryVitaminD":
            return QuantityType.DIETARY_VITAMIN_D
        if quantity_type == "HKQuantityTypeIdentifierDietaryVitaminE":
            return QuantityType.DIETARY_VITAMIN_E
        if quantity_type == "HKQuantityTypeIdentifierDietaryVitaminK":
            return QuantityType.DIETARY_VITAMIN_K
        if quantity_type == "HKQuantityTypeIdentifierDietaryWater":
            return QuantityType.DIETARY_WATER
        if quantity_type == "HKQuantityTypeIdentifierDietaryZinc":
            return QuantityType.DIETARY_ZINC

        """
        Activity
        """
        if quantity_type == "HKQuantityTypeIdentifierStepCount":
            return QuantityType.STEP_COUNT
        if quantity_type == "HKQuantityTypeIdentifierDistanceWalkingRunning":
            return QuantityType.DISTANCE_WALKING_RUNNING
        if quantity_type == "HKQuantityTypeIdentifierDistanceCycling":
            return QuantityType.DISTANCE_CYCLING
        if quantity_type == "HKQuantityTypeIdentifierPushCount":
            return QuantityType.PUSH_COUNT
        if quantity_type == "HKQuantityTypeIdentifierDistanceWheelchair":
            return QuantityType.DISTANCE_WHEELCHAIR
        if quantity_type == "HKQuantityTypeIdentifierSwimmingStrokeCount":
            return QuantityType.SWIMMING_STROKE_COUNT
        if quantity_type == "HKQuantityTypeIdentifierDistanceSwimming":
            return QuantityType.DISTANCE_SWIMMING
        if quantity_type == "HKQuantityTypeIdentifierDistanceDownhillSnowSports":
            return QuantityType.DISTANCE_DOWNHILL_SNOW_SPORTS
        if quantity_type == "HKQuantityTypeIdentifierBasalEnergyBurned":
            return QuantityType.BASAL_ENERGY_BURNED
        if quantity_type == "HKQuantityTypeIdentifierActiveEnergyBurned":
            return QuantityType.ACTIVE_ENERGY_BURNED
        if quantity_type == "HKQuantityTypeIdentifierFlightsClimbed":
            return QuantityType.FLIGHTS_CLIMBED
        if quantity_type == "HKQuantityTypeIdentifierNikeFuel":
            return QuantityType.NIKE_FUEL
        if quantity_type == "HKQuantityTypeIdentifierAppleExerciseTime":
            return QuantityType.APPLE_EXERCISE_TIME
        if quantity_type == "HKQuantityTypeIdentifierAppleStandTime":
            return QuantityType.APPLE_STAND_TIME

        """
        Reproductive Health
        """
        if quantity_type == "HKQuantityTypeIdentifierBasalBodyTemperature":
            return QuantityType.BASAL_BODY_TEMPERATURE

        """
        UV Exposure
        """
        if quantity_type == "HKQuantityTypeIdentifierUVExposure":
            return QuantityType.UV_EXPOSURE

        """
        Audio Exposure
        """
        if quantity_type == "HKQuantityTypeIdentifierEnvironmentalAudioExposure":
            return QuantityType.ENVIRONMENTAL_AUDIO_EXPOSURE
        if quantity_type == "HKQuantityTypeIdentifierHeadphoneAudioExposure":
            return QuantityType.HEADPHONE_AUDIO_EXPOSURE
        return None
