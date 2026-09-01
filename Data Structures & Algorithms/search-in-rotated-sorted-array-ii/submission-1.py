class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L, R = 0, len(nums) - 1

        while L <= R:
            M = (L + R) // 2

            if nums[M] == target:
                return True

            if nums[L] == nums[M] == nums[R]:
                L += 1
                R -= 1

            elif nums[L] <= nums[M]:  # left sorted
                if nums[L] <= target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1

            else:  # right sorted
                if nums[M] < target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1

        return False