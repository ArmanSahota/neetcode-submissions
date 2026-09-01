class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        res = 0
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            diff = cur - k
            res += prefix.get(diff, 0)
            prefix[cur] = 1 + prefix.get(cur, 0)
            
        return res


