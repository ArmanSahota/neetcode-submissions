class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            answer = target - n
            if answer in hashmap:
                return[hashmap[answer], i]
            hashmap[n] = i