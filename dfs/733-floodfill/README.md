# 733. Floodfill

**Link**: [LeetCode - Floodfill](https://leetcode.com/problems/flood-fill/description/)

---

## Problem
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

---

## Example
### Normal
- Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
- Output: [[2,2,2],[2,2,0],[2,0,1]]

### Edge
- Input: [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 1
- Output: same

### Invalid
- Input: [[]]
- Output: [[]]

---

## Approach
1. **Brute Force**:  
   - n/a  

2. **Optimal Solution**:  
   - go thru and explore each cell from sr, sc
   - watch out for bounds
   - no diagonal travel

---

## Complexity
- **Time**: O(n*m)  
- **Space**: O(1)  

---

## Pitfalls
- check bounds
- make sure color is different than original sr, sc

---
