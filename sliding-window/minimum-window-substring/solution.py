from collections import defaultdict
import unittest


class Solution:
    @staticmethod
    def minimum_window_substring(s: str, t: str) -> str:
        """
        Find the minimum window substring of s that contains all characters of t.
        
        Algorithm: Sliding Window Technique
        1. Expand window by moving right pointer until all conditions are met
        2. Once valid, shrink window by moving left pointer while maintaining validity
        3. Track the minimum valid window found
        """
        
        # Edge case: empty target string
        if t == "":
            return ""

        # STEP 1: Set up data structures
        # window: tracks character frequencies in current window
        # target: tracks required character frequencies from string t
        window, target = defaultdict(int), defaultdict(int)

        # Build target frequency map from string t
        # Example: if t = "abc", target = {'a': 1, 'b': 1, 'c': 1}
        for c in t:
            target[c] += 1

        # STEP 2: Initialize sliding window pointers and tracking variables
        start, end = 0, 0  # Left and right pointers of the sliding window
        
        # conditions_met: how many unique characters have sufficient count
        # total_conditions: total unique characters we need (length of target dict)
        # Example: if t = "aab", total_conditions = 2 (for 'a' and 'b')
        conditions_met, total_conditions = 0, len(target)
        
        # result: stores [start_index, end_index] of minimum window
        # min_len: length of minimum window found so far
        result, min_len = [], float('inf')

        # STEP 3: Main sliding window loop
        while end < len(s):
            # EXPAND WINDOW: Add current character to window
            end_char = s[end]
            window[end_char] += 1
            
            # Check if we've satisfied the requirement for this character
            # Only increment conditions_met when we reach EXACTLY the required count
            # (not when we exceed it, to avoid double counting)
            if end_char in target and window[end_char] == target[end_char]:
                conditions_met += 1

            # SHRINK WINDOW: While we have a valid window (all conditions met)
            while conditions_met == total_conditions:
                # Update result if current window is smaller than previous minimum
                current_window_size = (end - start) + 1
                if current_window_size < min_len:
                    result = [start, end]  # Store indices of minimum window
                    min_len = current_window_size

                # Try to shrink window from the left
                start_char = s[start]
                window[start_char] -= 1  # Remove leftmost character from window
                
                # Check if removing this character breaks a condition
                # We decrement conditions_met only when the count drops BELOW required
                if start_char in target and window[start_char] < target[start_char]:
                    conditions_met -= 1
                
                start += 1  # Move left pointer right (shrink window)

            # Move right pointer to expand window for next iteration
            end += 1

        # STEP 4: Return result
        # If result is empty, no valid window was found
        # Otherwise, extract substring using stored indices
        return s[result[0]:result[1] + 1] if len(result) > 0 else ""


class TestSolution(unittest.TestCase):
    def test_minimum_window_substring(self):
        self.assertEqual(Solution.minimum_window_substring("OUZODYXAZV", "XYZ"), "YXAZ")

if __name__ == "__main__":
    unittest.main()
