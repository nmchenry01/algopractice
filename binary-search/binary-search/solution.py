import math
from typing import List
import unittest


class Solution:
    @staticmethod
    def binary_search(nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            middle = math.floor((start + end) / 2)

            if nums[middle] < target:
                start = middle + 1
            elif nums[middle] > target:
                end = middle - 1
            else:
                return middle

        return -1

class TestSolution(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(Solution.binary_search([-1,0,2,4,6,8], 4), 3)

if __name__ == "__main__":
    unittest.main()
