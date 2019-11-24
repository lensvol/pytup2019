from typing import Optional

from bowler import Query, Filename, Capture, LN

from pytup2019.utils import fix_spelling

PATTERN = """STRING"""


def corrector(node: LN, capture: Capture, filename: Filename) -> Optional[LN]:
    node.value = fix_spelling(node.value)
    return node


def get_query(path):
    return Query(path).select(PATTERN).modify(corrector)
