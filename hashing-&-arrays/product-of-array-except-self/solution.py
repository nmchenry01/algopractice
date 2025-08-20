import unittest
from typing import List

class Solution:
    @staticmethod
    def product_of_array_except_self(nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # Calculate prefix in place using results array
        # [1, 1, 2, 8]
        prefix = 1
        for idx, num in enumerate(nums):
            result[idx] = prefix
            prefix = num * prefix

        # Calculate postfix/final result in one pass
        # Postfix = [48, 24, 6, 1]
        # Result = [48, 24, 12, 8]
        postfix = 1
        for idx in range(len(nums) - 1, -1, -1):
            num = nums[idx]
            result[idx] = result[idx] * postfix
            postfix = num * postfix

        return result

class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution.product_of_array_except_self([1,2,4,6]), [48, 24, 12, 8])

if __name__ == "__main__":
    unittest.main() 