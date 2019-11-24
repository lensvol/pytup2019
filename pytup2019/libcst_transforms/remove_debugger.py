from typing import Union

import libcst as cst
import libcst.matchers as m
from libcst import RemovalSentinel, Expr, BaseSmallStatement


class RemoveDebuggerInvocations(cst.CSTTransformer):
    def leave_Expr(
        self, original_node: "Expr", updated_node: "Expr"
    ) -> Union["BaseSmallStatement", RemovalSentinel]:
        # FIXME: For some strange reason if we put that matcher combination
        # into m.call_if_inside() (or others), then it will get triggered on
        # _every_ function call. Not sure if bug or a feature :/
        if m.matches(
            original_node,
            m.Expr(
                value=m.Call(
                    func=m.OneOf(
                        m.Attribute(
                            value=m.OneOf(m.Name(value="pdb"), m.Name(value="ipdb")),
                            attr=m.Name(value="set_trace"),
                        ),
                        m.Name("breakpoint"),
                    )
                )
            ),
        ):
            return cst.RemoveFromParent()

        return original_node
