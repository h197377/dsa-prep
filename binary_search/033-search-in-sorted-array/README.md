# 033. Search In Sorted Array

**Link**: [LeetCode - Search In Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

---

## Problem
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



---

## Example
### Normal
- Input: nums = [4,5,6,7,0,1,2], target = 0
- Output: 4

### Edge
- Input: nums = [4,5,6,7,0,1,2], target = 3
- Output: -1

### Invalid
- Input: []
- Output: -1

---

## Approach
1. **Brute Force**:
    - go thru the list, O(n)

2. **Optimal Solution**:
    - run binary search
    - during each iteration, with l, m, r, check if left or right half is sorted
    - on the sorted side, check if nums[start] <= target <= nums[end], then go that side
    - otherwise we go to other

---

## Complexity
- **Time**: O(log n)
- **Space**: O(1)

---

## Pitfalls
- use <=, and m +- 1 for this one since if we found match we return it right away 

---
