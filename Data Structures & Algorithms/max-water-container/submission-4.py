class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        
        r = len(heights) - 1
        res = 0
        while l < r:
            leftmax = heights[l]
            rightmax = heights[r]
            if leftmax < rightmax:
                res = max(res, leftmax * (r - l))
                l += 1
            else:
                res = max(res, rightmax * (r - l))
                r -= 1
        return res