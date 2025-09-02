# Binary Search

## Category

Binary Search

## Difficulty

Easy

## Problem Statement

You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

### Example

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3

### Solution Description

Binary search repeatedly cuts a sorted array in half by comparing the middle element to the target - if the middle is too small, search the right half; if too large, search the left half. This "divide and conquer" approach finds any element in O(log n) time by eliminating half the possibilities with each comparison.

### Optimal Time Complexity

O(logn)

### Optimal Space Complexity

O(1)
