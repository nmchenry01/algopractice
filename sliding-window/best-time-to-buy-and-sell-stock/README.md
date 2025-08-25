# Best Time to Buy and Sell Stock

## Category

Sliding Window

## Difficulty

Easy

## Problem Statement

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

### Example

Input: prices = [10,1,5,6,7,1]

Output: 6

### Solution Description

Initialize a start, end pointer (0, 1). While the end pointer is in bounds, check if there is a profit. If there is, update the max profit. If not, move the start pointer to the end (the new minimum). Always move the end pointer forward.

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(1)
