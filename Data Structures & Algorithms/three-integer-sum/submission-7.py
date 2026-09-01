class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            
            L = i + 1
            R = len(nums) - 1

            while L < R:

                cur = nums[L] + nums[R] + a
                if cur > 0:
                    R -= 1
                elif cur < 0:
                    L += 1
                else:
                    res.append([a, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return res
