# 226. Invert Bst

**Link**: [LeetCode - Invert Bst](https://leetcode.com/problems/invert-binary-tree/description/)

---

## Problem
Given the root of a binary tree, invert the tree, and return its root.

---

## Example
### Normal
- Input: [4,2,7,1,3,6,9]
- Output: [4,7,2,9,6,3,1]

### Edge
- Input: same
- Output: 

### Invalid
- Input: []
- Output: []

---

## Approach
1. **Brute Force**:  
   - N/A

2. **Optimal Solution**:  
   - switch left with right recursively
   - if want iterative, do a queue then swap left and right, then add children 

---

## Complexity
- **Time**: O(n)  
- **Space**: O(height) for recursion - for balanced,h = O(logn), for skewed, h = O(n), 

---

## Pitfalls
-  

---
