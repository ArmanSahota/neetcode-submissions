class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxCur = 0
        for num in nums:
            if (num - 1) not in nums:
                cur = 1
                while (num + cur) in nums:
                    cur += 1
                maxCur = max(maxCur, cur)
        return maxCur
