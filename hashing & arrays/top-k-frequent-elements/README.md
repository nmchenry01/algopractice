# Top K Frequent Elements

## Category

Arrays and Hashing

## Difficulty

Medium

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

### Example

**Input:** nums = [1,1,1,2,2,3], k = 2  
**Output:** [1,2]

**Input:** nums = [1], k = 1  
**Output:** [1]

### Solution Description

There are two common approaches to solve this problem:

**Naive Solution:**  
Count the frequency of each number using a hash map. Sort the numbers by frequency and return the top `k`. This is easy to implement but takes O(n log n) time.

**Optimal Solution:**  
Count frequencies with a hash map. Use a list of buckets where each index represents a frequency, and each bucket holds numbers with that frequency. Collect the most frequent numbers from the buckets until you have `k`. This runs in O(n) time.

### Optimal Time Complexity

O(n)

### Optimal Space Complexity

O(n)
