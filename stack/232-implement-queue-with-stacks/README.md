# 232. Implement Queue With Stacks

**Link**: [LeetCode - Implement Queue With Stacks](https://leetcode.com/problems/implement-queue-using-stacks/description/)

---

## Problem
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

---

## Example
### Normal
- Input: ["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
- Output: [null, null, null, 1, 1, false]

### Edge
- Input: 
- Output: 

### Invalid
- Input: 
- Output: 

---

## Approach
1. **Brute Force**:  
   - (describe)  

2. **Optimal Solution**:  
   - use 2 stacks 
   - one for pushing, one for popping 
   - when asking to pop elements, if pop stack is empty, we empty push stack to pop
   - then perform popping

---

## Complexity
- **Time**: O(1) for push, O(n) for pop if pop stack isnt populated, O(n) for peek if pop stack is empty, O(1) for empty  
- **Space**: O(n) for two stacks  

---

## Pitfalls
- call peek() during pop() to save code

---
