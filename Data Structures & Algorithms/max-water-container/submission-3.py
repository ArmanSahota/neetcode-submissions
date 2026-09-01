class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0 
        R = len(heights) - 1
        maxRes = 0
        cur = 0
        while L < R:
            cur = min(heights[L], heights[R]) * (R - L)
            maxRes = max(maxRes, cur)
        
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return maxRes
        