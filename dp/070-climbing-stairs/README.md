# 070. Climbing Stairs

**Link**: [LeetCode - Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)

---

## Problem
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

---

## Example
### Normal
- Input: n = 2
- Output: 2

### Edge
- Input: n = 0
- Output: 0

### Invalid
- Input: n = -1
- Output: 0

---

## Approach
1. **Brute Force**:  
   - generate all steps, backtracking. O(n!)

2. **Optimal Solution**:  
   - use two variables to track prev 2 steps then we can sum 

---

## Complexity
- **Time**: O(n)
- **Space**: O(1)

---

## Pitfalls
- 

---
