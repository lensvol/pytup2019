from typing import Optional

from bowler import Query, Filename, Capture, LN

from pytup2019.utils import fix_spelling

pattern = """STRING"""


def corrector(node: LN, capture: Capture, filename: Filename) -> Optional[LN]:
    node.value = fix_spelling(node.value)
    return node


if __name__ == "__main__":
    (Query("../samples/bad_spelling.py").select(pattern).modify(corrector).diff())
