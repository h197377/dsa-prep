# 981. Time Based Key Value Store

**Link**: [LeetCode - Time Based Key Value Store](https://leetcode.com/problems/time-based-key-value-store/)

---

## Problem
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

---

## Example
### Normal
- Input: ["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
- Output: [null, null, "bar", "bar", null, "bar2", "bar2"]

### Edge
- Input: 
- Output: 

### Invalid
- Input: 
- Output: 

---

## Approach
1. **Brute Force**:
    - hashmap of key -> list of (timestamp, value)
    - to get, linear scan to find one where time <= value time stamp, O(n)

2. **Optimal Solution**:
    - hashmap of key -> list of (timestamp, value)
    - run binary search on the timestamp to locate one before it, O(lgn)

---

## Complexity
- **Time**: O(1) to set, O(log n) to get
- **Space**: O(n)

---

## Pitfalls
- when found, we want to keep pushing boundry to the right, as we want the max time <= timestamp
- use while l <= r, with both l = m + 1 and r = m -1 boundry shrink 

---
