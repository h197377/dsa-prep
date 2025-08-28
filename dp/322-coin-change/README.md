# 322. Coin Change

**Link**: [LeetCode - Coin Change](https://leetcode.com/problems/coin-change/)

---

## Problem
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

---

## Example
### Normal
- Input: coins = [1,2,5], amount = 11
- Output: 3, because 5 + 5 + 1

### Edge
- Input: [2], 3
- Output: -1

### Invalid
- Input: [1], 0
- Output: 0

---

## Approach
1. **Brute Force**:
    - greedily use bigger coins first
    - generate all coin combo up to the amount

2. **Optimal Solution**:
    - use dynamic programming
    - make an dp[] of size amount + 1
    - dp[0] = 0 as it costs nothing to make amount 0
    - for all amounts,
    -   for all coin types
    -       see if dp[c - amount] is non-infinite, if so, we get the dp[c - amount] + 1 coin
    - dp[-1] is answer

---

## Complexity
- **Time**: O(n), n = amount
- **Space**: O(n)

---

## Pitfalls
- if dp[-1] is still untouched, we cant make this and return 0
- the coin c only goes to <= amount, else dp[a - c] will crash

---
