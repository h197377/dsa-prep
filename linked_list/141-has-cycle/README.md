# 141. Has Cycle

**Link**: [LeetCode - Has Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

---

## Problem
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

---

## Example
### Normal
- Input: head = [3,2,0,-4], pos = 1
- Output: True

### Edge
- Input: 
- Output: 

### Invalid
- Input: []
- Output: False

---

## Approach
1. **Brute Force**:  
   - (describe)  

2. **Optimal Solution**:  
   - fast, slow pointers
   - advance fast twice as fast, 
   - if they intersect its a cycle, if one hits None then no cycle 

---

## Complexity
- **Time**: O(n)  
- **Space**: O(1)  

---

## Pitfalls
-  while fast and fast.next: to check bounds
- fast and slow == check happens after advancement

---
