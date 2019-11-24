import libcst as cst

from pytup2019.utils import fix_spelling


class FixAbbreviationSpelling(cst.CSTTransformer):
    def visit_SimpleString(self, node):
        return " " in node.value

    def leave_SimpleString(self, original_node, updated_node):
        return original_node.with_changes(value=fix_spelling(original_node.value))
