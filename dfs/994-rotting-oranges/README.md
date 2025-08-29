# 994. Rotting Oranges

**Link**: [LeetCode - Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

---

## Problem
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

---

## Example
### Normal
- Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
- Output: 4

### Edge
- Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
- Output: -1
- Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

### Invalid
- Input: 
- Output: 

---

## Approach
1. **Brute Force**:
    - (describe)

2. **Optimal Solution**:
    - count all the 1s to know numGoodOranges
    - add all the 2s into queue, run bfs
    - for each level, is a day count
    - if at the end numGoodOranges == numRotten we return day count, else return -1

---

## Complexity
- **Time**: O(nm)
- **Space**: O(1)

---

## Pitfalls
- You can end function early if numGoodOranges == 0
- note we need to return days-1 since the first day's rotten is already done 

---
