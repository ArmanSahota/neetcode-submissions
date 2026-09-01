class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        window = set()
        for i in nums:
            if i in window: 
                return i
            window.add(i)
        