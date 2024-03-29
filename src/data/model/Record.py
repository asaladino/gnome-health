import hashlib
from datetime import datetime

from sqlalchemy import Column, String, Float, DateTime, Enum, Integer
from sqlalchemy.ext.declarative import declarative_base

from src.data.model import consts
from src.data.model.Types import QuantityType

Base = declarative_base()


class Record(Base):
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    hash = Column(String, unique=True)
    type = Column(Enum(QuantityType))
    source_name = Column(String)
    source_version = Column(String)
    unit = Column(String)
    created = Column(DateTime)
    start = Column(DateTime)
    end = Column(DateTime)
    value = Column(Float)

    def __repr__(self):
        return "<Record(type='%s', value='%d' unit='%s')>" % (self.type, self.value, self.unit)

    def set_hash(self):
        props_to_use = [self.type if self.type is not None else '',
                        self.source_name if self.source_name is not None else '',
                        self.source_version if self.source_version is not None else '',
                        self.unit if self.unit is not None else '',
                        datetime.timestamp(self.created) if self.created is not None else '',
                        datetime.timestamp(self.start) if self.start is not None else '',
                        datetime.timestamp(self.end) if self.end is not None else '',
                        self.value if self.value is not None else '']
        hash_value = ''.join(str(x) for x in props_to_use).encode()
        self.hash = hashlib.sha3_224(hash_value).hexdigest()

    @staticmethod
    def build(quantity_type, value, unit, the_date):
        record = Record()
        record.value = value
        record.type = quantity_type
        record.unit = unit
        record.created = datetime(year=the_date.year, month=the_date.month + 1, day=the_date.day)
        record.start = datetime(year=the_date.year, month=the_date.month + 1, day=the_date.day)
        record.end = datetime(year=the_date.year, month=the_date.month + 1, day=the_date.day)
        record.source_name = 'Health'
        record.source_version = '1.0.0'
        record.set_hash()
        return record

    @staticmethod
    def build_from_dict(record_dict):
        record = Record()
        if 'value' in record_dict:
            record.value = record_dict['value']
        if 'type' in record_dict:
            record.type = QuantityType.find(record_dict['type'])
        if 'unit' in record_dict:
            record.unit = record_dict['unit']

        if 'created' in record_dict:
            record.set_created(record_dict['created'])
        else:
            record.created = datetime.now()

        if 'start' in record_dict:
            record.set_start(record_dict['start'])
        else:
            record.start = datetime.now()

        if 'end' in record_dict:
            record.set_end(record_dict['end'])
        else:
            record.end = datetime.now()

        if 'source_name' in record_dict:
            record.source_name = record_dict['source_name']
        if 'source_version' in record_dict:
            record.source_version = record_dict['source_version']
        record.set_hash()
        return record

    def copy_from_object(self, obj):
        for att in obj.__dict__:
            self.__setattr__(att, obj.__getattribute__(att))

    def set_created(self, start):
        self.created = datetime.strptime(start, consts.date_time_format)

    def set_start(self, start):
        self.start = datetime.strptime(start, consts.date_time_format)

    def set_end(self, start):
        self.end = datetime.strptime(start, consts.date_time_format)
