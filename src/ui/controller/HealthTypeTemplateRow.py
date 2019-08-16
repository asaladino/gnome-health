from gi.repository import Gtk

from src.data.model.RecordGroup import RecordGroup


# noinspection PyUnresolvedReferences
@Gtk.Template(resource_path='/com/codingsimply/gnome/health/health_type_template_row.ui')
class HealthTypeTemplateRow(Gtk.ListBoxRow):
    __gtype_name__ = 'HealthTypeTemplateRow'

    healthTypeNameLabel = Gtk.Template.Child()
    healthTypeTotalLabel = Gtk.Template.Child()
    healthTypeUnitLabel = Gtk.Template.Child()
    healthTypeDateLabel = Gtk.Template.Child()

    def set_group(self, group: RecordGroup):
        self.healthTypeNameLabel.set_text(group.name)
        decimal = ".0f"
        if group.total < 10:
            decimal = ".1f"
        if group.total < 1:
            decimal = ".2f"
        self.healthTypeTotalLabel.set_text(f"{group.total:,{decimal}}")
        self.healthTypeUnitLabel.set_text(group.unit)
        self.healthTypeDateLabel.set_text(group.end.strftime('%b %d, %Y %H:%M'))
