# 150. Evaluate Polish Notation

**Link**: [LeetCode - Evaluate Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

---

## Problem
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

---

## Example
### Normal
- Input: tokens = ["2","1","+","3","*"]
- Output: 9
- Explanation: ((2 + 1) * 3) = 9

### Edge
- Input: tokens = ["4","13","5","/","+"]
- Output: 6
- Explanation: (4 + (13 / 5)) = 6

### Invalid
- Input: []
- Output: 0

---

## Approach
1. **Brute Force**:
    - (describe)

2. **Optimal Solution**:
    - stack to push numbers
    - if we see a non-digit, we pop it as the sign
    - once computed we put the answer right back into stack
    - return stack[-1]

---

## Complexity
- **Time**: O(n)
- **Space**: O(n) for stack

---

## Pitfalls
- ask if inputs will be valid
- ask if they want decimals for division, how to round? 
- if c in ["+", "-", "*", "/"]: is alot safer

---
