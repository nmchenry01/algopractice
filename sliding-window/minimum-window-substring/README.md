# Minimum Window Substring

## Category

Sliding Window

## Difficulty

Hard

## Problem Statement

Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

### Example

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"

### Solution Description

Use a sliding window with two pointers: expand the right pointer until you have a valid window containing all target characters, then shrink the left pointer while the window remains valid to find the minimum size. Track character frequencies with hash maps and use a "conditions met" counter to efficiently check if your current window is valid without scanning the entire frequency map each time.

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(n)
