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

    def find_most_recent(self):
        """
        Find the most recent results.
        :return: results or None
        """
        record = self.session.query(Record).order_by(Record.created.desc()).first()
        if record is not None:
            the_date = record.created.date()
            tomorrow = the_date + datetime.timedelta(days=1)
            return self.session.query(Record).filter(Record.start.between(the_date, tomorrow)).all()
        return None

    def save(self, record: Record):
        """
        Created a new record
        :param record: to create
        :return: Record
        """
        self.session.add(record)
        self.session.flush()
        return record

    def save_all(self, records: [Record]):
        """
        Save all but they will need an id. Use, last_id and iterate off of it.
        :param records: to save.
        :return: None
        """
        self.session.bulk_save_objects(records)
        self.session.commit()
        self.session.flush()

    def last_id(self):
        """
        Get the last id used.
        :return: the last id or None
        """
        result = self.session.query(Record).order_by(Record.id.desc()).first()
        if result is not None:
            return result.id
        return None

    def read(self, record: Record):
        """
        Get record by id
        :param record: to read
        :return: Record
        """
        return self.session.query(Record).filter_by(id=record.id).first()

    def exists_by_hash(self, record: Record):
        """
        Check if the record exists by matching on all properties except hash
        :param record: to find
        :return: Record
        """
        return self.session.query(Record).filter_by(hash=record.hash).first()

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
