class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = nums[0]
        cursum = 0
        for i in range(len(nums)):
            cursum = max(cursum, 0)
            cursum += nums[i]
            maxNum = max(cursum, maxNum)
        return maxNum

        