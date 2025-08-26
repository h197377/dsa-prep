# 125. Valid Palindrome

**Link**: [LeetCode - Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

---

## Problem
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

---

## Example
### Normal
- Input: s = "A man, a plan, a canal: Panama"
- Output: True
Explanation: "amanaplanacanalpanama" is a palindrome.

### Edge
- Input: "     .    . A,,     "
- Output: True

- "0P"
- False

### Invalid
- Input: None
- Output: False

---

## Approach
1. **Brute Force**:  
   - reverse the entire string and compare with original
   - O(n) space if all characters, we can do O(1)

2. **Optimal Solution**:  
   - two pointer from start and end
   - shrink as possible, ignoring all non-alpha characters
   - isalnum()

---

## Complexity
- **Time**: O(n)  
- **Space**: O(1)  

---

## Pitfalls
-  ask if only char are the ones count for palindrome, e.g. number? 

---
