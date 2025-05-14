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

Group words that are anagrams by using the frequency of each letter as a unique signature.

How it works:

1. Count Letters:
  For each word, count how many times each letter appears.

2. Create a Hashable Key:
  Convert the letter counts into a tuple (which is hashable and can be used as a dictionary key).

3. Group Words:
  Use a dictionary to group words that share the same letter-count key.

4. Return Groups:
  Output the grouped anagrams as a list of lists.

Why it works:
Anagrams have the exact same letter counts, so their tuple keys will match, ensuring they are grouped together.

### Optimal Time Complexity

O(m*nlog(n)) or O(m * n)

m = The number of strings in the input array
n = The number of letters in each string

### Optimal Space Complexity

O(n*m)