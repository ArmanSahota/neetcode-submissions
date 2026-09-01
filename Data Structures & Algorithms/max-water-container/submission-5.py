class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        area = 0
        
        while L < R:
            if heights[L] < heights[R]:
                area = max(area, heights[L] * (R - L))
                L += 1
            else:
                area = max(area, heights[R] * (R - L))
                R -= 1
                
        return area


            

        