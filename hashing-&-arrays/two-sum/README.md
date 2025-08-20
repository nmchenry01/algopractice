# Two Sum

## Category

Arrays and Hashing

## Difficult

Easy

## Problem Statement

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

### Example

**Input:** nums = [3,4,5,6], target = 7
**Output:** [0,1]

**Input:** nums = [4,5,6], target = 10
**Output:** [0,2]

### Solution Description

Loop through the array, and for each number, check if its complement (target minus the number) is already in a hash map. If it is, return their indices. If not, add the number and its index to the hash map. This finds the answer in one pass.

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(n)