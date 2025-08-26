# 235. Lowest Common Ancestor Bst

**Link**: [LeetCode - Lowest Common Ancestor Bst](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

---

## Problem
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

---

## Example
### Normal
- Input: [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
- Output: 6

### Edge
- Input: [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
- Output: 2

### Invalid
- Input: [], p = 2, q = 4
- Output: []

---

## Approach
1. **Brute Force**:  
   - get the tree out in pre-order, then see the element before p and q
   - O(n) space which is not needed
   - O(n) time 

2. **Optimal Solution**:  
   - use BST property, if root is bigger than both go left
   - if root is smaller than both we go right
   - if root is in between, it IS the common ancestor

---

## Complexity
- **Time**: O(log n), O(n) if tree is very long  
- **Space**: O(1)

---

## Pitfalls
- watch out when root is one of the p, q

---
