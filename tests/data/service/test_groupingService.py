import os
from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.data.model.Record import Base as RecordBase
from src.data.model.Me import Base as MeBase
from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository
from src.data.service.GroupingService import GroupingService


def _create_session():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_file = os.path.abspath(os.path.join(dir_path, '..', '..', '..', 'test_data', 'your_data_full.sqlite'))
    engine = create_engine('sqlite:///' + db_file, echo=False)
    session = sessionmaker(bind=engine)
    RecordBase.metadata.create_all(engine)
    MeBase.metadata.create_all(engine)
    return session()


class TestGroupingService(TestCase):

    def test_sum_groups(self):
        records_sqlite_repo = RecordsSqliteRepository(_create_session())
        records = records_sqlite_repo.find_most_recent()
        groups = GroupingService.for_records(records)
        self.assertTrue(len(groups) > 0)

    def test_sum_groups_list_store(self):
        records_sqlite_repo = RecordsSqliteRepository(_create_session())
        records = records_sqlite_repo.find_most_recent()
        groups = GroupingService.for_records_as_list_store(records)
        self.assertTrue(len(groups) > 0)
