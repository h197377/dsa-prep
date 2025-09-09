# 236. Lowest Common Ancestor Of Binary Tree

**Link**: [LeetCode - Lowest Common Ancestor Of Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

---

## Problem
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

---

## Example
### Normal
- Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
- Output: 3

### Edge
- Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
- Output: 5

### Invalid
- Input: []
- Output: -1

---

## Approach
1. **Brute Force**:
    - (describe)

2. **Optimal Solution**:
    - start from root, if root is p or q we return root
    - if not we recurse down, if left or right is root we return the non-null one

---

## Complexity
- **Time**: O(n)
- **Space**: O(h)

---

## Pitfalls
- 

---
