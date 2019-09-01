import datetime

from gi.repository import Gtk, GLib

# noinspection PyUnresolvedReferences-
from src.data.model import Types
from src.data.model.Record import Record
from src.data.model.Types import QuantityTypeInfo, QuantityType
from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository
from src.utility.DbSession import create_session


@Gtk.Template(resource_path='/com/codingsimply/gnome/health/add_dialog.ui')
class AddDialogController(Gtk.Dialog):
    __gtype_name__ = 'AddDialog'

    cancelButton: Gtk.Button = Gtk.Template.Child()
    saveButton: Gtk.Button = Gtk.Template.Child()

    recordTypeComboBox: Gtk.ComboBox = Gtk.Template.Child()
    valueEntry: Gtk.Entry = Gtk.Template.Child()
    unitsEntry: Gtk.Entry = Gtk.Template.Child()
    dateCalendar: Gtk.Calendar = Gtk.Template.Child()

    selected_type: QuantityType = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cancelButton.connect('clicked', self.dialog_close)
        self.saveButton.connect('clicked', self.save)

        name_store = Gtk.ListStore(int, str)
        for qt in QuantityType:
            name_store.append([qt.value, QuantityTypeInfo.info[qt]['name']])

        self.recordTypeComboBox.set_model(name_store)
        self.recordTypeComboBox.connect("changed", self.on_name_combo_changed)
        self.recordTypeComboBox.set_entry_text_column(1)

    def on_name_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            self.selected_type, name = model[tree_iter][:2]
        # else:
        #     entry = combo.get_child()
        #     print("Entered: %s" % entry.get_text())

    # noinspection PyUnusedLocal
    def dialog_close(self, widget):
        self.hide()

    # noinspection PyUnusedLocal
    def save(self, widget):
        record = Record()
        for qt in QuantityType:
            if qt.value == self.selected_type:
                record.type = qt
                break
        record.value = float(self.valueEntry.get_text())
        record.unit = self.unitsEntry.get_text()
        the_date = self.dateCalendar.get_date()
        record.created = datetime.date(year=the_date.year, month=the_date.month + 1, day=the_date.day)
        with RecordsSqliteRepository(create_session()) as repo:
            r = repo.save(record)
            print(r)
        self.hide()
