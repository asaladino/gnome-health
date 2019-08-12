from gi.repository import Gtk, GLib
import threading
from src.data.service.ImportService import ImportService
from src.utility.DbSession import create_session


@Gtk.Template(resource_path='/com/codingsimply/gnome/health/import_dialog.ui')
class ImportDialogController(Gtk.Dialog):
    __gtype_name__ = 'ImportDialog'

    cancelImportButton = Gtk.Template.Child()
    importFileChooserButton = Gtk.Template.Child()
    runImportButton = Gtk.Template.Child()
    importProgressBar = Gtk.Template.Child()
    loadingSpinner = Gtk.Template.Child()

    importFinishedEvent = threading.Event()

    importThread = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cancelImportButton.connect('clicked', self.import_dialog_close)
        self.runImportButton.connect('clicked', self.run_import)
        self.loadingSpinner.activate()

    # noinspection PyUnusedLocal
    def import_dialog_close(self, widget):
        self.hide()

    # noinspection PyUnusedLocal
    def run_import(self, widget):
        files = self.importFileChooserButton.get_files()
        if len(files) > 0:
            self.ui_start_import()

            path = files[0].get_path()
            self.importThread = threading.Thread(target=self.async_import, args=(path,))
            self.importThread.daemon = True
            self.importThread.start()
        else:
            self.hide()

    def async_import(self, path):

        import_service = ImportService(create_session())
        import_service.apple_import(path, lambda progress, total, message: GLib.idle_add(self.update_progress, progress, total, message))

        GLib.idle_add(self.ui_reset_import)
        GLib.idle_add(self.hide)

    def ui_start_import(self):
        self.loadingSpinner.start()
        self.runImportButton.set_sensitive(False)
        self.cancelImportButton.set_sensitive(False)

        self.importProgressBar.set_show_text(True)

    def ui_reset_import(self):
        self.loadingSpinner.stop()
        self.runImportButton.set_sensitive(True)
        self.cancelImportButton.set_sensitive(True)

        self.importProgressBar.set_fraction(0.0)
        self.importProgressBar.set_show_text("")

    def update_progress(self, progress, total, message):
        if progress == -1:
            self.loadingSpinner.start()
            self.importProgressBar.set_text(message)

        if progress > 0:
            self.loadingSpinner.stop()
            self.importProgressBar.set_fraction(progress / total)
