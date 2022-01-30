import gi

from logbook.journal_manager import Entry

gi.require_version("Gtk", "3.0")
gi.require_version("Granite", "1.0")

from gi.repository import Granite, Gtk  # noqa: E402


class EntryItem(Gtk.Grid):
    def __init__(self, entry: Entry) -> None:
        super().__init__()
        self.name = entry.title
        self.message = entry.message
        self.timestamp = entry.timestamp
        self.priority = entry.priority

        # syslog priority levels along with an unknown case for entries with no
        # specified priority
        self.priority_levels = [
            "Emergency",
            "Alert",
            "Critical",
            "Error",
            "Warning",
            "Notice",
            "Info",
            "Debug",
            "Unknown",
        ]

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

        priority = Gtk.Label(f"priority:{self.priority_levels[self.priority]}")
        priority.props.halign = Gtk.Align.START
        priority_style = priority.get_style_context()
        if self.priority < 3:
            priority_style.add_class(Gtk.STYLE_CLASS_ERROR)
        elif self.priority < 5:
            priority_style.add_class(Gtk.STYLE_CLASS_WARNING)
        else:
            priority_style.add_class(Gtk.STYLE_CLASS_INFO)

        self.attach(title, 0, 0, 1, 1)
        self.attach(timestamp, 1, 0, 1, 1)
        self.attach(body, 0, 1, 1, 1)
        self.attach(priority, 0, 2, 1, 1)
