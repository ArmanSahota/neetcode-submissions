class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        total = 0
        L = 0

        for R in range(len(nums)):
            total += nums[R]
            result = max(result, total)
            if total < 0:
                total = 0
                L = R
        return result
            


