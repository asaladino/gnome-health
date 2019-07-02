from datetime import datetime

from src.data.model import consts


class Record:
    def __init__(self):
        self.type = ''
        self.source_name = ''
        self.source_version = ''
        self.unit = ''
        self.created = None
        self.start = None
        self.end = None
        self.value = 0

    def set_created(self, start):
        self.created = datetime.strptime(start, consts.date_time_format)

    def set_start(self, start):
        self.start = datetime.strptime(start, consts.date_time_format)

    def set_end(self, start):
        self.end = datetime.strptime(start, consts.date_time_format)
