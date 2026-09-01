class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        output = 1
        list1 = []
        if not nums:
            return 0
        
        print (nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i - 1] == nums[i] - 1:
                output += 1
                print(output)
            elif nums[i - 1] == nums[i]:
                continue
            else:
                list1.append(output)
                output = 1

        return max(max(list1, default=0), 1)

            
        
        