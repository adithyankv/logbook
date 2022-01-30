import gi

from logbook.entry_item import EntryItem
from logbook.journal_manager import Journal

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk  # noqa: E402


class EntryList(Gtk.Box):
    def __init__(self, reversed: bool = True) -> None:
        super().__init__()
        self.props.orientation = Gtk.Orientation.VERTICAL
        self.reversed = reversed
        self.create_layout()

    def create_layout(self) -> None:
        journal = Journal()
        entries = [entry for entry in journal]
        if self.reversed:
            entries.reverse()

        for entry in entries:
            entry_item = EntryItem(entry)
            self.add(entry_item)
            self.add(Gtk.Separator())
