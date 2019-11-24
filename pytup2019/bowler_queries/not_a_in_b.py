from lib2to3.pytree import Node, Leaf
from symbol import comp_op
from symbol import comparison

from bowler import Query, Filename, Capture, LN


PATTERN = """not_test < 'not' comparison <element=any 'in' collection=any > >"""


def fix_not_a_in_b(node: LN, capture: Capture, filename: Filename):
    capture["element"].parent = None
    capture["collection"].parent = None

    new_comparison = Node(
        comparison,
        [
            capture["element"],
            Node(comp_op, [Leaf(1, "not", prefix=" "), Leaf(1, "in", prefix=" ")]),
            capture["collection"],
        ],
    )
    new_comparison.parent = node.parent
    return new_comparison


def get_query(path):
    return Query(path).select(PATTERN).modify(fix_not_a_in_b)
