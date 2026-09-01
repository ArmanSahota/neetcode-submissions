class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC = 0
        c = 0
        i = 0
        while i <= len(nums) - 1:
            if nums[i] == 1:
                c += 1
            else:
                maxC = max(c, maxC)
                c = 0
            i += 1
        return max(maxC, c)