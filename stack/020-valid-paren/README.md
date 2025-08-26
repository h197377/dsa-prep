# 020. Two Sum

**Link**: [LeetCode - Valid Parenthesis](https://leetcode.com/problems/valid-parentheses/)

---

## Problem
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

---

## Example
- Normal
**Input**: s = ()
**Output**: True

- Edge
**Input**: s = [[[[[[[[[[[[[[())]]]]]]]]]]]]]]
**Output**: True

- Invalid
**Input**: s = 1559
**Output**: False
---

## Approach
2. **Optimal (stack)**:  
   - Iterate once, if we see an open (, we push ) to it 
   - otherwise we check if stack pop is the same as current close bracket  
   - If stack is empty at the end we good

---

## Complexity
- **Time**: O(n)
- **Space**: O(n) (stack)

---

## Pitfalls
- verify if we will only have bracket chars 
- at the end check if stack is empty

---