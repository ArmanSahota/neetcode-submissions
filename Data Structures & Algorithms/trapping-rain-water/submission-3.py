class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        LeftMax = height[L]
        RightMax = height[R]
        Res = 0

        while L <= R:
            if LeftMax < RightMax:
                LeftMax = max(LeftMax, height[L])
                Res += LeftMax - height[L]
                L += 1
            else:
                RightMax = max(RightMax, height[R])
                Res += RightMax - height[R]
                R -= 1
        return Res
