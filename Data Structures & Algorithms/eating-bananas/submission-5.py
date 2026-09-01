class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        res = float('inf')

        while L <= R:
            M =(L + R) // 2
            cur = 0
            for i in piles:
                cur += math.ceil(float(i) / M)
            if cur <= h:
                res = min(M, res)
                R = M - 1
            else:
                L = M + 1
        return res
