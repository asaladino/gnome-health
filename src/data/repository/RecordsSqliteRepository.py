from src.data.model.Record import Record


class RecordsSqliteRepository:

    def __init__(self, session):
        self.session = session

    def save(self, record: Record):
        """
        Created a new record
        :param record: to create
        :return: Record
        """
        self.session.add(record)
        self.session.flush()
        return record

    def read(self, record: Record):
        """
        Get record by id
        :param record: to create
        :return: Record
        """
        return self.session.query(Record).filter_by(id=record.id).first()

    def delete(self, record: Record):
        self.session.delete(record)
        self.session.flush()
