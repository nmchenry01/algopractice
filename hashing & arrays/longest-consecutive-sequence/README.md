# Longest Consecutive Sequence

## Category

Arrays and Hashing

## Difficult

Hard

## Problem Statement

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

### Example

Input: nums = [2,20,4,10,3,4,5]
Output: 4

### Solution Description

Use a hash set to store all numbers, then for each number that could start a sequence (no num-1 in set), count consecutive numbers forward until the sequence breaks.
Keep track of the maximum sequence.

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(n)