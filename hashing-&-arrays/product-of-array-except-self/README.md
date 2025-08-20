# Product of Array Except Self

## Category

Arrays and Hashing

## Difficult

Medium

## Problem Statement

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Solve it in O(n) time without using the division operation.

### Example

Input: nums = [1,2,4,6]
Output: [48,24,12,8]

### Solution Description

Using the result array, make the first pass over the array (initialize with 1s) to calculate the prefix (assign value before updating prefix). On the second pass, calculate both the postfix and final solution using similar logic, but iterating backwards.

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(n)