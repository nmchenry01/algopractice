# Minimum in Rotated Sorted Array

## Category

Binary Search

## Difficulty

Medium

## Problem Statement

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

### Example

Input: nums = [3,4,5,6,1,2]

Output: 1

### Solution Description

In a rotated sorted array, exactly one half is properly sorted while the other contains the rotation break where the minimum lives. Compare the middle element to the start element - if middle >= start, the left half is sorted so search right; otherwise, the rotation break is in the left half so search left.

### Optimal Time Complexity

O(logn)

### Optimal Space Complexity

O(1)
