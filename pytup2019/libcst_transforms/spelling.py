import re

import libcst as cst
from libcst import BaseExpression, SimpleString

from pytup2019.utils import fix_spelling


class FixAbbreviationSpelling(cst.CSTTransformer):
    def leave_SimpleString(
        self, original_node: "SimpleString", updated_node: "SimpleString"
    ) -> "BaseExpression":
        return updated_node.with_changes(value=fix_spelling(original_node.value))
