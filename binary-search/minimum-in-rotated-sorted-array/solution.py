import math
from typing import List
import unittest


class Solution:
    @staticmethod
    def minimum_in_rotated_sorted_array(nums: List[int]) -> int:
        minimum = float('inf')
        start, end = 0, len(nums) - 1

        while start <= end:
            if nums[start] <= nums[end]:
                minimum = min(minimum, nums[start])
                break

            middle = math.floor((start + end) / 2)
            minimum = min(minimum, nums[middle])
            
            if nums[middle] >= nums[start]:
                # Search right
                start = middle + 1
            else:
                # Search left
                end = middle - 1

        return minimum

class TestSolution(unittest.TestCase):
    def test_minimum_in_rotated_sorted_array(self):
        self.assertEqual(Solution.minimum_in_rotated_sorted_array([3,4,5,6,1,2]), 1)

if __name__ == "__main__":
    unittest.main()
