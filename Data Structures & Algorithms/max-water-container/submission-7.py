class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        result = 0
        while l < r:
            if heights[l] > heights[r]:
                result = max(result, heights[r] * (r - l))
                r -= 1
            else:
                result = max(result, heights[l] * (r - l))
                l += 1
        return result
                
