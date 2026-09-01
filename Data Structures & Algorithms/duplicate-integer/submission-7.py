class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]] = i
        return False