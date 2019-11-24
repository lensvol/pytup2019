#!/usr/bin/env python

import sys
from lib2to3.main import main
from pathlib import Path

if __name__ == "__main__":
    cur_path = Path().cwd()
    sys.path.append(str(cur_path / "pytup2019"))
    sys.exit(main("pytup2019.fixers_2to3"))
