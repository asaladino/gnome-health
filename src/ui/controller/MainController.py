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

from gi.repository import Gtk, GLib, GObject

from src.data.model.RecordGroup import RecordGroup
from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository
from src.data.service.GroupingService import GroupingService
from src.ui.controller.ImportDialogController import ImportDialogController
from src.utility.DbSession import create_session, create_session_2


@Gtk.Template(resource_path='/com/codingsimply/gnome/health/window.ui')
class MainController(Gtk.ApplicationWindow):
    __gtype_name__ = 'GnomeHealthWindow'

    dateTimeButton = Gtk.Template.Child()
    calendar = Gtk.Template.Child()
    calendarPopover = Gtk.Template.Child()
    headerBar = Gtk.Template.Child()
    groupsScrolledWindow = Gtk.Template.Child()
    healthTypesListBox = Gtk.Template.Child()

    selectedDate = datetime.date.today()

    prevDayButton = Gtk.Template.Child()
    todayButton = Gtk.Template.Child()
    mostRecentButton = Gtk.Template.Child()
    nextDayButton = Gtk.Template.Child()

    appCloseButton = Gtk.Template.Child()
    importButton = Gtk.Template.Child()

    importDialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db_session = create_session_2()
        records_sqlite_repo = RecordsSqliteRepository(db_session())
        self.selectedDate = records_sqlite_repo.find_most_recent_date()
        db_session.remove()
        self.calendar.select_month(self.selectedDate.month, self.selectedDate.year)

        self.calendar.connect('day-selected', self.change_selected_day)
        self.appCloseButton.connect('clicked', self.app_close)
        self.importButton.connect('clicked', self.import_dialog_open)

        self.prevDayButton.connect('clicked', self.prev_day)
        self.nextDayButton.connect('clicked', self.next_day)

        self.calendar.select_day(self.selectedDate.day)

    def prev_day(self, widget):
        the_date = self.selectedDate + datetime.timedelta(days=-1)
        self.set_selected_day(the_date)

    def next_day(self, widget):
        the_date = self.selectedDate + datetime.timedelta(days=1)
        self.set_selected_day(the_date)

    def load_records(self):
        most_recent_thread = threading.Thread(target=self.load_records_async, args=())
        most_recent_thread.daemon = True
        most_recent_thread.start()

    def load_records_async(self):
        db_session = create_session_2()
        records_sqlite_repo = RecordsSqliteRepository(db_session())
        records = records_sqlite_repo.find_on_date(self.selectedDate)
        db_session.remove()
        groups = GroupingService.for_records(records)
        GLib.idle_add(self.display_most_recent_records, groups)

    def display_most_recent_records(self, groups):
        for child in self.healthTypesListBox.get_children():
            self.healthTypesListBox.remove(child)

        for record_type in groups:
            group = groups[record_type]  # type: RecordGroup
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            row.add(hbox)
            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            hbox.pack_start(vbox, True, True, 5)

            label1 = Gtk.Label(group.name, xalign=0)
            label2 = Gtk.Label(str(group.total) + ' ' + group.unit, xalign=0)
            vbox.pack_start(label1, True, True, 5)
            vbox.pack_start(label2, True, True, 5)
            self.healthTypesListBox.add(row)

        self.healthTypesListBox.show_all()

    def change_selected_day(self, widget):
        the_date = widget.get_date()
        self.set_selected_day(the_date)

    def set_selected_day(self, the_date):
        self.selectedDate = datetime.date(year=the_date.year, month=the_date.month, day=the_date.day)
        self.show_date()
        self.calendarPopover.popdown()
        self.load_records()

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
