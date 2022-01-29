import gi
from headerbar import HeaderBar
from journal_entries import JournalEntries

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk  # noqa: E402


class LogbookWindow(Gtk.ApplicationWindow):
    def __init__(self, application: Gtk.Application) -> None:
        super().__init__()
        self.set_application(application)
        self.create_layout()

    def create_layout(self):
        headerbar = HeaderBar()
        scrolled_window = Gtk.ScrolledWindow()
        entries_list = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        scrolled_window.add(entries_list)

        entries = JournalEntries()
        for entry in entries:
            entry_label = Gtk.Label(entry["MESSAGE"])
            entry_label.props.halign = Gtk.Align.START
            separator = Gtk.Separator()
            entries_list.add(entry_label)
            entries_list.add(separator)

        self.props.default_height = 400
        self.props.default_width = 400
        self.set_titlebar(headerbar)
        self.add(scrolled_window)
