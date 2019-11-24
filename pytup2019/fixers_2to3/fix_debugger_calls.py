#!/usr/bin/env python
from lib2to3.fixer_base import BaseFix


class FixDebuggerCalls(BaseFix):

    PATTERN = """
        CALL=power < "ipdb" trailer < '.' 'set_trace' > trailer < '(' ')' > > |
        CALL=power < "breakpoint" trailer < "(" ")" > > 
    """

    def transform(self, node, results):
        parent_index = node.parent.children.index(node)
        print(results)

        if parent_index == 0:
            node.parent.children = node.parent.children[1:]
        else:
            node.parent.children = (
                    node.parent.children[0:parent_index] + node.parent.children[parent_index + 2:]
            )
        node.changed()