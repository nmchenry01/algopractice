from collections import defaultdict
import unittest
from typing import List

class SolutionOne:
    @staticmethod
    def group_anagrams(strs: List[str]) -> List[List[str]]:
        # Create a helper function for decomposing each string into its letter count
        def count_letters(value: str) -> tuple[str, int]:
            # Creates a dictionary where 0 is the default value
            result = defaultdict(int)
            sorted_value = sorted(value)
            for val in sorted_value:
                result[val] += 1

            # A tuple is hashable
            return tuple(result.items())

        grouped_letters = defaultdict(list)
        
        for val in strs:
            letter_count = count_letters(val)

            grouped_letters[letter_count].append(val)

        return list(grouped_letters.values())

class TestSolutionOne(unittest.TestCase):
    def test_groupAnagrams(self):
        self.assertEqual(
            sorted([sorted(group) for group in SolutionOne.group_anagrams(["eat","tea","tan","ate","nat","bat"])]),
            sorted([sorted(group) for group in [["bat"],["nat","tan"],["ate","eat","tea"]]])
        )

if __name__ == "__main__":
    unittest.main() 