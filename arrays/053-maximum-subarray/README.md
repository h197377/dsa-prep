# 053. Maximum Subarray

**Link**: [LeetCode - Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

---

## Problem
Given an integer array nums, find the subarray with the largest sum, and return its sum.

---

## Example
### Normal
- Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
- Output: 6

### Edge
- Input: [-1, -1, -1, -1]
- Output: -1

### Invalid
- Input: []
- Output: 0

---

## Approach
1. **Brute Force**:
    - generate all subarrays and get the max value, O(n!)

2. **Optimal Solution**:
    - run thru the array once, check if we can do better by summing up running elements, or take the current one


---

## Complexity
- **Time**: O(n)
- **Space**: O(1)

---

## Pitfalls
- make sure to start with first element, in case its like -1, we still take -1, not default to 0

---
