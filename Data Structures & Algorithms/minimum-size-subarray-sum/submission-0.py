class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        cur = 0
        res = float('inf')

        for R in range(len(nums)):
            cur += nums[R]

            while cur >= target:
                res = min(res, R - L + 1)
                cur -= nums[L]
                L += 1
        return 0 if res == float('inf') else res
                

