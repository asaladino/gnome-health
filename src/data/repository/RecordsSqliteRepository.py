import datetime

from src.data.model.Record import Record


class RecordsSqliteRepository:

    def __init__(self, session):
        self.session = session

    def find_all(self):
        """
        Find all the records in the stored.
        :return: a list of all the records.
        """
        return self.session.query(Record).all()

    def find_today(self):
        """
        Find all the records for today.
        :return: a list of records for today
        """
        today = datetime.date.today()
        return self.find_on_date(today)

    def find_on_date(self, the_date):
        """
        Find records on a given date.
        :param the_date: to look for records.
        :return: a list of records for the date.
        """
        tomorrow = the_date + datetime.timedelta(days=1)
        return self.session.query(Record). \
            filter(Record.start.between(the_date, tomorrow)). \
            all()

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
        :param record: to read
        :return: Record
        """
        return self.session.query(Record).filter_by(id=record.id).first()

    def exists(self, record: Record):
        """
        Check if the record exists by matching on all properties except id
        :param record: to find
        :return: Record
        """
        return self.session.query(Record).filter_by(type=record.type,
                                                    source_name=record.source_name,
                                                    source_version=record.source_version,
                                                    unit=record.unit,
                                                    created=record.created,
                                                    start=record.start,
                                                    end=record.end,
                                                    value=record.value).first()

    def delete(self, record: Record):
        """
        Delete a record.
        :param record: to delete
        :return: None
        """
        self.session.delete(record)
        self.session.flush()
