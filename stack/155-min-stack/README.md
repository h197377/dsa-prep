# 155. Min Stack

**Link**: [LeetCode - Min Stack](https://leetcode.com/problems/min-stack/)

---

## Problem
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

---

## Example
### Normal
- Input ["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

- Output [null,null,null,null,-3,null,0,-2]

### Edge
- Input: 
- Output: 

### Invalid
- Input: 
- Output: 

---

## Approach
1. **Brute Force**:
    - make two stacks, the other stack pushes the same number of elements but just the minimum. When popping, pop on both

2. **Optimal Solution**:
    - make two stacks, one pushes ele, other one only pushes when current push is less than top (new min), during popping, only pop when the main pop is == min

---

## Complexity
- **Time**: O(n)
- **Space**: O(n + k), k is number of minimums

---

## Pitfalls
- if not self.min_stk or val <= self.min_stk[-1]:
- note the above <=, this will make sure we not just pop the min element once

---
