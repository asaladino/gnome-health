from gi.overrides import Gtk

from src.data.model import consts
from src.data.model.RecordGroup import RecordGroup
from src.data.model.Types import QuantityTypeInfo, CalcType


class GroupingService:

    @staticmethod
    def for_records(records):
        """
        Group a bunch of records together and sum them.
        :param records: to group
        :return: a dictionary of groups
        """
        groups = dict()
        for record in records:
            try:
                groups[record.type]
            except KeyError:
                groups[record.type] = RecordGroup()
                groups[record.type].unit = record.unit
                groups[record.type].type = record.type
                groups[record.type].end = record.end
                groups[record.type].records = []
                try:
                    groups[record.type].name = QuantityTypeInfo.info[record.type]['name']
                    groups[record.type].description = QuantityTypeInfo.info[record.type]['description']
                except KeyError:
                    groups[record.type].name = str(record.type.name).replace('_', ' ').lower().title()
                    groups[record.type].description = "Missing type info: description " + str(record.type.name)

            groups[record.type].total += record.value
            groups[record.type].records.append(record)

        # Handle aggregate operations on groups
        for record_type in groups:
            calc_type = CalcType.SUM
            try:
                calc_type = QuantityTypeInfo.info[record_type]['calc']
            except KeyError:
                pass
            if calc_type == CalcType.AVERAGE and len(groups[record_type].records) > 0:
                groups[record_type].total = groups[record_type].total / len(groups[record_type].records)

        return groups

    @staticmethod
    def for_records_as_list_store(records):
        groups: [RecordGroup] = GroupingService.for_records(records)
        store = Gtk.ListStore(str, float, str, int, str)
        for key in groups:
            group = groups[key]  # type: RecordGroup
            store.append(
                [group.name, group.total, group.unit, group.type.value, group.end.strftime(consts.date_display_format)])
        return store
