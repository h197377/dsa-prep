# 238. Product Of Arrays Except Self

**Link**: [LeetCode - Product Of Arrays Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)

---

## Problem
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

---

## Example
### Normal
- Input: nums = [1,2,3,4]
- Output: [24,12,8,6]

### Edge
- Input: nums = [-1,1,0,-3,3]
- Output: [0,0,9,0,0]

### Invalid
- Input: []
- Output: []

---

## Approach
1. **Brute Force**:
    - for each number, go thru and multiply by numbers other than itself
    - O(n^2)

2. **Optimal Solution**:
    - make empty res[] of all 1s
    - go thru and multiply delayed once from left
    - then make a variable right and multiply delayed from right
    - return res

---

## Complexity
- **Time**: O(n)
- **Space**: O(1) if we don't count res

---

## Pitfalls
- make sure the multiply carry forward
- first left pass do res[i] = nums[i - 1] * res[i - 1] so res[i] is cumlative

---
