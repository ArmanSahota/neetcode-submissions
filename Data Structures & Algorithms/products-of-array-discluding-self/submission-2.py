class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        Left = [0] * n
        Right = [0] * n
        l = 1
        r = 1

        for i, num in enumerate(nums):
            Left[i] = l
            j = -i -1
            Right[j] = r
            l *= nums[i]
            r *= nums[j]

        return[l*r for l,r in zip(Left, Right)]
        