#!/usr/bin/env python
from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import Name, Comma, Newline, Assign, String
from lib2to3.pgen2 import token
from lib2to3.pytree import type_repr, Leaf


class FixAllAttribute(BaseFix):

    PATTERN = """
        classdef <'class' classname=any any*>
        |
        funcdef <'def' funcname=any any* >
    """

    def start_tree(self, tree, filename):
        super(FixAllAttribute, self).start_tree(tree, filename)
        # Reset the patterns attribute for every file:
        self._names = []

    def transform(self, node, results):
        if type_repr(node.parent.type) != "file_input":
            return node

        if "classname" in results:
            name = results["classname"].value
        elif "funcname" in results:
            name = results["funcname"].value

        if not name.startswith("_"):
            self._names.append(name)

        return node

    def finish_tree(self, tree, filename):
        print(filename)

        if isinstance(tree, Leaf):
            return

        if not self._names:
            return

        names = [Leaf(token.LBRACE, "[", prefix=" "), Newline()]

        for name in self._names:
            names.append(String('"' + name + '"', prefix="    "))
            names.append(Comma())
            names.append(Newline())

        names.append(Leaf(token.LBRACE, "]", prefix=""))

        tree.append_child(Assign(Name("__all__"), names))
        tree.append_child(Newline())

        super(FixAllAttribute, self).finish_tree(tree, filename)
