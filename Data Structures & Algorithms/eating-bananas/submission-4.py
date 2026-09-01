class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        res = float('inf')

        while L <= R:
            M = (L + R) // 2
            cur = 0
            for i in piles:
                cur += math.ceil(i / M)
            if cur > h:
                L = M + 1
            elif cur <= h:
                R = M - 1
                res = min(res, M)
        return res