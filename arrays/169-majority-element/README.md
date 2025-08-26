# 169. Majority Element

**Link**: [LeetCode - Majority Element](https://leetcode.com/problems/majority-element/)

---

## Problem
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

---

## Example
### Normal
- Input: nums = [3,2,3]
- Output: 3

### Edge
- Input: nums = [1,1,1,1,1,2,2,2,2]
- Output: 1

### Invalid
- Input: []
- Output: -1

---

## Approach
1. **Brute Force**:
    - make a hashmap to track element -> freq
    - O(n) space

2. **Optimal Solution**:
    - simply maintain a best counter

---

## Complexity
- **Time**: O(n)
- **Space**: O(1)

---

## Pitfalls
- reset when count == 0

---
