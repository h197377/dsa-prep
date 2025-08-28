# 217. Contains Duplicates

**Link**: [LeetCode - Contains Duplicates](https://leetcode.com/problems/contains-duplicate/)

---

## Problem
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

---

## Example
### Normal
- Input: [1,2,3,1]
- Output: True

### Edge
- Input: [1,2,3,...,100]
- Output: False

### Invalid
- Input: []
- Output: False

---

## Approach
1. **Brute Force**:
    - Put everything in a set, if we have seen, return True
    - Might not fit all in memory if large nums O(n) space

2. **Optimal Solution**:
    - We could also sort it O(nlgn) time
    - then just go thru and check prev number if the same. O(1) space

---

## Complexity
- **Time**: O(nlogn)
- **Space**: O(1)

---

## Pitfalls
- ask what the interviewer wants, whats the input like

---
