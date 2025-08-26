# 121. Buy Stock

**Link**: [LeetCode - Buy Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

---

## Problem
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

---

## Example
### Normal
- Input: [7,1,5,3,6,4]
- Output: 5

### Edge
- Input: [7,6,5,4,3,1]
- Output: 0
Bear market :(

### Invalid
- Input: []
- Output: 0

---

## Approach
1. **Brute Force**:  
   - for ever i, buy it, then calculate every single sell option
   - O(n^2) worst case which isnt good

2. **Optimal Solution**:  
   - kadane algorithm, at everyday we either sell curr bought and make incremental profit or ditch last buy
   - O(n) 

---

## Complexity
- **Time**: O(n)  
- **Space**: O(1)  

---

## Pitfalls
- ask if input can be negative


---
