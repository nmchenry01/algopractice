# Longest Substring Without Repeats

## Category

Sliding Window

## Difficulty

Medium

## Problem Statement

Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

### Example

Input: s = "zxyzxyz"

Output: 3

### Solution Description

Use a set to keep track of duplicate characters, and use a sliding window (start/end from 0). While the end is in bounds, check if the end character is a duplicate. If it is, remove the start character from the set, and move the start pointer over. Keep checking for max (end - start + 1) and adding characters to the set along the way.

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(n)
