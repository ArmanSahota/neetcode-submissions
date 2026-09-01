class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in s: return i
            elif i + 1 not in s:
                return i + 1
        