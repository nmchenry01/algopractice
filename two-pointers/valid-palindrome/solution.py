from collections import defaultdict
import unittest


class Solution:
    @staticmethod
    def valid_palindrome(s: str) -> bool:
        def is_alpha_numeric(s: str) -> bool:
            to_lower = s.lower()

            return (ord("a") <= ord(to_lower) <= ord("z")) or (
                ord("0") <= ord(to_lower) <= ord("9")
            )

        start, end = 0, len(s) - 1

        while start < end:
            # Move pointers inward if not an alphanumeric character (ensuring inbounds)
            while start < end and not is_alpha_numeric(s[start]):
                start += 1
            while start < end and not is_alpha_numeric(s[end]):
                end -= 1

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True


class TestSolution(unittest.TestCase):
    def test_valid_palindrome(self):
        self.assertEqual(Solution.valid_palindrome("Was it a car or a cat I saw?"), True)
        self.assertEqual(Solution.valid_palindrome("tab a cat"), False)


if __name__ == "__main__":
    unittest.main()
