from datetime import datetime

from src.data.model import consts


class Record:
    type = str
    source_name = str
    source_version = str
    unit = str
    created = datetime
    start = datetime
    end = datetime
    value = int

    def copy_from_object(self, obj):
        for att in obj.__dict__:
            self.__setattr__(att, obj.__getattribute__(att))

    def set_created(self, start):
        self.created = datetime.strptime(start, consts.date_time_format)

    def set_start(self, start):
        self.start = datetime.strptime(start, consts.date_time_format)

    def set_end(self, start):
        self.end = datetime.strptime(start, consts.date_time_format)
