# 098. Validate Binary Search Tree

**Link**: [LeetCode - Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

---

## Problem
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.

---

## Example
### Normal
- Input: root = [2,1,3]
- Output: True

### Edge
- Input: root = [5,1,4,null,null,3,6]
- Output: False

### Invalid
- Input: []
- Output: True

---

## Approach
1. **Brute Force**:
    - walk the tree with in-order traversal, then compare if value is strictly greater than last one

2. **Optimal Solution**:
    - do in order traversal, while keeping track of prev, if curr val ever <= prev.val, return False
    - else True

---

## Complexity
- **Time**: O(n)
- **Space**: O(1)

---

## Pitfalls
- remember the iterative in order traversal
- use a stack, keep pushing node and its left
- when node is Null, we pop it out to process it, do something
- then node = node.right 
- and implicitly let the while loop handle the rest

---
