#!/usr/bin/env python

import difflib
import sys

import libcst as cst

from pytup2019.libcst_transforms.all_attribute import AllAttributeTransformer
from pytup2019.libcst_transforms.mutable_args import ArgEmptyInitTransformer
from pytup2019.libcst_transforms.spelling import FixAbbreviationSpelling


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fp:
        source = fp.read()

    tree = cst.parse_module(source)
    wrapped_tree = cst.MetadataWrapper(tree)
    modified_tree = wrapped_tree

    transformers = [
        AllAttributeTransformer(),
        ArgEmptyInitTransformer(),
        FixAbbreviationSpelling(),
    ]

    for transformer in transformers:
        modified_tree = modified_tree.visit(transformer)

    print(
        "".join(
            difflib.unified_diff(
                source.splitlines(keepends=True), modified_tree.code.splitlines(1)
            )
        )
    )
