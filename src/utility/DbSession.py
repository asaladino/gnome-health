import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.data.model.Record import Base as RecordBase
from src.data.model.Me import Base as MeBase


def create_session():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_file = os.path.abspath(os.path.join(dir_path, '..', '..', 'test_data', 'your_data.sqlite'))
    engine = create_engine('sqlite:///' + db_file, echo=False)
    session = sessionmaker(bind=engine)
    RecordBase.metadata.create_all(engine)
    MeBase.metadata.create_all(engine)
    return session()
