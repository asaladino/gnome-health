from gi.repository import Gtk, GLib

# noinspection PyUnresolvedReferences-
from src.data.model import Types
from src.data.model.Types import QuantityTypeInfo


@Gtk.Template(resource_path='/com/codingsimply/gnome/health/add_dialog.ui')
class AddDialogController(Gtk.Dialog):
    __gtype_name__ = 'AddDialog'

    cancelButton: Gtk.Button = Gtk.Template.Child()
    saveButton: Gtk.Button = Gtk.Template.Child()

    recordTypeComboBox: Gtk.ComboBox = Gtk.Template.Child()
    valueEntry: Gtk.Entry = Gtk.Template.Child()
    unitsEntry: Gtk.Entry = Gtk.Template.Child()
    dateCalendar: Gtk.Calendar = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cancelButton.connect('clicked', self.dialog_close)
        self.saveButton.connect('clicked', self.save)

        name_store = Gtk.ListStore(int, str)
        for qt in Types.QuantityType:
            name_store.append([qt.value, QuantityTypeInfo.info[qt]['name']])

        self.recordTypeComboBox.set_model(name_store)
        renderer_text = Gtk.CellRendererText()
        self.recordTypeComboBox.connect("changed", self.on_name_combo_changed)
        self.recordTypeComboBox.set_entry_text_column(1)

    def on_name_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            row_id, name = model[tree_iter][:2]
            print("Selected: ID=%d, name=%s" % (row_id, name))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())

    # noinspection PyUnusedLocal
    def dialog_close(self, widget):
        self.hide()

    # noinspection PyUnusedLocal
    def save(self, widget):
        self.hide()
