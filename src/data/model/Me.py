from datetime import datetime

from src.data.model import consts

from src.data.model.Gender import Gender


class Me:
    birth = None
    biological_gender = Gender.OTHER
    blood_type = None
    fitzpatrick_skin_type = None

    def set_birth(self, birth):
        self.birth = datetime.strptime(birth, consts.date_format)
