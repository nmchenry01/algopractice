import unittest
from typing import List

class Solution:
    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        lookup = set()

        for i in range(len(nums)):
            val = nums[i]
            if val in lookup:
                return True
            lookup.add(val)

        return False
    
class TestSolution(unittest.TestCase):
    def test_containsDuplicate(self):
        self.assertEqual(Solution.containsDuplicate([1,2,3,1]), True)
        self.assertEqual(Solution.containsDuplicate([1,2,3,4]), False)
        self.assertEqual(Solution.containsDuplicate([1]), False)

if __name__ == "__main__":
    unittest.main()