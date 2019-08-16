class RecordGroup:
    total = 0
    unit = ''
    type = None
    name = None
    description = None
    end = None
    records = []

    def __repr__(self):
        return "<Group(type='%s', value='%d' unit='%s')>" % (self.type, self.total, self.unit)
