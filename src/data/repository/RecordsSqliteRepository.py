from pony.orm import Database, PrimaryKey, db_session, commit

from src.data.model.Record import Record as RecordModel

db = Database()
db.bind(provider='sqlite', filename=':memory:')


class Record(RecordModel, db.Entity):
    id = PrimaryKey(int, auto=True)


db.generate_mapping(create_tables=True)


class RecordsSqliteRepository:

    @staticmethod
    @db_session
    def create(record: RecordModel):
        record_sql = Record()
        record_sql.copy_from_object(record)
        commit()
        return record_sql

    @staticmethod
    @db_session
    def read(record_id):
        return Record[record_id]

    @staticmethod
    @db_session
    def update(self):
        pass

    @staticmethod
    @db_session
    def delete(self):
        pass
