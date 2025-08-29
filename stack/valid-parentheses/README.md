# Valid Parentheses

## Category

Stack

## Difficulty

Easy

## Problem Statement

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

### Example

Input: s = "([{}])"

Output: true

### Solution Description

Use a stack to keep track of opening characters. Iterate through string, adding to the stack if an opening character. If a closing character, return false if no match or stack empty. At the end, if the stack is empty we can return true, otherwise false.

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(n)
