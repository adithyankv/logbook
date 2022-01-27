import gi
from window import LogbookWindow

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk  # noqa: E402


class LogbookApp(Gtk.Application):
    app_id = "com.github.adithyankv.logbook"

    def __init__(self) -> None:
        super().__init__(application_id=self.app_id)

    def do_activate(self) -> None:
        window = LogbookWindow(application=self)
        window.show_all()
