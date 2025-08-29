# 015. 3Sum

**Link**: [LeetCode - 3Sum](https://leetcode.com/problems/3sum/)

---

## Problem
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

---

## Example
### Normal
- Input: nums = [-1,0,1,2,-1,-4]
- Output: [[-1,-1,2],[-1,0,1]]

### Edge
- Input: nums = [0,1,1]
- Output: []

### Invalid
- Input: []
- Output: []

---

## Approach
1. **Brute Force**:
    - generate all 3 number pairs, then see if they add up, slow

2. **Optimal Solution**:
    - sort the numbers
    - for each i, start 2 pointer of [i + 1, n - 1]
    - once we have a match, add to res, then scan for duplicates if match
    - advance either pointer if not match

---

## Complexity
- **Time**: O(n^2)
- **Space**: O(1)

---

## Pitfalls
- ask what they want to do with duplicates, include or not?

---
