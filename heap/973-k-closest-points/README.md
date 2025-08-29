# 973. K Closest Points

**Link**: [LeetCode - K Closest Points](https://leetcode.com/problems/k-closest-points-to-origin/)

---

## Problem
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

---

## Example
### Normal
- Input: points = [[1,3],[-2,2]], k = 1
- Output: [[-2,2]]

### Edge
- Input: points = [[3,3],[5,-1],[-2,4]], k = 2
- Output: [[3,3],[-2,4]]

### Invalid
- Input: [[]]
- Output: [[]]

---

## Approach
1. **Brute Force**:
    - min heap, load entire points, then pop top k
    - O(n log n), with O(n) space

2. **Optimal Solution**:
    - (opposite) MAX heap, load only up to k points, then pop once count >= k

---

## Complexity
- **Time**: O(n log k)
- **Space**: O(k)

---

## Pitfalls
- closest points -> opposite of (default) min heap -> max heap
- distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
- return [point for _, point in h] 

---
