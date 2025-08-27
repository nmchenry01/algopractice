# Longest Repeating Substring with Replacement

## Category

Sliding Window

## Difficulty

Medium

## Problem Statement

You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

### Example

Input: s = "XYYX", k = 2

Output: 4

### Solution Description

Use sliding window where (window_size - most_frequent_char_count) ≤ k. Keep track of character frequency (using a hashmap) and move the pointer right. If the substring is invalid (IE, the condition fails) move the left pointer until valid again. Always move right pointer for every iteration and keep track of maximum.

### Optimal Time Complexity

O(n) (because of 26 characters in hashmap maximum)

### Optimal Space Complexity

O(m) (where m is the number of unique characters in the string)
