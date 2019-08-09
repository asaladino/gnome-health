import datetime
import os
from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.data.model.Record import Base as RecordBase
from src.data.model.Me import Base as MeBase

from src.data.model.Record import Record, Base
from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository


def _create_session():
    engine = create_engine('sqlite:///:memory:', echo=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return session()


def _create_session_from_file():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_file = os.path.abspath(os.path.join(dir_path, '..', '..', '..', 'test_data', 'your_data_full.sqlite'))
    engine = create_engine('sqlite:///' + db_file, echo=False)
    session = sessionmaker(bind=engine)
    RecordBase.metadata.create_all(engine)
    MeBase.metadata.create_all(engine)
    return session()


class TestRecordsSqliteRepository(TestCase):

    def test_create(self):
        repo = RecordsSqliteRepository(_create_session())
        record = Record(source_name="Testing")
        saved_record = repo.save(record)
        self.assertTrue(saved_record.id > 0)

    def test_find_today(self):
        repo = RecordsSqliteRepository(_create_session())
        for index in range(10):
            record = Record(source_name="Testing " + str(index))
            record.start = datetime.datetime.today() + datetime.timedelta(days=index - 5)
            repo.save(record)

        records = repo.find_today()
        self.assertTrue(len(records) > 0)

    def test_find_most_recent(self):
        repo = RecordsSqliteRepository(_create_session_from_file())
        records = repo.find_most_recent()
        self.assertTrue(len(records) > 0)

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

    def test_last_id(self):
        repo = RecordsSqliteRepository(_create_session())
        last = 10
        for i in range(last):
            record = Record(source_name="Testing " + str(i))
            repo.save(record)
        last_id = repo.last_id()
        self.assertEqual(last, last_id)

    def test_delete(self):
        repo = RecordsSqliteRepository(_create_session())
        record = Record(source_name="Testing")
        record = repo.save(record)
        repo.delete(record)
        got_record = repo.read(record)

        self.assertIsNone(got_record)
