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
        progress(1, 1, 'Saved me info')

        records_to_import = apple_health_xml_repo.find_all_records()
        progress(-1, len(records_to_import), 'Importing records')
        records_that_were_imported = 0
        for index, r in enumerate(records_to_import):
            if records_sqlite_repo.exists(r) is None:
                records_sqlite_repo.save(r)
                records_that_were_imported += 1
                progress(index, len(records_to_import), 'Saved record')

        return me is not None, len(records_to_import), records_that_were_imported
