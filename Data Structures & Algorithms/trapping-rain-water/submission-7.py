class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        res = 0
        leftmax = height[L]
        rightmax = height[R]
        while L <= R:
            if leftmax < rightmax:
                leftmax = max(leftmax, height[L])
                res += leftmax - height[L]
                L += 1
            else:
                rightmax = max(rightmax, height[R])
                res += rightmax - height[R]
                R -= 1
        return res

