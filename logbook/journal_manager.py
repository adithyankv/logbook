from __future__ import annotations

import logging

from systemd import journal


class Journal:
    def __init__(self) -> None:
        self.journal_reader = journal.Reader()
        self.journal_reader.this_boot()

    def __iter__(self) -> Journal:
        return self

    def __next__(self) -> Entry:
        entry_data = self.journal_reader.get_next()

        if entry_data:
            return Entry(entry_data)
        else:
            raise StopIteration


class Entry:
    def __init__(self, entry: dict) -> None:
        self.message = entry["MESSAGE"]

        try:
            self.timestamp = entry["__REALTIME_TIMESTAMP"].strftime("%X")
        except KeyError as e:
            logging.error(f"Couldn't retrieve timestamp of sender {repr(e)}")
            exit()

        try:
            self.title = entry["SYSLOG_IDENTIFIER"]
        except KeyError as id_error:
            try:
                # journalctl seems to use this value in the absense of identifier
                self.title = entry["_COMM"]
            except KeyError as comm_error:
                self.title = ""
                logging.error(
                    f"Couldn't retrieve name of sender \n{repr(id_error)}\n{repr(comm_error)}"
                )

        self.priority = entry["PRIORITY"]
