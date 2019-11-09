import re
from typing import Optional

from bowler import Query, Filename, Capture, LN

pattern = '''
STRING
'''


CORRECTIONS = {
    'json': 'JSON',
    'yaml': 'YAML',
}


def corrector(node: LN, capture: Capture, filename: Filename) -> Optional[LN]:
    for pattern, replacement in CORRECTIONS.items():
        compiled_re = re.compile(pattern, re.IGNORECASE)
        node.value = re.sub(compiled_re, replacement, node.value)

    return node


if __name__ == '__main__':
    (
        Query("../samples/bad_spelling.py")
        .select(pattern)
        .modify(corrector)
        .diff()
    )