class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1

        while L < R:
            middle = (R + L) //2
            if nums[middle] > nums[-1]:
                L = middle + 1
            else:
                R = middle
        return nums[L]

