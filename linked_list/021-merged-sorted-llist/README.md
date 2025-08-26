# 021. Merged Sorted Llist

**Link**: [LeetCode - Merged Sorted Llist](https://leetcode.com/problems/merge-two-sorted-lists/)

---

## Problem
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

---

## Example
### Normal
- Input: list1 = [1,2,4], list2 = [1,3,4]
- Output: [1,1,2,3,4,4]

### Edge
- Input: list1 = [1,2,4,5,5,6,7,8], list2 = [1,3,4]
- Output: [1,1,2,3,4,4, 5, 5, 6, 7, 8]

### Invalid
- Input: list1 = [], list2 = None
- Output: []

---

## Approach
1. **Brute Force** (if applicable):  
   - put all nodes into a array, then native sort
   - nlgn time, and also n space 

2. **Optimal Solution**:  
   - track both heads, then just recursively call

---

## Complexity
- **Time**: O(n + m)  
- **Space**: O(1)  

---

## Pitfalls
- use dummy node
- connect the other list if one list was all exhausted

---
