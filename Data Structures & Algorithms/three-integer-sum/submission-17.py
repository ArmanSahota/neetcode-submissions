class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i, a in enumerate(nums):
            if a > 0:
                return result
            if i > 0 and a == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                total = a + nums[L] + nums[R]
                if total == 0:
                    result.append([a, nums[R], nums[L]])
                    R -= 1
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                elif total > 0:
                    R -= 1
                else:
                    L += 1
        return result
