class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = float('-inf')
        cursum = 0
        for i in range(len(nums)):
            cursum = max(cursum, 0)
            cursum += nums[i]
            maxNum = max(cursum, maxNum)
        return maxNum

        