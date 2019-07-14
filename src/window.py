# window.py
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

from gi.repository import Gtk


@Gtk.Template(resource_path='/com/codingsimply/gnome/health/window.ui')
class GnomeHealthWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'GnomeHealthWindow'

    dateTimeButton = Gtk.Template.Child()
    dateLabel = Gtk.Template.Child()
    calendar = Gtk.Template.Child()
    calendarPopover = Gtk.Template.Child()
    healthTypesListBox = Gtk.Template.Child()

    selectedDate = datetime.date.today()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.calendar.connect('day-selected', self.change_selected_day)
        self.change_selected_day(self.calendar)

    def change_selected_day(self, widget):
        the_date = widget.get_date()
        self.selectedDate = datetime.date(year=the_date.year, month=the_date.month, day=the_date.day)
        self.show_date()
        self.calendarPopover.popdown()

    def show_date(self):
        self.dateLabel.set_text(self.selectedDate.strftime('%b %d, %Y'))
