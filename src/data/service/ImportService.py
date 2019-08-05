from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from src.data.repository.MeSqliteRepository import MeSqliteRepository
from src.data.repository.RecordsAppleHealthXmlRepository import RecordsAppleHealthXmlRepository
from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository


class ImportService:
    """
    Service for importing data from other sources.
    """
    session: sessionmaker

    def __init__(self, session):
        """
        Need to init with a db session
        :param session: sqlalchemy db session.
        """
        self.session = session

    def apple_import(self, path, progress=lambda progress, total, message: None):
        """
        Import an apple health export xml file.
        :param path: to the xml file.
        :param progress: keep tabs on the import progress.
        :return: a tuple of import results.
        """
        me_sqlite_repo = MeSqliteRepository(self.session)
        records_sqlite_repo = RecordsSqliteRepository(self.session)

        # Load the xml to save.
        apple_health_xml_repo = RecordsAppleHealthXmlRepository(path)
        apple_health_xml_repo.load_data()

        # Update me information.
        me_updated = apple_health_xml_repo.find_me()
        me = me_sqlite_repo.read()
        me.update(me_updated)
        me_sqlite_repo.save(me)
        progress(-1, 0, 'Saved me info')

        last_id = records_sqlite_repo.last_id()
        if last_id is None:
            last_id = 0

        progress(-1, 0, 'Loading records')
        records_to_import = apple_health_xml_repo.find_all_records(last_id)
        progress(-1, len(records_to_import), 'Importing records')
        records_that_were_imported = 0
        records_to_save = []
        index = 0
        for h, r in records_to_import.items():
            progress(index, len(records_to_import), 'Checking record')
            index += 1
            if records_sqlite_repo.exists_by_hash(r) is None:
                records_to_save.append(r)

        progress(-1, len(records_to_save), 'Saving records')
        records_sqlite_repo.save_all(records_to_save)

        return me is not None, len(records_to_import), records_that_were_imported
