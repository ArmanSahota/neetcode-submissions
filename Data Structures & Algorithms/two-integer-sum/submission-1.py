class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            ans = target - n
            if ans in hashmap:
                return [hashmap[ans], i]
            hashmap[n] = i