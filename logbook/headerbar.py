import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk  # noqa: E402


class HeaderBar(Gtk.HeaderBar):
    def __init__(self):
        super().__init__()
        self.props.title = "Logbook"
        self.props.show_close_button = True
