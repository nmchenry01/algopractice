from collections import defaultdict
import unittest
from typing import List

class Solution:
    @staticmethod
    def top_k_frequent_elements_slow(nums: List[int], k: int) -> List[int]:
        #Naive solution
        # Group elements by frequency (O(n))
        # Sort the elements by values (O(nlog(n))
        # Return the first k elements, given that elements is sorted by highest -> lowest frequency

        lookup = defaultdict(int)
        for num in nums:
            lookup[num] += 1

        # A list of nums order by frequency (highest first)
        result = sorted(lookup.items(), key=lambda item: item[1], reverse=True)

        return list(map(lambda x: x[0], result[0:k]))
    
    @staticmethod
    def top_k_frequent_elements_fast(nums: List[int], k: int) -> List[int]:
        # Optimal Solution

        # Group elements by frequency (O(n))
        # Initialize an array of len(nums)
        # Insert into the array where idx = frequency and val = list(count_of_nums_with_frequency)
        # Iterate backwards through the array, return values until k is satisfied

        lookup = defaultdict(int)

        for num in nums:
            lookup[num] += 1

        buckets = [[] for _ in range(len(nums))]

        for [key, value] in lookup.items():
            buckets[value - 1].append(key)

        result = []

        for i in range(len(nums) - 1, -1, -1):
            values = buckets[i]
            if len(values) > 0:
                for val in values:
                    result.append(val)

                    if k == len(result):
                        return result;
    
class TestSolution(unittest.TestCase):
    def test_top_k_frequent_elements_slow(self):
        self.assertEqual(Solution.top_k_frequent_elements_slow([1,1,1,2,2,3], 2).sort(), [1,2].sort())
        self.assertEqual(Solution.top_k_frequent_elements_slow([1], 1), [1])

    def test_top_k_frequent_elements_fast(self):
        self.assertEqual(Solution.top_k_frequent_elements_fast([1,1,1,2,2,3], 2).sort(), [1, 2].sort())
        self.assertEqual(Solution.top_k_frequent_elements_fast([1], 1), [1])

if __name__ == "__main__":
    unittest.main()