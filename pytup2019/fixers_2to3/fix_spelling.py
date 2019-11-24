#!/usr/bin/env python

from pytup2019.utils import fix_spelling

from lib2to3.fixer_base import BaseFix


class FixSpelling(BaseFix):
    PATTERN = """STRING"""

    def match(self, node):
        return " " in node.value

    def transform(self, node, results):
        node.value = fix_spelling(node.value)
        return node
