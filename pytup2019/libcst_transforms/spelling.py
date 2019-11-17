import re

import libcst as cst
from libcst import BaseExpression, SimpleString

CORRECTIONS = {
    re.compile(r"\b{0}\b".format(pattern), re.IGNORECASE): replacement
    for pattern, replacement in (("json", "JSON"), ("yaml", "YAML"))
}


class FixAbbreviationSpelling(cst.CSTTransformer):
    def leave_SimpleString(
        self, original_node: "SimpleString", updated_node: "SimpleString"
    ) -> "BaseExpression":
        if " " not in original_node.value:
            return original_node

        text = original_node.value
        for pattern, replacement in CORRECTIONS.items():
            text = re.sub(pattern, replacement, text)
        return updated_node.with_changes(value=text)
