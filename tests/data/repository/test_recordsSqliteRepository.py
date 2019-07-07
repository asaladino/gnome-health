from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.data.model.Record import Record, Base
from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository


def _create_session():
    engine = create_engine('sqlite:///:memory:', echo=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return session()


class TestRecordsSqliteRepository(TestCase):

    def test_create(self):
        repo = RecordsSqliteRepository(_create_session())
        record = Record(source_name="Testing")
        saved_record = repo.save(record)
        self.assertTrue(saved_record.id > 0)

    def test_read(self):
        repo = RecordsSqliteRepository(_create_session())
        record = Record(source_name="Testing")
        saved_record = repo.save(record)
        got_record = repo.read(saved_record)
        self.assertEqual(got_record.id, saved_record.id)

    def test_update(self):
        repo = RecordsSqliteRepository(_create_session())
        record = Record(source_name="Testing")
        saved_record = repo.save(record)

        saved_record.source_name = "Update Testing"
        repo.save(saved_record)

        got_record_2 = repo.read(saved_record)
        self.assertEqual(record.source_name, got_record_2.source_name)

    def test_delete(self):
        repo = RecordsSqliteRepository(_create_session())
        record = Record(source_name="Testing")
        record = repo.save(record)
        repo.delete(record)
        got_record = repo.read(record)

        self.assertIsNone(got_record)
