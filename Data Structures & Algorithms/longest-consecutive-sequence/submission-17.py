class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashset = set(nums)
        for num in nums:
            streak, cur = 0, num
            while cur in hashset:
                cur += 1
                streak += 1
            res = max(res, streak)
        return 0 if not nums else res

        
