class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) -1
        leftMax = height[L]
        rightMax = height[R]
        res = 0

        while L <= R:
            if leftMax < rightMax:
                leftMax = max(leftMax, height[L])
                res += leftMax - height[L]
                L += 1
            else:
                rightMax = max(rightMax, height[R])
                res += rightMax - height[R]
                R -= 1
        return res
