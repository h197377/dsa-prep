# 409. Longest Palindrome

**Link**: [LeetCode - Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

---

## Problem
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

---

## Example
### Normal
- Input: abccccdd
- Output: 7

### Edge
- Input: aa
- Output: 2

### Invalid
- Input: ""
- Output: 0

---

## Approach
1. **Brute Force**:  
   - generate all string possibilities then get longest palindrome ones. O(n!)

2. **Optimal Solution**:  
   - We count the single characters. 
   - Then math: string length - num_singles + 1 because we can put it in middle

---

## Complexity
- **Time**: O(n)
- **Space**: O(n)

---

## Pitfalls
- if there are no singles, nothing goes in center so no + 1 !!

---
