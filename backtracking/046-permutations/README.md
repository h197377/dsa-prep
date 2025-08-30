# 046. Permutations

**Link**: [LeetCode - Permutations](https://leetcode.com/problems/permutations/)

---

## Problem
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

---

## Example
### Normal
- Input: nums = [1,2,3]
- Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

### Edge
- Input: nums = [0,1]
- Output: [[0,1],[1,0]]

### Invalid
- Input: [[]]
- Output: []

---

## Approach
1. **Brute Force**:
    - (describe)

2. **Optimal Solution**:
    - backtracking
    - need a [used] size of nums to keep track which number used
    - when len(curr) == len(nums), add it in
    - for loop continues with i + 1

---

## Complexity
- **Time**: O(?)
- **Space**: O(?)

---

## Pitfalls
- 

---
