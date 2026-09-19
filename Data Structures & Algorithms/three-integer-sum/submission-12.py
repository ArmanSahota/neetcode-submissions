class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            if a > 0:
                break
            
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = a + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    result.append([a, nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return result



                

