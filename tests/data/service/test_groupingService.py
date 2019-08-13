import os
from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.data.model.Record import Base as RecordBase
from src.data.model.Me import Base as MeBase
from src.data.model.Types import QuantityType, QuantityTypeInfo
from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository


def _create_session():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_file = os.path.abspath(os.path.join(dir_path, '..', '..', '..', 'test_data', 'your_data_full.sqlite'))
    engine = create_engine('sqlite:///' + db_file, echo=False)
    session = sessionmaker(bind=engine)
    RecordBase.metadata.create_all(engine)
    MeBase.metadata.create_all(engine)
    return session()


class Group:
    total = 0
    unit = ''
    type = None
    name = None
    description = None
    end = None

    def __repr__(self):
        return "<Group(type='%s', value='%d' unit='%s')>" % (self.type, self.total, self.unit)


class TestGroupingService(TestCase):

    def test_sum_groups(self):
        records_sqlite_repo = RecordsSqliteRepository(_create_session())
        records = records_sqlite_repo.find_most_recent()

        groups = dict()

        for record in records:
            try:
                groups[record.type]
            except KeyError:
                groups[record.type] = Group()
                groups[record.type].unit = record.unit
                groups[record.type].type = record.type
                groups[record.type].end = record.end
                groups[record.type].name = QuantityTypeInfo.info[record.type]['name']
                groups[record.type].description = QuantityTypeInfo.info[record.type]['description']

            groups[record.type].total += record.value

        for key in groups:
            print(groups[key].name)
            print(groups[key].end)
            print(groups[key].total)