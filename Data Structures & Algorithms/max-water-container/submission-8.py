class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1

        max_volume = 0

        while L < R:
            if heights[L] > heights[R]:
                max_volume = max(max_volume, heights[R] * (R - L))
                R -= 1
            else:
                max_volume = max(max_volume, (heights[L] * (R - L)))
                L += 1
        return max_volume