from collections import defaultdict
import unittest
from typing import List

class SolutionOne:
    @staticmethod
    def group_anagrams(strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)

        # Helper function for getting character counts as a tuple
        def get_char_count(input: str) -> tuple[int, ...]:
            # Map the letters of the alphabet to index positions
            result = [0] * 26

            # Using ASCII values, normalize alphabet to 0-25
            for i in input:
                result[ord(i) - ord("a")] += 1

            # Return the result as a hashable tuple (to be used as the key in the result)
            return tuple(result)

        # Now group all the words
        for word in strs:
            char_count = get_char_count(word)

            result_dict[char_count].append(word)

        # Return as a list (values returns an iterator type)
        return list(result_dict.values())

class TestSolutionOne(unittest.TestCase):
    def test_groupAnagrams(self):
        self.assertEqual(
            sorted([sorted(group) for group in SolutionOne.group_anagrams(["eat","tea","tan","ate","nat","bat"])]),
            sorted([sorted(group) for group in [["bat"],["nat","tan"],["ate","eat","tea"]]])
        )

if __name__ == "__main__":
    unittest.main() 