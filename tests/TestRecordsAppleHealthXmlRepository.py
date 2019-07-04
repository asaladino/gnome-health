import unittest
from src.data.repository.RecordsAppleHealthXmlRepository import RecordsAppleHealthXmlRepository


class TestRecordsAppleHealthXmlRepository(unittest.TestCase):

    def test_import(self):
        repo = RecordsAppleHealthXmlRepository('../../gnome-health-data/export/apple_health_export/export_sample.xml')
        repo.load_data()

        my_info = repo.find_me()
        self.assertIsNotNone(my_info)

        my_records = repo.find_all_records()
        self.assertTrue(len(my_records) > 0)
