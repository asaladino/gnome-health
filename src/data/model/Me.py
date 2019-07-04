from datetime import datetime

from src.data.model import consts

from src.data.model.Gender import Gender


class Me:
    def __init__(self):
        self.birth = None
        self.biological_gender = Gender.OTHER
        self.blood_type = None
        self.fitzpatrick_skin_type = None

    def set_birth(self, birth):
        self.birth = datetime.strptime(birth, consts.date_format)
