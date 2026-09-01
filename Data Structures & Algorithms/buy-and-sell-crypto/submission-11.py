class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        res = 0
        for R in range(1, len(prices)):
            if prices[R] < prices[L]:
                L = R
            else:
                res = max(res, prices[R] - prices[L])
        return res

