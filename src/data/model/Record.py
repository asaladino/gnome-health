from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base

from src.data.model import consts

from sqlalchemy import Column, Integer, String, Float, DateTime, Enum

from src.data.model.Types import QuantityType

Base = declarative_base()


class Record(Base):
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(QuantityType))
    source_name = Column(String)
    source_version = Column(String)
    unit = Column(String)
    created = Column(DateTime)
    start = Column(DateTime)
    end = Column(DateTime)
    value = Column(Float)

    def __repr__(self):
        return "<Record(source_name='%s')>" % self.source_name

    def copy_from_object(self, obj):
        for att in obj.__dict__:
            self.__setattr__(att, obj.__getattribute__(att))

    def set_created(self, start):
        self.created = datetime.strptime(start, consts.date_time_format)

    def set_start(self, start):
        self.start = datetime.strptime(start, consts.date_time_format)

    def set_end(self, start):
        self.end = datetime.strptime(start, consts.date_time_format)
