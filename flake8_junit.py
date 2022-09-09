# Copyright (c) 2022 Pablo Marti <pablo@cointracker.io>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""Flake8 extension that bans JUnit asserts."""

import ast
import re

__all__ = ["AssertChecker"]
__version__ = "0.1.0"

JUNIT_ASSERT = re.compile(r"^assert[A-Z]\w+$")


class AssertChecker:
    """Unittest assert method checker"""

    name = "junit"
    version = __version__
    JUNIT_FIXES = {
        "assertRaises": "pytest.raises(Exception):",
    }

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    def is_assert_method_call(self, node):
        return (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and JUNIT_ASSERT.match(node.func.attr)
        )

    def run(self):
        # Visit all the assert method calls in the tree.
        for node in ast.walk(self.tree):
            if self.is_assert_method_call(node):
                suggested_fix = self.JUNIT_FIXES.get(
                    node.func.attr, "assert actual == expected"
                )
                msg = f"J100 - Detected usage of `{node.func.attr}`, replace with `{suggested_fix}`"
                yield node.lineno, node.col_offset, msg, type(self)
