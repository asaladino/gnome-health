from xml.dom import minidom

from src.data.model.Me import Me
from src.data.model.Record import Record
from src.data.model.Gender import Gender


class RecordsAppleHealthXmlRepository:

    def __init__(self, location):
        self.data = None
        self.location = location

    def load_data(self):
        self.data = minidom.parse(self.location)

    def find_me(self):
        mrs = self.data.getElementsByTagName('Me')
        if len(mrs) > 0:
            r = mrs[0]
            me = Me()
            me.set_birth(self._get_attribute_value(r, 'HKCharacteristicTypeIdentifierDateOfBirth'))
            gender = self._get_attribute_value(r, 'HKCharacteristicTypeIdentifierBiologicalSex')
            me.biological_gender = self._get_gender(gender)
            me.blood_type = self._get_attribute_value(r, 'HKCharacteristicTypeIdentifierBloodType')
            me.fitzpatrick_skin_type = self._get_attribute_value(r, 'HKCharacteristicTypeIdentifierFitzpatrickSkinType')
            return me
        return None

    def find_all_records(self):
        result = []
        rs = self.data.getElementsByTagName('Record')
        for r in rs:
            record = Record()
            record.type = self._get_attribute_value(r, 'type')
            record.source_name = self._get_attribute_value(r, 'sourceName')
            record.source_version = self._get_attribute_value(r, 'sourceVersion')
            record.unit = self._get_attribute_value(r, 'unit')
            record.set_created(self._get_attribute_value(r, 'creationDate'))
            record.set_start(self._get_attribute_value(r, 'startDate'))
            record.set_end(self._get_attribute_value(r, 'endDate'))
            record.value = self._get_attribute_value(r, 'value')
            result.append(record)
        return result

    @staticmethod
    def _get_gender(gender):
        """
        Get the gender based on apple developer enum
        https://developer.apple.com/documentation/healthkit/hkbiologicalsex?language=objc
        :param gender: as apple text representation.
        :return: Gender
        """
        if gender == "HKBiologicalSexMale":
            return Gender.MALE
        if gender == "HKBiologicalSexFemale":
            return Gender.MALE
        return Gender.OTHER

    @staticmethod
    def _get_attribute_value(record, attribute):
        if attribute in record.attributes:
            return record.attributes[attribute].value
        return None
