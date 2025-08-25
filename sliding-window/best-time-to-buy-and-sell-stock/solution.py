from typing import List
import unittest


class Solution:
    @staticmethod
    def best_time_to_buy_and_sell_stock(prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        # Initialize sliding window
        start, end = 0, 1
        max_profit = 0

        while end < len(prices):
            profit = prices[end] - prices[start]

            # If profit is positive, update. Otherwise, move to the new minimum
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                start = end

            end += 1


        return max_profit


class TestSolution(unittest.TestCase):
    def test_best_time_to_buy_and_sell_stock(self):
        self.assertEqual(Solution.best_time_to_buy_and_sell_stock([10,1,5,6,7,1]), 6)

if __name__ == "__main__":
    unittest.main()
