# 383. Ransom Note

**Link**: [LeetCode - Ransom Note](https://leetcode.com/problems/ransom-note/description/)

---

## Problem
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

---

## Example
### Normal
- Input: ransomNote = "a", magazine = "b"
- Output: False

### Edge
- Input: ransomNote = "", magazine = "aaa"
- Output: True

### Invalid
- Input: ransomNote = "a", magazine = ""
- Output: False

---

## Approach
1. **Brute Force**:  
   - make a hashmap of magazine letters
   - decrement ransomNote as we consume letters
   - O(n) space

2. **Optimal Solution**:  
   - Use int[26] to track letter availability
   - go thru magazine once to load all letters, then write ransomNote

---

## Complexity
- **Time**: O(n + m)
- **Space**: O(26) or O(1)

---

## Pitfalls
- can we have non letters to worry about?

---
