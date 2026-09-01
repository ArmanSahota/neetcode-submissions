class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        area = 0
        leftmax = height[L]
        rightmax = height[R]
        while L < R:
            if leftmax < rightmax:
                L += 1
                leftmax = max(leftmax, height[L])
                area += leftmax - height[L]
            else:
                R -= 1
                rightmax = max(rightmax, height[R])
                area += rightmax - height[R]
        return area if height else 0