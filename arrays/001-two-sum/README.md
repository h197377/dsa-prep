# 0001. Two Sum

**Link**: [LeetCode - Two Sum](https://leetcode.com/problems/two-sum/)

---

## Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.  
You may assume that each input would have exactly one solution, and you may not use the same element twice.  
You can return the answer in any order.

---

## Example
**Input**: nums = [2,7,11,15], target = 9  
**Output**: [0,1]  

---

## Approach
1. **Brute force**: Check every pair → O(n²) time.  
2. **Optimal (HashMap)**:  
   - Iterate once, store numbers in a hashmap as `missing val -> index`.  
   - For each `num`, check if `missing` exists in hashmap.  
   - If yes, return indices.
   - If not, hm[num] = index

---

## Complexity
- **Time**: O(n)
- **Space**: O(n) (hashmap)

---

## Pitfalls
- Don’t reuse the same element twice.  
- Watch for duplicates (e.g., nums = [3,3], target = 6).

---