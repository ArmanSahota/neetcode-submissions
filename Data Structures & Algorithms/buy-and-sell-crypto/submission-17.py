class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for R in range(len(prices)):
            for L in range(R, len(prices)):
                profit = max(profit, (prices[L] - prices[R]))
        return profit
