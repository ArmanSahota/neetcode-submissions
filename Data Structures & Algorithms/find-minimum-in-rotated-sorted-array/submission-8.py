class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        boundary_index = -1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] <= nums[-1]:
                boundary_index = nums[mid]
                R = mid - 1
            else:
                L = mid + 1
        return boundary_index

        