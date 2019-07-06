from unittest import TestCase

from src.data.model.Record import Record
from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository


class TestRecordsSqliteRepository(TestCase):
    def test_create(self):
        record = Record()
        record.source_name = "Testing"
        saved_record = RecordsSqliteRepository.create(record)
        self.assertTrue(saved_record.id > 0)

    def test_read(self):
        record = Record()
        record.source_name = "Testing"
        saved_record = RecordsSqliteRepository.create(record)
        got_record = RecordsSqliteRepository.read(saved_record.id)
        self.assertEqual(got_record.id, saved_record.id)

    def test_update(self):
        self.fail()

    def test_delete(self):
        self.fail()
