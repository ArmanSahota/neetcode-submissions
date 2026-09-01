class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L = 0

        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
            else:
                res = max(res, prices[R] - prices[L])
        return res
