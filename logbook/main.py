import sys
from typing import List

from logbook.application import LogbookApp


def main(*args: List[str]) -> int:
    app = LogbookApp()
    return app.run(*args)


if __name__ == "__main__":
    main(sys.argv)
