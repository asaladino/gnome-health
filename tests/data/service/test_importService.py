import os
from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.data.model.Record import Base as RecordBase
from src.data.model.Me import Base as MeBase
from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository
from src.data.service.ImportService import ImportService


def _create_session():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_file = os.path.abspath(os.path.join(dir_path, '..', '..', '..', 'test_data', 'your_data_full.sqlite'))
    engine = create_engine('sqlite:///' + db_file, echo=False)
    # engine = create_engine('sqlite:///:memory:', echo=True)
    session = sessionmaker(bind=engine)
    RecordBase.metadata.create_all(engine)
    MeBase.metadata.create_all(engine)
    return session()


class TestImportService(TestCase):

    def test_apple_import(self):
        session = _create_session()
        records_sqlite_repo = RecordsSqliteRepository(session)

        path = '../../../../gnome-health-data/export/apple_health_export/export.xml'
        import_service = ImportService(session)
        # (found_me, records_found, records_that_were_imported) = import_service.apple_import(path)
        (found_me, records_found, records_that_were_imported) = import_service.apple_import(path, self.report_progress)
        session.commit()
        print(found_me, records_found, records_that_were_imported)
        records_imported = records_sqlite_repo.find_all()
        self.assertEqual(len(records_imported), records_found)

    @staticmethod
    def report_progress(progress, total, message):
        if progress % 100 == 0 or progress < 0:
            print(progress, total, message)
