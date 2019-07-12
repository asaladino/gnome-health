import datetime
from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.data.model.Me import Me, Base
from src.data.model.Types import Gender, BloodType, SkinType
from src.data.repository.MeSqliteRepository import MeSqliteRepository


def _create_session():
    engine = create_engine('sqlite:///:memory:', echo=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return session()


class TestMeSqliteRepository(TestCase):

    def test_create(self):
        repo = MeSqliteRepository(_create_session())
        me = repo.read()
        me.birth = datetime.datetime.today()
        me.biological_gender = Gender.MALE
        me.blood_type = BloodType.A_NEGATIVE
        me.fitzpatrick_skin_type = SkinType.TYPE_IV
        me_saved = repo.save(me)
        self.assertTrue(me_saved.id == 1)

    def test_read(self):
        repo = MeSqliteRepository(_create_session())
        me_saved = repo.read()
        self.assertTrue(me_saved.id == 1)
        me_saved = repo.read()
        self.assertTrue(me_saved.id == 1)
        me_saved = repo.read()
        self.assertTrue(me_saved.id == 1)
        me_saved = repo.read()
        self.assertTrue(me_saved.id == 1)
