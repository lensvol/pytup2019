#!/usr/bin/env python

import sys

from bowler import Query, Filename, Capture, LN


PATTERN = """
    power < "ipdb" trailer < '.' 'set_trace' > trailer < '(' ')' > > |
    power < "breakpoint" trailer < "(" ")" > > 
"""


def remove_debugger_statements(node: LN, capture: Capture, filename: Filename):
    parent_index = node.parent.children.index(node)
    node.parent.children = (
        node.parent.children[0:parent_index] + node.parent.children[parent_index + 2 :]
    )

    return None


def get_query(path):
    return (
        Query(path)
        .select(PATTERN)
        .modify(remove_debugger_statements)
        .execute(interactive=False, write=True)
    )
