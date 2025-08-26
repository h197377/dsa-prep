# 110. Balanced Binary Tree

**Link**: [LeetCode - Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)

---

## Problem
Given a binary tree, determine if it is height-balanced.

If height of left and right differ by at most 1
---

## Example
### Normal
- Input: root = [3,9,20,null,null,15,7]
- Output: True

### Edge
- Input: root = [1,2,3,4,5,6,7]
- Output: False

### Invalid
- Input: []
- Output: False

---

## Approach
1. **Brute Force**:  
   - no pruning, compute heights everytime. 
   - O(n^2) since we call height for each node, if tree is skewed is bad

2. **Optimal Solution**:  
   - check left and right, 
   - if either one has height difference > 1 we return -1 right away
   - O(n)

---

## Complexity
- **Time**: O(n)
- **Space**: O(h) for height  

---

## Pitfalls
-   

---
