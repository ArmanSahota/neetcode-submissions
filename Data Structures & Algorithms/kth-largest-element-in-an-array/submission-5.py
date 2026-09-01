class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(L, R):
            pivot, P = nums[R], L
            for i in range(L, R):
                if nums[i] <= pivot:
                    nums[P], nums[i] = nums[i], nums[P]
                    P +=1
            nums[P], nums[R] = nums[R], nums[P]

            if P > k:
                return quickselect(L, P - 1)
            if P < k:
                return quickselect(P + 1, R)
            else:
                return nums[P]
        return quickselect(0, len(nums) - 1)
    
