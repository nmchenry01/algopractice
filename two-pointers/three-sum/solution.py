from typing import List
import unittest


class Solution:
    @staticmethod
    def three_sum(nums: List[int]) -> List[List[int]]:
        # Sort the array first so that the numbers are in ascending order
        nums.sort()

        result = []

        # Iterate over all of the elements, making sure to skip duplicate values
        for idx, num in enumerate(nums):
            # Move forward if the last value is the same, as that prevents duplicates
            if idx > 0 and num == nums[idx-1]:
                continue

            # Use a two pointers approach to check pairs
            # If sum > 0, move right pointer in (decreasing possible sum)
            # If sum < 0, move pointer left out (increasing possible sum)
            # Otherwise, add triplet to result array and make sure to handle duplicates

            start, end = idx + 1, len(nums) - 1
            while start < end:
                triplet_sum = num + nums[start] + nums[end]

                if triplet_sum > 0:
                    end -= 1
                elif triplet_sum < 0:
                    start += 1
                else:
                    result.append([num, nums[start], nums[end]])
                    
                    # Now we need to move pointers, making sure to avoid duplicates again
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1

                    start += 1
                    end -= 1

        return result


class TestSolution(unittest.TestCase):
    def test_three_sum(self):
        self.assertEqual(Solution.three_sum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])

if __name__ == "__main__":
    unittest.main()
