# Encode and Decode Strings

## Category

Arrays and Hashing

## Difficulty

Medium

## Problem Statement

Design an algorithm to encode a list of strings to a single string. 

The encoded string is then decoded back to the original list of strings.

### Example

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

### Solution Description

Encode: Prefix each string with its length and a "#" delimiter (e.g., "hello" becomes "5#hello").
Decode: Parse length before "#", then extract exactly that many characters to reconstruct each original string.

### Optimal Time Complexity

O(n)

n = The sum of the length of all of the strings

### Optimal Space Complexity

O(n+m)

n = The sum of the length of all of the strings
m = The number of strings