# Reverse Linked List

## Category

Linked List

## Difficulty

Easy

## Problem Statement

Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

### Example

Input: head = [0,1,2,3]

Output: [3,2,1,0]

### Solution Description

Keep track of prev/curr, while there is a current node swap curr.next, prev, then curr, and return prev.

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(1)
