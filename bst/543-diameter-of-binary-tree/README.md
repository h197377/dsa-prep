# 543. Diameter Of Binary Tree

**Link**: [LeetCode - Diameter Of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

---

## Problem
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

---

## Example
### Normal
- Input: root = [1,2,3,4,5]
- Output: 3, since [4,2,1,3]

### Edge
- Input: [1, 2]
- Output: 1

### Invalid
- Input: []
- Output: 0

---

## Approach
1. **Brute Force**:
    - (describe)

2. **Optimal Solution**:
    - need a helper function
    - res gets update with max(res, left + right), no +1 since we want the number of edges, not nodes
    - recursively call down each child, then return 1+ max(left, right) for the height

---

## Complexity
- **Time**: O(n)
- **Space**: O(h)

---

## Pitfalls
- 

---
