class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if i in res:
                res.remove(i)
            else:
                res.append(i)
        res.sort()
        return res[-1] if res else -1

        