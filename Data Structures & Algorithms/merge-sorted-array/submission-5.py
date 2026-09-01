class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        maxNums1 = m - 1
        maxNums2 = n - 1
        lastIndex = m + n - 1

        while maxNums2 >=0:
            if maxNums1 >= 0 and nums1[maxNums1] > nums2[maxNums2]:
                nums1[lastIndex] = nums1[maxNums1]
                maxNums1 -= 1
            else:
                nums1[lastIndex] = nums2[maxNums2]
                maxNums2 -= 1
            lastIndex -= 1




        
        


            
        