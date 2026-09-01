class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxV = 0
        L = 0
        R = len(heights) - 1
        while L < R:
            volume = min(heights[L], heights[R]) * (R - L)
            maxV = max(volume, maxV)
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return maxV
            