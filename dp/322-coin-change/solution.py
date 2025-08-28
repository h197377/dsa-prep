class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return 0
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if c <= a: #only use coin up to ammount we tryna build
                    if dp[a - c] != float('inf'):
                        dp[a] = min(dp[a], dp[a - c] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
    
