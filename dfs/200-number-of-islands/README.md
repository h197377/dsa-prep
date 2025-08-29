# 200. Number Of Islands

**Link**: [LeetCode - Number Of Islands](https://leetcode.com/problems/number-of-islands/)

---

## Problem
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

---

## Example
### Normal
- Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
- Output: 1

### Edge
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

### Invalid
- Input: [[]]
- Output: 0

---

## Approach
1. **Brute Force**:
    - (describe)

2. **Optimal Solution**:
    - go thru coordinate, if we see a 1 we increment counter, set to 0, then dfs its neighboring islands

---

## Complexity
- **Time**: O(nm)
- **Space**: O(1)

---

## Pitfalls
- Verify if cell value is 1 or "1"

---
