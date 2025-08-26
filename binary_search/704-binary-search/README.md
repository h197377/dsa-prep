# 704. Binary Search

**Link**: [LeetCode - Binary Search](https://leetcode.com/problems/binary-search/)

---

## Problem
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

---

## Example
### Normal
- Input: nums = [-1,0,3,5,9,12], target = 9
- Output: 4

### Edge
- Input: [-1,-1,-1,-1], target = -5
- Output: -1

### Invalid
- Input: [], target = 9
- Output: -1

---

## Approach
1. **Brute Force**:  
   - go through array and search for element, O(n)

2. **Optimal Solution**:  
   - run binary search, O(logn)

---

## Complexity
- **Time**: O(logn)  
- **Space**: O(1)  

---

## Pitfalls
- check for duplicate answer return
- use m = x + 1, and while l <= r

---
