import math
from typing import List
import unittest


class Solution:
    @staticmethod
    def search_in_rotated_sorted_array(nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            middle = (end + start) // 2

            if nums[middle] == target:
                return middle

            # In left sorted array
            if nums[middle] >= nums[start]:
                # If outside the left section, search right
                if target > nums[middle] or target < nums[start]:
                    start = middle + 1
                # Otherwise, we need to search in the left section
                else:
                    end = middle - 1
            else:
                # Same logic as above, but inverted
                if target < nums[middle] or target > nums[end]:
                    end = middle - 1
                else:
                    start = middle + 1

        return -1

class TestSolution(unittest.TestCase):
    def test_search_in_rotated_sorted_array(self):
        self.assertEqual(Solution.search_in_rotated_sorted_array([3,4,5,6,1,2], 1), 4)

if __name__ == "__main__":
    unittest.main()
