# Group Anagrams

## Category

Arrays and Hashing

## Difficulty

Medium

## Problem Statement

Given an array of strings, group anagrams together.

You can return the answer in any order.

### Example

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]
**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

### Solution Description

Think of each word as a 26-slot “letter counter” where each slot matches a letter’s position from ord(char) - ord('a').
Words with the same counter (same letters in same counts) share the same tuple key and get grouped together as anagrams.

### Optimal Time Complexity

O(m * n)

m = The number of strings in the input array
n = The number of letters in each string

### Optimal Space Complexity

O(m)