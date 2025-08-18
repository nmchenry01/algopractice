import unittest
from typing import List

class Solution:
    @staticmethod
    def encode(strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    
    @staticmethod
    def decode(s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            # First step is to find the length
            j = i

            # Move the pointer forward until we find the delimiter
            while str(s[j]) != "#":
                j += 1

            # Get the length (can be multiple digits, hence why the delimiter is important)
            length = int(s[i:j])

            # Move pointer forward, off of delimiter
            j += 1

            # Get the sub string, move the pointer forward
            sub_str = s[j:j+length]
            result.append(sub_str)
            i = j + length

        return result



    
class TestSolution(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(Solution.encode(["leet","code","loves","you"]), "4#leet4#code5#loves3#you")

    def test_decode(self):
        self.assertEqual(Solution.decode("4#leet4#code5#loves3#you"), ["leet","code","loves","you"])

if __name__ == "__main__":
    unittest.main()