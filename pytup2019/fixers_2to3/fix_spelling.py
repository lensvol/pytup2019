#!/usr/bin/env python
import re
from lib2to3.fixer_base import BaseFix

from pytup2019.utils import fix_spelling


class FixSpelling(BaseFix):
    PATTERN = """STRING"""

    def transform(self, node, results):
        node.value = fix_spelling(node.value)
        return node
