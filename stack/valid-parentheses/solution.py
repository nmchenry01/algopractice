from typing import List
import unittest


class Solution:
    @staticmethod
    def valid_parentheses(s: str) -> bool:
        opening_chars = set(["(", "{", "["])
        lookup = {")": "(", "}": "{", "]": "["}

        stack = []

        for c in s:
            if c in opening_chars:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                last_char = stack.pop()

                if last_char != lookup[c]:
                    return False

        return len(stack) == 0


class TestSolution(unittest.TestCase):
    def test_valid_parentheses(self):
        self.assertEqual(Solution.valid_parentheses("([{}])"), True)

if __name__ == "__main__":
    unittest.main()
