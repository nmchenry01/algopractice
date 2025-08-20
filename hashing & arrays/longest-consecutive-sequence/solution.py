import unittest
from typing import List

class Solution:
    @staticmethod
    def longest_consecutive_sequence(nums: List[int]) -> int:
        # Need to be able to determine items in the list that are the start of a sequence
        # Can define this as num - 1 not in set(nums) (IE, if there's nothing before it, it's the start of a sequence)
        # Can skip anything that isn't that start of a sequence
        # For each start of the sequence, we count forward until the end
        unique_nums = set(nums)
        longest_seq = 0

        for num in unique_nums:
            is_start_of_seq = num - 1 not in unique_nums

            if is_start_of_seq:
                current_seq = 1
                next_num = num + 1

                while next_num in unique_nums:
                    current_seq += 1
                    next_num += 1
                
                longest_seq = max(longest_seq, current_seq)

        return longest_seq

class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution.longest_consecutive_sequence([2,20,4,10,3,4,5]), 4)

if __name__ == "__main__":
    unittest.main() 