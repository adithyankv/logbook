import gi
from journal_entries import JournalEntry

gi.require_version("Gtk", "3.0")
gi.require_version("Granite", "1.0")

from gi.repository import Granite, Gtk  # noqa: E402


class EntryItem(Gtk.Grid):
    def __init__(self, entry: JournalEntry) -> None:
        super().__init__()
        self.name = entry.title
        self.message = entry.message
        self.timestamp = entry.timestamp

        self.create_layout()

    def create_layout(self) -> None:
        self.props.margin = 10

        title = Gtk.Label(self.name)
        title.get_style_context().add_class(Granite.STYLE_CLASS_H3_LABEL)
        title.props.halign = Gtk.Align.START
        title.props.ellipsize = True

        body = Gtk.Label(self.message)
        body.get_style_context().add_class(Granite.STYLE_CLASS_H4_LABEL)
        body.props.ellipsize = True

        timestamp = Gtk.Label(self.timestamp)
        timestamp.props.hexpand = True
        timestamp.props.halign = Gtk.Align.END

        self.attach(title, 0, 0, 1, 1)
        self.attach(timestamp, 1, 0, 1, 1)
        self.attach(body, 0, 1, 1, 1)
