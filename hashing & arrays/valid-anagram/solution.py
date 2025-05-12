from collections import defaultdict
import unittest

class Solution:
    @staticmethod
    def valid_anagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def to_dict(input: str):
            res = defaultdict(int)

            for i in input:
                res[i] += 1

            return res

        s_dict = to_dict(s)
        t_dict = to_dict(t)

        return s_dict == t_dict
    
class TestSolution(unittest.TestCase):
    def test_valid_anagram(self):
        self.assertEqual(Solution.valid_anagram("anagram", "nagaram"), True)
        self.assertEqual(Solution.valid_anagram("rat", "car"), False)

if __name__ == "__main__":
    unittest.main()