from unittest import TestCase

from src.data.model.Record import Record
from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository


class TestRecordsSqliteRepository(TestCase):
    def test_create(self):
        repo = RecordsSqliteRepository()
        record = Record()
        record.source_name = "Testing"
        repo.create(record)
        self.fail()

    def test_read(self):
        self.fail()

    def test_update(self):
        self.fail()

    def test_delete(self):
        self.fail()
