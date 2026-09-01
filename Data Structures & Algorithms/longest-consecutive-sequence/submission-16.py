class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 1
        cur = 1
        hashset = set(nums)
        i = 0
        while i < len(nums):
            number = nums[i]
            while number + 1 in hashset:
                cur += 1
                number += 1
            res = max(res, cur)
            cur = 1
            i += 1
        return 0 if not nums else res

        
