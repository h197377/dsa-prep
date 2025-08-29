# 542. 01 Matrix

**Link**: [LeetCode - 01 Matrix](https://leetcode.com/problems/01-matrix/)

---

## Problem
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.



---

## Example
### Normal
- Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
- Output: [[0,0,0],[0,1,0],[1,2,1]]

### Edge
- Input: [[1,1,1],[1,0,1],[1,1,1]]
- Output: [[2,1,2],[1,0,1],[2,1,2]]

### Invalid
- Input: [[]]
- Output: [[]]

---

## Approach
1. **Brute Force**:
    - start from each 1, extend outward to find a 0, record distance
    - slow, for each coor, n* n^2 so O(n3)

2. **Optimal Solution**:
    - use -1 to mark visited
    - we start from 0s all at once and advance towards 1 with distance markers in queue
    - [(i, j), dist]
    - if res[i][j] == -1 and matrix[i][j] == 1, we write the distance to dist
    - then return res

---

## Complexity
- **Time**: O(n*m)
- **Space**: O(n*m)

---

## Pitfalls
- 

---
