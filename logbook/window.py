import gi

from logbook.entry_item import EntryItem
from logbook.entry_list import EntryList
from logbook.headerbar import HeaderBar

gi.require_version("Gtk", "3.0")

from gi.repository import GObject, Gtk  # noqa: E402


class LogbookWindow(Gtk.ApplicationWindow):
    def __init__(self, application: Gtk.Application) -> None:
        super().__init__()
        self.set_application(application)
        self.create_layout()

    def create_layout(self) -> None:
        self.props.default_width = 600
        self.props.default_height = 400

        headerbar = HeaderBar()
        scrolled_window = Gtk.ScrolledWindow()
        entry_list = EntryList()

        scrolled_window.add(entry_list)
        self.set_titlebar(headerbar)
        self.add(scrolled_window)
