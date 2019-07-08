import unittest
from src.data.repository.RecordsAppleHealthXmlRepository import RecordsAppleHealthXmlRepository


class TestRecordsAppleHealthXmlRepository(unittest.TestCase):

    def test_import(self):
        path = '../../../../gnome-health-data/export/apple_health_export/export_sample.xml'
        repo = RecordsAppleHealthXmlRepository(path)
        repo.load_data()

        my_info = repo.find_me()
        self.assertIsNotNone(my_info)

        my_records = repo.find_all_records()
        self.assertTrue(len(my_records) > 0)
