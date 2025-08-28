# 067. Add Binary

**Link**: [LeetCode - Add Binary](https://leetcode.com/problems/add-binary/)

---

## Problem
Given two binary strings a and b, return their sum as a binary string.

---

## Example
### Normal
- Input: a = "11", b = "1"
- Output: "100"

### Edge
- Input: "0000", "1"
- Output: "1"

### Invalid
- Input: "1", ""
- Output: "1"

---

## Approach
1. **Brute Force**:
    - convert to int then add, which isnt allowed

2. **Optimal Solution**:
    - go from the back of each of the strings, add with mod 2 check of carry
    - reverse at the end

---

## Complexity
- **Time**: O(n + m)
- **Space**: O(1)

---

## Pitfalls
- 

---
