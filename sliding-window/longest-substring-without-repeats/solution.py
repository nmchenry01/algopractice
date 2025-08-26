from typing import List
import unittest


class Solution:
    @staticmethod
    def longest_substring_without_repeats(s: str) -> int:
        max_sub_str = 0
        start, end = 0, 0
        unique_chars = set()

        while end < len(s):
            end_char = s[end]

            while end_char in unique_chars:
                start_char = s[start]
                unique_chars.remove(start_char)
                start += 1

            unique_chars.add(end_char)
            max_sub_str = max(max_sub_str, end - start + 1)
            end += 1

        return max_sub_str


class TestSolution(unittest.TestCase):
    def test_longest_substring_without_repeats(self):
        self.assertEqual(Solution.longest_substring_without_repeats("zxyzxyz"), 3)

if __name__ == "__main__":
    unittest.main()
