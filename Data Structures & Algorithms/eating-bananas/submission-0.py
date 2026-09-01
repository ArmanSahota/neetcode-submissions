class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        res = R
        while L <= R:
            M = (L + R) // 2
            totalT = 0
            for p in piles:
                totalT += math.ceil(float(p) / M)
            if totalT <= h:
                res = min(res, M)
                R = M - 1
            else:
                L = M + 1
        return res

