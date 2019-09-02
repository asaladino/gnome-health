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

from gi.repository import Gtk, GLib

from src.data.repository.RecordsSqliteRepository import RecordsSqliteRepository
from src.data.service.GroupingService import GroupingService
from src.ui.controller.HealthTypeTemplateRow import HealthTypeTemplateRow
from src.ui.controller.ImportDialogController import ImportDialogController
from src.ui.controller.AddDialogController import AddDialogController
from src.utility.DbSession import create_session


# noinspection PyUnresolvedReferences
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
    addButton = Gtk.Template.Child()

    importDialog = None
    addDialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.calendar.connect('day-selected', self.change_selected_day)
        self.appCloseButton.connect('clicked', self.app_close)
        self.importButton.connect('clicked', self.import_dialog_open)
        self.addButton.connect('clicked', self.add_dialog_open)

        self.prevDayButton.connect('clicked', self.prev_day)
        self.todayButton.connect('clicked', self.today)
        self.mostRecentButton.connect('clicked', self.most_recent)
        self.nextDayButton.connect('clicked', self.next_day)

        with RecordsSqliteRepository(create_session()) as repo:
            most_recent_date = repo.find_most_recent_date()
            if most_recent_date is not None:
                self.selectedDate = most_recent_date

        self.calendar.select_month(self.selectedDate.month - 1, self.selectedDate.year)
        self.calendar.select_day(self.selectedDate.day)

    def prev_day(self, _):
        the_date = self.selectedDate + datetime.timedelta(days=-1)
        self.calendar.select_month(the_date.month - 1, the_date.year)
        self.calendar.select_day(the_date.day)

    def most_recent(self, _):
        with RecordsSqliteRepository(create_session()) as repo:
            the_date = repo.find_most_recent_date()
        if the_date is not None:
            self.calendar.select_month(the_date.month - 1, the_date.year)
            self.calendar.select_day(the_date.day)

    def today(self, _):
        the_date = datetime.datetime.now()
        self.calendar.select_month(the_date.month - 1, the_date.year)
        self.calendar.select_day(the_date.day)

    def next_day(self, _):
        the_date = self.selectedDate + datetime.timedelta(days=1)
        self.calendar.select_month(the_date.month - 1, the_date.year)
        self.calendar.select_day(the_date.day)

    def load_records(self):
        most_recent_thread = threading.Thread(target=self.load_records_async, args=())
        most_recent_thread.daemon = True
        most_recent_thread.start()

    def load_records_async(self):
        with RecordsSqliteRepository(create_session()) as repo:
            records = repo.find_on_date(self.selectedDate)

        groups = GroupingService.for_records(records)
        GLib.idle_add(self.display_most_recent_records, groups)

    def display_most_recent_records(self, groups):
        for child in self.healthTypesListBox.get_children():
            self.healthTypesListBox.remove(child)

        for record_type in groups:
            group = groups[record_type]
            the_row = HealthTypeTemplateRow()
            the_row.set_group(group)
            self.healthTypesListBox.add(the_row)

        self.healthTypesListBox.show_all()

    def change_selected_day(self, widget):
        the_date = widget.get_date()
        self.set_selected_day(the_date)

    def set_selected_day(self, the_date):
        self.selectedDate = datetime.date(year=the_date.year, month=the_date.month + 1, day=the_date.day)
        self.show_date()
        self.calendarPopover.popdown()
        self.load_records()

    def show_date(self):
        self.headerBar.set_subtitle(self.selectedDate.strftime('%b %d, %Y'))

    def import_dialog_open(self, _):
        if self.importDialog is None:
            self.importDialog = ImportDialogController()
        self.importDialog.show()

    def add_dialog_open(self, _):
        if self.addDialog is None:
            self.addDialog = AddDialogController()
        self.addDialog.show()

    @staticmethod
    def app_close(_):
        Gtk.main_quit()
