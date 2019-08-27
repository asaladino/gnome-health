from gi.repository import Gtk, GLib


# noinspection PyUnresolvedReferences
@Gtk.Template(resource_path='/com/codingsimply/gnome/health/add_dialog.ui')
class AddDialogController(Gtk.Dialog):
    __gtype_name__ = 'AddDialog'

    cancelButton = Gtk.Template.Child()
    saveButton = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cancelButton.connect('clicked', self.dialog_close)
        self.saveButton.connect('clicked', self.save)

    # noinspection PyUnusedLocal
    def dialog_close(self, widget):
        self.hide()

    # noinspection PyUnusedLocal
    def save(self, widget):
        self.hide()
