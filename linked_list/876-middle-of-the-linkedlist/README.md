# 876. Middle Of The Linkedlist

**Link**: [LeetCode - Middle Of The Linkedlist](https://leetcode.com/problems/middle-of-the-linked-list/)

---

## Problem
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

---

## Example
### Normal
- Input: [1,2,3,4,5]
- Output: [3,4,5]

### Edge
- Input: [1,2,3,4]
- Output: [3,4]

### Invalid
- Input: []
- Output: []

---

## Approach
1. **Brute Force**:
    - go thru the whole list, get len, then traverse len // 2

2. **Optimal Solution**:
    - slow and fast pointer, when fast is None, slow is the middle

---

## Complexity
- **Time**: O(n)
- **Space**: O(1)

---

## Pitfalls
- 

---
