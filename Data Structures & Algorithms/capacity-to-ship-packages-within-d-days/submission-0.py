class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        L = max(weights)
        R = sum(weights)
        res = R

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap
                currCap -= w
            return True
        while L <= R:
            cap = (L + R)// 2
            if canShip(cap):
                res = min(res, cap)
                R = cap - 1
            else:
                L = cap + 1
        return res
