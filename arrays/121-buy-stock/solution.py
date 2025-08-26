
def buyStock(self, prices) -> int:
    if len(prices) < 2:
        return 0
    
    curr = prices[0]
    res = 0
        
    for i in range(1, len(prices)):
        curr = max(0, curr + prices[i] - prices[i - 1])
        res += max(res, curr)

    return res
