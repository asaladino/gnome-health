from datetime import datetime

from src.data.model import consts

from src.data.model.Types import Gender, BloodType


class Me:
    birth = None
    biological_gender = Gender.NOT_SET
    blood_type = BloodType.NOT_SET
    fitzpatrick_skin_type = None

    def set_birth(self, birth):
        self.birth = datetime.strptime(birth, consts.date_format)
