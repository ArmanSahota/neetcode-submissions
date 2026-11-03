class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            middle = (R + L) // 2
            if nums[middle] == target:
                return middle
            
            if nums[L] <= nums[middle]:
                if target > nums[middle] or target < nums[L]:
                    L = middle + 1
                else:
                    R = middle -1
            else:
                if target < nums[middle] or target > nums[R]:
                    R = middle - 1
                else:
                    L = middle + 1
        return -1
        
