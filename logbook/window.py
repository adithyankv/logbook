import gi

from logbook.entry_list import EntryList
from logbook.headerbar import HeaderBar

gi.require_version("Gtk", "3.0")

from gi.repository import Gio, Gtk  # noqa: E402


class LogbookWindow(Gtk.ApplicationWindow):
    def __init__(self, application: Gtk.Application) -> None:
        super().__init__()
        self.set_application(application)
        self.create_layout()

        self.load_config_from_schema()

        self.connect("delete_event", self.save_config_to_schema)

    def create_layout(self) -> None:
        self.props.default_width = 600
        self.props.default_height = 400

        headerbar = HeaderBar()
        scrolled_window = Gtk.ScrolledWindow()
        entry_list = EntryList()

        scrolled_window.add(entry_list)
        self.set_titlebar(headerbar)
        self.add(scrolled_window)

    def load_config_from_schema(self) -> None:
        self.settings = Gio.Settings(schema_id="com.github.adithyankv.logbook")
        x = self.settings.get_int("position-x")
        y = self.settings.get_int("position-y")
        self.move(x, y)

        width = self.settings.get_int("width")
        height = self.settings.get_int("height")
        self.resize(width, height)

    def save_config_to_schema(self, *args) -> None:
        width, height = self.get_size()
        x, y = self.get_position()

        self.settings.set_int("position-x", x)
        self.settings.set_int("position-y", y)

        self.settings.set_int("width", width)
        self.settings.set_int("height", height)
