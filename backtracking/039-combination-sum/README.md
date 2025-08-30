# 039. Combination Sum

**Link**: [LeetCode - Combination Sum](https://leetcode.com/problems/combination-sum/)

---

## Problem
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

---

## Example
### Normal
- Input: candidates = [2,3,6,7], target = 7
- Output: [[2,2,3],[7]]

### Edge
- Input: candidates = [2,3,5], target = 8
- Output: [[2,2,2,2],[2,3,3],[3,5]]

### Invalid
- Input: [], -1
- Output: []

---

## Approach
1. **Brute Force**:
    - (describe)

2. **Optimal Solution**:
    - use backtracking
    - track curr summed, if == target, add to res
    - dont forget to undo adds

---

## Complexity
- **Time**: O(?)
- **Space**: O(?)

---

## Pitfalls
- 

---
