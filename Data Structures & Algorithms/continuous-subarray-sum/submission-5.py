class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0 : -1}
        curSum = 0
        for i, num in enumerate(nums):
            curSum += num
            R = curSum % k
            if R not in hashmap:
                hashmap[R] = i
            elif i - hashmap[R] > 1:
                return True
        return False


        