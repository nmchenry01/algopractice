import unittest
from typing import List

class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        lookup = {}

        for idx in range(len(nums)):
            num = nums[idx]
            complement = target - num

            if complement in lookup:
                return [lookup[complement], idx]
            
            lookup[num] = idx

        return []

class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(Solution.two_sum([2,7,11,15], 9), [0,1])
        self.assertEqual(Solution.two_sum([3,2,4], 6), [1,2])
        self.assertEqual(Solution.two_sum([3,3], 6), [0,1])
        self.assertEqual(Solution.two_sum([-1,0], -1), [0,1])
        self.assertEqual(Solution.two_sum([-3,4,3,90], 0), [0,2])

if __name__ == "__main__":
    unittest.main() 