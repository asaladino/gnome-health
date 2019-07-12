from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, Integer
from sqlalchemy.ext.declarative import declarative_base

from src.data.model import consts

from src.data.model.Types import Gender, BloodType, SkinType

Base = declarative_base()


class Me(Base):
    __tablename__ = 'me'
    id = Column(Integer, primary_key=True)
    birth = Column(DateTime)
    biological_gender = Column(Enum(Gender))
    blood_type = Column(Enum(BloodType))
    fitzpatrick_skin_type = Column(Enum(SkinType))

    def set_birth(self, birth):
        self.birth = datetime.strptime(birth, consts.date_format)
