#!/usr/bin/env python
import inspect
import sys
from lib2to3.fixer_base import BaseFix
from lib2to3.fixer_util import Name, Comma, Newline, Assign, String
from lib2to3.main import main
from lib2to3.pgen2 import token
from lib2to3.pytree import type_repr, Leaf
from pathlib import Path


class FixAll2To3(BaseFix):

    PATTERN = """
        classdef <'class' classname=any any*>
        |
        funcdef <'def' funcname=any any* >
    """

    def start_tree(self, tree, filename):
        super(FixAll2To3, self).start_tree(tree, filename)
        # Reset the patterns attribute for every file:
        self._names = []

    def transform(self, node, results):
        if type_repr(node.parent.type) != 'file_input':
            return node

        if 'classname' in results:
            name = results['classname'].value
        elif 'funcname' in results:
            name = results['funcname'].value

        if not name.startswith('_'):
            self._names.append(name)

        return node

    def finish_tree(self, tree, filename):
        print(filename)

        if isinstance(tree, Leaf):
            return

        names = [
            Leaf(token.LBRACE, "[", prefix=" "),
            Newline(),
        ]

        for name in self._names:
            names.append(String('"' + name + '"', prefix='    '))
            names.append(Comma())
            names.append(Newline())

        names.append(Leaf(token.LBRACE, "]", prefix=""))

        tree.append_child(Assign(Name('__all__'), names))
        tree.append_child(Newline())

        super(FixAll2To3, self).finish_tree(tree, filename)


if __name__ == '__main__':
    cur_path = Path().cwd()
    sys.path.append(str(cur_path / '..'))
    sys.exit(main(cur_path.parts[-1]))
