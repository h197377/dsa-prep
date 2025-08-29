# 057. Insert Interval

**Link**: [LeetCode - Insert Interval](https://leetcode.com/problems/insert-interval/)

---

## Problem
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

---

## Example
### Normal
- Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
- Output: [[1,5],[6,9]]

### Edge
- Input: intervals = [[1,3],[6,9]], newInterval = [11,12]
- Output: [[1,3],[6,9],[11,12]]

### Invalid
- Input: [], []
- Output: []

---

## Approach
1. **Brute Force**:
    - (describe)

2. **Optimal Solution**:
    - 3 sets, 
    - the intervals that end before NEW interval starts
    - intervals that end after NEW interval starts need to be merged
    - anything else that starts after NEW interval ends

---

## Complexity
- **Time**: O(n)
- **Space**: O(1)

---

## Pitfalls
- confirm if already sorted by start
- need 3 separate whiles 
- to check overlap, need "as long as the next interval starts before or equal the new interval ends"
-       intervals[i][0] <= newInterval[1]:

---
