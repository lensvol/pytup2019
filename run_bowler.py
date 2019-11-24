#!/usr/bin/env python

import sys

from pytup2019.bowler_queries import spelling, remove_debugger, not_a_in_b


if __name__ == "__main__":
    for path in sys.argv[1:]:
        for module in [spelling, remove_debugger, not_a_in_b]:
            query = module.get_query(path)
            query.diff()
