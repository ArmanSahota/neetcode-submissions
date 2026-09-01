class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = nums[0]
        L = 0
        R = len(nums) - 1
        while L <= R:
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break
            m = (L + R) // 2
            res = min(res, nums[m])
            if nums[L] <= nums[m]:
                L = m + 1
            else:
                R = m - 1
        return res
        


        