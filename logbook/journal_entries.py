from __future__ import annotations

from systemd import journal


class JournalEntries:
    def __init__(self, reversed: bool = True) -> None:
        self.journal_reader = journal.Reader()
        self.reversed = reversed
        if self.reversed:
            self.journal_reader.seek_tail()
        self.journal_reader.this_boot()

    def __iter__(self) -> JournalEntries:
        return self

    def __next__(self) -> JournalEntry:
        if self.reversed:
            entry_data = self.journal_reader.get_previous()
        else:
            entry_data = self.journal_reader.get_next()

        if entry_data:
            return JournalEntry(entry_data)
        else:
            raise StopIteration


class JournalEntry:
    def __init__(self, entry: dict) -> None:
        self.message = entry["MESSAGE"]
        self.timestamp = entry["__REALTIME_TIMESTAMP"].strftime("%X")
        try:
            self.title = entry["SYSLOG_IDENTIFIER"]
        except KeyError:
            self.title = entry["_COMM"]
