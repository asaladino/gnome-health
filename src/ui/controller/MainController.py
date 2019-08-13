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

from gi.repository import Gtk

from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository
from src.ui.controller.ImportDialogController import ImportDialogController
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

    appCloseButton = Gtk.Template.Child()
    importButton = Gtk.Template.Child()

    importDialog = None

    dbSession = create_session()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.calendar.connect('day-selected', self.change_selected_day)
        self.appCloseButton.connect('clicked', self.app_close)
        self.importButton.connect('clicked', self.import_dialog_open)
        self.change_selected_day(self.calendar)
        self.load_most_recent_records()

    def load_most_recent_records(self):
        most_recent_thread = threading.Thread(target=self.load_most_recent_records_async, args=())
        most_recent_thread.daemon = True
        most_recent_thread.start()

    def load_most_recent_records_async(self):
        records_sqlite_repo = RecordsSqliteRepository(self.dbSession)
        records = records_sqlite_repo.find_most_recent()
        for record in records:
            print(record)

    def change_selected_day(self, widget):
        the_date = widget.get_date()
        self.selectedDate = datetime.date(year=the_date.year, month=the_date.month, day=the_date.day)
        self.show_date()
        self.calendarPopover.popdown()

    def show_date(self):
        self.headerBar.set_subtitle(self.selectedDate.strftime('%b %d, %Y'))

    # noinspection PyUnusedLocal
    def import_dialog_open(self, widget):
        if self.importDialog is None:
            self.importDialog = ImportDialogController()
        self.importDialog.show()

    # noinspection PyUnusedLocal
    @staticmethod
    def app_close(widget):
        Gtk.main_quit()