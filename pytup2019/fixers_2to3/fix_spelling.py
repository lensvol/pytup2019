#!/usr/bin/env python
import re
from lib2to3.fixer_base import BaseFix


class FixSpelling(BaseFix):

    CORRECTIONS = {"json": "JSON"}

    PATTERN = """STRING"""

    def transform(self, node, results):
        for pattern, replacement in self.CORRECTIONS.items():
            compiled = re.compile(r"\b{0}\b".format(pattern), re.IGNORECASE)
            node.value = re.sub(compiled, replacement, node.value)
        return node
