# Valid Anagram

## Problem Statement

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example

**Input:** s = "anagram", t = "nagaram"
**Output:** true

**Input:** s = "rat", t = "car"
**Output:** false

### Solution Description

Use a hashmap to count character occurrences in each string. If both strings have the same length and identical character counts, they are anagrams; otherwise, they're not.

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(n)
