class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxPrice = 0
        Left = 0
        Right = 1
        for i in range(len(prices) - 1):
            if prices[Left] >= prices[Right]:
                Left = Right
            else:
                Price = prices[Right] - prices[Left]
                MaxPrice = max(Price, MaxPrice)
            Right += 1
        return (MaxPrice)
        