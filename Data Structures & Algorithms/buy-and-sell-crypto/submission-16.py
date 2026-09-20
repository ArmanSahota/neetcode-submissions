class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Left = 0
        Result = 0
        for Right in range(1, len(prices)):
            if prices[Left] >= prices[Right]:
                Left = Right
            else:
                Result = max(Result, prices[Right] - prices[Left])
        return Result


        
            
