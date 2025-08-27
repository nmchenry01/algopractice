from collections import defaultdict
import unittest


class Solution:
    @staticmethod
    def longest_repeating_substring_with_replacement(s: str, k: int) -> int:
        start, end = 0, 0
        max_len = 0
        # At most 26 entries, given problem constraints
        frequency = defaultdict(int)

        while end < len(s):
            # Check if current sub string requires fewer than k replacements
            # If less or equal, move pointer right
            # If greater, move left pointer until valid

            end_char = s[end]
            frequency[end_char] += 1

            curr_len = end - start + 1
            replacements = curr_len - max(frequency.values())

            # If # replacements exceeds K, update freq, move start pointer, and recalculate
            while replacements > k:
                start_char = s[start]
                frequency[start_char] -= 1
                
                start += 1
                
                curr_len = end - start + 1
                replacements = curr_len - max(frequency.values())

            # Always move right pointer and check max
            max_len = max(max_len, curr_len)
            end += 1

        return max_len


class TestSolution(unittest.TestCase):
    def test_longest_repeating_substring_with_replacement(self):
        self.assertEqual(Solution.longest_repeating_substring_with_replacement("XYYX", 2), 4)

if __name__ == "__main__":
    unittest.main()
