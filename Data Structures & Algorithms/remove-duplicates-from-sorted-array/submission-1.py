class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Turn the list into a set 
        temp = sorted(set(nums))
        nums[:] = temp
        return len(nums)