class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0 : -1}

        total = 0

        for i, num in enumerate(nums):
            total += num

            r = total % k

            if r in hashmap:
                if i - hashmap[r]  > 1:
                    return True
            else:
                hashmap[r] = i
        return False