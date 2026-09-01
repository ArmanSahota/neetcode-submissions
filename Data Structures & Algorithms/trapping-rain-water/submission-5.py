class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        L = 0
        R = len(height) - 1
        maxleft = height[L]
        maxright = height[R]
        res = 0
        while L < R:
            if maxleft < maxright:
                L += 1
                maxleft = max(maxleft, height[L])
                res += maxleft - height[L]
            else:
                R -= 1
                maxright = max(maxright, height[R])
                res += maxright - height[R]
        return res