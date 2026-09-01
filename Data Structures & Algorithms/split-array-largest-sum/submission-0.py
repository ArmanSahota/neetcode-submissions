class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray + 1 <= k
        L, R = max(nums), sum(nums)
        res = R

        while L <= R:
            Mid = (L + R) // 2
            if canSplit(Mid):
                res = Mid
                R = Mid - 1
            else:
                L = Mid + 1
        return res
        
        