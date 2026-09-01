class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_index = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            r = prefix % k

            if r in remainder_index:
                if i - remainder_index[r] > 1:
                    return True
            else:
                remainder_index[r] = i

        return False