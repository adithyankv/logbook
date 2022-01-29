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

    def __next__(self) -> dict:
        if self.reversed:
            entry = self.journal_reader.get_previous()
        else:
            entry = self.journal_reader.get_next()

        if entry:
            return entry
        else:
            raise StopIteration
