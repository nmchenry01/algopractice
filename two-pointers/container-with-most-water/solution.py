from typing import List
import unittest


class Solution:
    @staticmethod
    def container_with_most_water(heights: List[int]) -> int:
        # Volume = h * w, where h = min(bar 1, bar 2)
        # Two pointers, trying to maximize volume along the way

        max_volume = 0
        start, end = 0, len(heights) - 1

        while start < end:
            startBar = heights[start]
            endBar = heights[end]

            volume = (end - start) * min(startBar, endBar)

            max_volume = max(max_volume, volume)

            # Move bar based on which is lower
            if startBar >= endBar:
                end -= 1
            else:
                start += 1

        return max_volume


class TestSolution(unittest.TestCase):
    def test_container_with_most_water(self):
        self.assertEqual(Solution.container_with_most_water([1,7,2,5,4,7,3,6]), 36)

if __name__ == "__main__":
    unittest.main()
