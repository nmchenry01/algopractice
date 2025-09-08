# Search in Rotated Sorted Array

## Category

Binary Search

## Difficulty

Medium

## Problem Statement

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

### Example

Input: nums = [3,4,5,6,1,2], target = 1

Output: 4

### Solution Description

In a rotated sorted array, exactly one half is properly sorted while the other contains the rotation break where the minimum lives. Compare the middle element to the start element - if middle >= start, the left half is sorted so search right; otherwise, the rotation break is in the left half so search left. However, you also have to consider the target you're looking for, once you've established which portion of the array you're in. For example, if you're in the left sorted portion and the target is either less than the start or greater than the middle, search right.

### Optimal Time Complexity

O(logn)

### Optimal Space Complexity

O(1)
