import unittest
from datetime import datetime

from src.data.model import consts
from src.data.model.Record import Record
from src.data.model.Types import QuantityType


class TestRecord(unittest.TestCase):

    def test_format_date(self):
        """
        Make sure the date time is getting converted correctly.
        :return: None
        """
        record = Record()
        date1 = "2018-09-27 19:01:47 -0400"
        record.set_start(date1)

        self.assertIsNotNone(record.start)

        print(record.start)

    def test_set_id(self):
        record = Record()
        record.set_hash()
        self.assertIsNotNone(record.hash)

    def test_build_from_dict(self):
        date = "2018-09-27 19:01:47 -0400"
        record_dict = {
            'type': QuantityType.BASAL_ENERGY_BURNED.value,
            'source_name': 'test function',
            'source_version': '1.0.1',
            'unit': 'km',
            'created': date,
            'start': date,
            'end': date,
            'value': 265,
        }
        record = Record.build_from_dict(record_dict)
        self.assertEqual(record_dict['type'], record.type.value)
        self.assertEqual(record_dict['source_name'], record.source_name)
        self.assertEqual(record_dict['source_version'], record.source_version)
        self.assertEqual(record_dict['unit'], record.unit)
        self.assertEqual(datetime.strptime(record_dict['created'], consts.date_time_format), record.created)
        self.assertEqual(datetime.strptime(record_dict['start'], consts.date_time_format), record.start)
        self.assertEqual(datetime.strptime(record_dict['end'], consts.date_time_format), record.end)
        self.assertEqual(record_dict['value'], record.value)
