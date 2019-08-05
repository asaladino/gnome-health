# MainController.py
#
# Copyright 2019 Adam Saladino
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import datetime
import threading
import time

from gi.repository import Gtk

from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository
from src.data.service.ImportService import ImportService
from src.utility.DbSession import create_session


@Gtk.Template(resource_path='/com/codingsimply/gnome/health/window.ui')
class MainController(Gtk.ApplicationWindow):
    __gtype_name__ = 'GnomeHealthWindow'

    dateTimeButton = Gtk.Template.Child()
    calendar = Gtk.Template.Child()
    calendarPopover = Gtk.Template.Child()
    healthTypesListBox = Gtk.Template.Child()
    headerBar = Gtk.Template.Child()

    selectedDate = datetime.date.today()

    importDialog = Gtk.Template.Child()
    appCloseButton = Gtk.Template.Child()
    importButton = Gtk.Template.Child()
    cancelImportButton = Gtk.Template.Child()
    importFileChooserButton = Gtk.Template.Child()
    runImportButton = Gtk.Template.Child()
    importProgressBar = Gtk.Template.Child()
    loadingSpinner = Gtk.Template.Child()

    dbSession = create_session()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.calendar.connect('day-selected', self.change_selected_day)
        self.appCloseButton.connect('clicked', self.app_close)
        self.importButton.connect('clicked', self.import_dialog_open)
        self.cancelImportButton.connect('clicked', self.import_dialog_close)
        self.runImportButton.connect('clicked', self.run_import)
        self.change_selected_day(self.calendar)

    def change_selected_day(self, widget):
        the_date = widget.get_date()
        self.selectedDate = datetime.date(year=the_date.year, month=the_date.month, day=the_date.day)
        self.show_date()
        self.calendarPopover.popdown()

    def show_date(self):
        self.headerBar.set_subtitle(self.selectedDate.strftime('%b %d, %Y'))

    # noinspection PyUnusedLocal
    def import_dialog_open(self, widget):
        self.importDialog.show()

    # noinspection PyUnusedLocal
    def run_import(self, widget):
        files = self.importFileChooserButton.get_files()
        self.loadingSpinner.activate()
        self.loadingSpinner.start()
        if len(files) > 0:
            path = files[0].get_path()
            import_thread = threading.Thread(target=self.async_import, args=(path,))
            import_thread.start()
        else:
            self.importDialog.hide()

    def async_import(self, path):
        import_service = ImportService(self.dbSession)
        import_service.apple_import(path, self.update_progress)
        self.importProgressBar.set_fraction(0.0)
        self.importDialog.hide()

    def update_progress(self, progress, total, message):
        print(progress, total, message)
        if progress == -2:
            self.loadingSpinner.stop()

        if progress > 0:
            self.importProgressBar.set_fraction(progress / total)

    # noinspection PyUnusedLocal
    def import_dialog_close(self, widget):
        self.importDialog.hide()

    # noinspection PyUnusedLocal
    @staticmethod
    def app_close(widget):
        Gtk.main_quit()