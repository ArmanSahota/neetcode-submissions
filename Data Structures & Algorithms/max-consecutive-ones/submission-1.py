class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxC = 0
        c = 0
        i = 0
        for num in nums:
            if num == 1:
                c += 1
            else:
                maxC = max(c, maxC)
                c = 0
            i += 1
        return max(maxC, c)