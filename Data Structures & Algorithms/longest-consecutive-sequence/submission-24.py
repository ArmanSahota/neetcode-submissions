class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for i in nums:
            if (i - 1) not in nums:
                c = 1
                cur = i
                while cur + 1 in nums:
                    cur += 1
                    c += 1
                longest = max(longest, c)
        return longest