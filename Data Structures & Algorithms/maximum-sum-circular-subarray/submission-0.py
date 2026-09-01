class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMin, curMax = 0, 0

        globalMin, globalMax = nums[0], nums[0]
        total = 0


        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
