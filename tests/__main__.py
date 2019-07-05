import unittest

from tests.data.model.test_record import TestRecord
from tests.data.repository.test_recordsAppleHealthXmlRepository import TestRecordsAppleHealthXmlRepository


def suite():
    s = unittest.TestSuite()
    s.addTest(TestRecord('test_format_date'))
    s.addTest(TestRecordsAppleHealthXmlRepository('test_import'))
    return s


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
