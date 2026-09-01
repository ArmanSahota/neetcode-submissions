class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        total = 0
        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                total = max(total, profit)
            else:
                L = R
            R += 1
        return total
            
