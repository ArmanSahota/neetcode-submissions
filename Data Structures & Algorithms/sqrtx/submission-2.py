class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        L = 1
        R = x - 1
        while L <= R:
            M = (L + R) // 2
            if M * M > x:
                R = M - 1
            elif M * M < x:
                L = M + 1
            else:
                return M
        return R