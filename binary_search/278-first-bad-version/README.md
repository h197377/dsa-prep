# 278. First Bad Version

**Link**: [LeetCode - First Bad Version](https://leetcode.com/problems/first-bad-version/description/)

---

## Problem
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

---

## Example
### Normal
- Input: n = 5, bad = 4
- Output: 4

### Edge
- Input: n = 10000, bad = 996
- Output: 996

### Invalid
- Input: n = -9
- Output: -1

---

## Approach
1. **Brute Force**:  
   - Go thru every version and call is_bad_version(i), O(n)

2. **Optimal Solution**:  
   - run binary search 

---

## Complexity
- **Time**: O(lgn)
- **Space**: O(1)

---

## Pitfalls
- start from 1 to n
- if isBadVersion(i) is true, r can be fixed
- use **l < r**

---
