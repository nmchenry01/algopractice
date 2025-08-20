# Contains Duplicate

## Category

Arrays and Hashing

## Difficulty

Easy

## Problem Statement

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

### Example

**Input:** nums = [1,2,3,1]
**Output:** true

**Input:** nums = [1,2,3,4]
**Output:** false

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]
**Output:** true

### Solution Description

Use a set to track seen numbers; return `True` if a number is already in the set, otherwise add it to the set. If loop completes, return `False`.

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(n)
