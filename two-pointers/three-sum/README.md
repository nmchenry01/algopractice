# Three Sum

## Category

Two Pointers

## Difficulty

Medium

## Problem Statement

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

### Example

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

### Solution Description

Sort the array, iterate over the sorted array (making sure to skip duplicates via the n == n-1 check), then use two pointers (left/right) to find pairs that sum to 0. Move pointers depending on whether the sum is greater than or less than 0. In the case of a 0 sum, make sure to skip duplicates for both pointers (while loops) and move both the pointers.

### Optimal Time Complexity

O(n^2)

### Optimal Space Complexity

O(1) or O(n)
