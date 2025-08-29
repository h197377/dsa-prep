# 003. Longest Substring Without Repeats

**Link**: [LeetCode - Longest Substring Without Repeats](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## Problem
Given a string s, find the length of the longest substring without duplicate characters.

---

## Example
### Normal
- Input: abcabcbb
- Output: 3, because abc

### Edge
- Input: bbbbb
- Output: 1

### Invalid
- Input: ""
- Output: 0

---

## Approach
1. **Brute Force**:
    - generate all substrings, then find the one thats longest
    - O(n!)

2. **Optimal Solution**:
    - use a hashmap to track char -> last seen idx
    - update window as we go thru the s

---

## Complexity
- **Time**: O(n)
- **Space**: O(n)

---

## Pitfalls
- always do res = max(res, last_good_idx + 1) regardless if we have seen the current char 

---
