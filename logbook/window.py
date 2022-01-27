import gi
from headerbar import HeaderBar

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk  # noqa: E402


class LogbookWindow(Gtk.ApplicationWindow):
    def __init__(self, application: Gtk.Application) -> None:
        super().__init__()
        self.set_application(application)
        self.create_layout()

    def create_layout(self):
        headerbar = HeaderBar()

        self.props.default_height = 400
        self.props.default_width = 400
        self.set_titlebar(headerbar)
