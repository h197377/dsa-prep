# 075. Sort Colors

**Link**: [LeetCode - Sort Colors](https://leetcode.com/problems/sort-colors/)

---

## Problem
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

---

## Example
### Normal
- Input: nums = [2,0,2,1,1,0]
- Output: [0,0,1,1,2,2]

### Edge
- Input: [2,2,2,2,2]
- Output: [2,2,2,2,2]

### Invalid
- Input: []
- Output: []

---

## Approach
1. **Brute Force**:
    - run array.sort, O(log n)

2. **Optimal Solution**:
    - start with a l, m = 0 and r = len() - 1 pointer
    - use arr[m] as main mover
    - if arr[m] = 0, swap arr[m] and arr[l], l++, m++
    - if arr[m] = 1, m++, if arr[m] = 2, swap arr[m], arr[r], r--

---

## Complexity
- **Time**: O(n)
- **Space**: O(1)

---

## Pitfalls
- while m <= r as our checking condition
- only if arr[m] == 0 we move l and r pointers, other ones we only touch one, m or r pointers

---
