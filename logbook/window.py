import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk  # noqa: E402


class LogbookWindow(Gtk.ApplicationWindow):
    def __init__(self, application: Gtk.Application) -> None:
        super().__init__(application=application)
