import gi

gi.require_version("Gtk", "3.0")
gi.require_version("Granite", "1.0")

from gi.repository import Granite, Gtk  # noqa: E402


class EntryItem(Gtk.Grid):
    def __init__(self, message: str) -> None:
        super().__init__()
        self.name = "Title"
        self.message = message
        self.timestamp = "00:00:00"

        self.create_layout()

    def create_layout(self) -> None:
        self.props.margin = 10

        title = Gtk.Label(self.name)
        title.get_style_context().add_class(Granite.STYLE_CLASS_H3_LABEL)
        title.props.halign = Gtk.Align.START

        body = Gtk.Label(self.message)
        body.get_style_context().add_class(Granite.STYLE_CLASS_H4_LABEL)
        body.props.ellipsize = True

        timestamp = Gtk.Label(self.timestamp)
        timestamp.props.hexpand = True
        timestamp.props.halign = Gtk.Align.END

        self.attach(title, 0, 0, 1, 1)
        self.attach(timestamp, 1, 0, 1, 1)
        self.attach(body, 0, 1, 1, 1)
