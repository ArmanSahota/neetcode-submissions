class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        L = 0
        R = 1
        for i in range(len(prices) - 1):
            if prices[L] >= prices[R]:
                L = R
                R += 1
            else:
                price = prices[R] - prices[L]
                maxP = max(maxP, price)
                R += 1
        return maxP
        