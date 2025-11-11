"""Entry point for running the package as a module: python -m legal_writing_tool"""

import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main())
