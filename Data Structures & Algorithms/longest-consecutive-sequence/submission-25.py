class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for i in nums:
            if i - 1 in nums:
                continue
            c = 1
            while i + 1 in nums:
                c += 1
                i += 1
            longest = max(c, longest)
        return longest

