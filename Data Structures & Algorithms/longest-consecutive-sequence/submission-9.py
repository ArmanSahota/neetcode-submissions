class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = 1
        current = 1
        hashset = sorted(set(nums))
        for i in hashset:
            if (i - 1) in hashset:
                current += 1
                length = max(current, length)
                print(i)
            else:
                length = max(current, length)
                current = 1
                
        return length
        