# Valid Palindrome

## Category

Two Pointers

## Difficulty

Easy

## Problem Statement

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

### Example

Input: s = "Was it a car or a cat I saw?"
Output: true

### Solution Description

Create a helper function to determine alphanumeric (use ord/ascii values) and have two pointers move back towards one another, checking for lowercase equality along the way. If the 
character being looked at by one of the pointers isn't alphanumeric, move the pointer as long as it stays within bounds and is not alphanumeric (while loop).

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(1)
