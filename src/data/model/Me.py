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

    def update(self, me_updated):
        """
        Update the properties of me.
        :param me_updated:
        :return: None
        """
        self.birth = me_updated.birth
        self.biological_gender = me_updated.biological_gender
        self.blood_type = me_updated.blood_type
        self.fitzpatrick_skin_type = me_updated.fitzpatrick_skin_type