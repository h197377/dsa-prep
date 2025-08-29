# 207. Course Schedule

**Link**: [LeetCode - Course Schedule](https://leetcode.com/problems/course-schedule/)

---

## Problem
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



---

## Example
### Normal
- Input: numCourses = 2, prerequisites = [[1,0]]
- Output: True
- take course 0 to take course 1, course 0 can be taken freely 

### Edge
- Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
- Output: False

### Invalid
- Input: [[]]
- Output: False

---

## Approach
1. **Brute Force**:
    - (describe)

2. **Optimal Solution**:
    - make a indegree[] to track which course has pre-reqs, numTaken to track progress
    - make a hashmap of course -> [unlocked courses]
    - anything with indegree[i] of 0, we add it to queue and run bfs
    - at the end check numTaken == total numCourses

---

## Complexity
- **Time**: O(n)
- **Space**: O(n)

---

## Pitfalls
- careful when adding indegree[i] == 0 courses. 

---
