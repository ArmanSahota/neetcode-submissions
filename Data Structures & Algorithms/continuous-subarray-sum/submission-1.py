class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        stack = [sum(nums)]
        if len(nums) < 2:
            return False
        for i in range(len(nums)):
            cur = stack.pop()
            if cur % k == 0:
                return True
            stack.append(cur - nums[i])
        return False

