import sys
from typing import List

import application


def main(*args: List[str]) -> int:
    app = application.LogbookApp()
    return app.run(*args)


if __name__ == "__main__":
    main(sys.argv)
