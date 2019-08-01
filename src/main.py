from __future__ import print_function

import gi

from os.path import abspath, join, dirname

gi.require_version('Gtk', '3.0')
script_dir = dirname(abspath(__file__))

add_src = 'src'
if script_dir.endswith('src'):
    add_src = ''

from gi.repository import Gio

resource = Gio.resource_load(join(script_dir, add_src, 'resources', 'gnome-health.gresource'))
# noinspection PyProtectedMember
Gio.Resource._register(resource)

from gi.repository import Gtk
from src.ui.controller.MainController import MainController


def run_app():
    window = MainController()
    window.set_wmclass("Health", "Health")
    window.connect('delete-event', Gtk.main_quit)
    window.show_all()
    Gtk.main()


if __name__ == '__main__':
    run_app()
