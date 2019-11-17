from typing import Optional, Union

import libcst as cst
from libcst import (
    FunctionDef,
    Module,
    Name,
    Assign,
    List,
    Element,
    SimpleString,
    AssignTarget,
    ParenthesizedWhitespace,
    TrailingWhitespace,
    SimpleWhitespace,
    Newline,
    Comma,
    LeftSquareBracket,
    RightSquareBracket,
    ClassDef,
)
from libcst.metadata import ScopeProvider, GlobalScope


class AllAttributeTransformer(cst.CSTTransformer):
    METADATA_DEPENDENCIES = (ScopeProvider,)

    def __init__(self):
        super().__init__()
        self.names = []

    def process_name(self, node: Union["FunctionDef", "ClassDef"]) -> None:
        scope = self.get_metadata(ScopeProvider, node)
        if isinstance(scope, GlobalScope) and not node.name.value.startswith("_"):
            self.names.append(node.name.value)

    def visit_FunctionDef(self, node: "FunctionDef") -> Optional[bool]:
        self.process_name(node)
        return None

    def visit_ClassDef(self, node: "ClassDef") -> Optional[bool]:
        self.process_name(node)
        return None

    def leave_Module(self, original_node: "Module", updated_node: "Module") -> "Module":
        modified_body = list(original_node.body)

        indented_space = ParenthesizedWhitespace(
            first_line=TrailingWhitespace(
                whitespace=SimpleWhitespace(value=""),
                comment=None,
                newline=Newline(value=None),
            ),
            empty_lines=[],
            indent=True,
            last_line=SimpleWhitespace(value="    "),
        )

        indented_comma = Comma(
            whitespace_before=SimpleWhitespace(value=""),
            whitespace_after=indented_space,
        )
        line_break = ParenthesizedWhitespace(
            first_line=TrailingWhitespace(
                whitespace=SimpleWhitespace(value=""),
                comment=None,
                newline=Newline(value=None),
            )
        )

        list_values = [
            Element(SimpleString(value=f'"{global_name}"'), comma=indented_comma)
            for global_name in self.names[:-1]
        ]
        list_values.append(
            Element(
                SimpleString(value=f'"{self.names[-1]}"'),
                comma=Comma(
                    whitespace_before=SimpleWhitespace(value=""),
                    whitespace_after=line_break,
                ),
            )
        )

        all_names = Assign(
            targets=(AssignTarget(target=Name(value="__all__")),),
            value=List(
                list_values,
                lbracket=LeftSquareBracket(
                    whitespace_after=ParenthesizedWhitespace(
                        first_line=TrailingWhitespace(
                            whitespace=SimpleWhitespace(value=""),
                            comment=None,
                            newline=Newline(value=None),
                        ),
                        empty_lines=[],
                        indent=True,
                        last_line=SimpleWhitespace(value="    "),
                    )
                ),
                rbracket=RightSquareBracket(
                    whitespace_before=SimpleWhitespace(value="")
                ),
            ),
        )

        modified_body.append(Newline())
        modified_body.append(all_names)
        return updated_node.with_changes(body=modified_body)
