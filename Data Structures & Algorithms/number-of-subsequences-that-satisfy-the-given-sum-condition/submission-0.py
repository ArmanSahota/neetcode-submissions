class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = (10 ** 9 + 7)
        R = len(nums) - 1
        for i , left in enumerate(nums):
            while left + nums[R] > target and i <= R:
                R -= 1
            if i <= R:
                res += (2 ** (R - i)) 
                res %= mod
        return res

        