class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        res = 0
        LeftMax = height[L]
        RightMax = height[R]
        while L < R:
            if LeftMax < RightMax:
                L += 1
                LeftMax = max(LeftMax, height[L])
                res += LeftMax - height[L]
            else:
                R -= 1
                RightMax = max(RightMax, height[R])
                res += RightMax - height[R]
        return (res)
            
        