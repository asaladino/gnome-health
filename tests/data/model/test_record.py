import unittest

from src.data.model.Record import Record


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