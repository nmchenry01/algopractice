# Container With Most Water

## Category

Two Pointers

## Difficulty

Medium

## Problem Statement

You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

### Example

Input: height = [1,7,2,5,4,7,3,6]

Output: 36

### Solution Description

Start with pointers at both ends of the array, calculate area, then move the pointer with the smaller height inward.

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(1)
