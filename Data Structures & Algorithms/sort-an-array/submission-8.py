class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            left = arr[L : M + 1]
            right = arr[M + 1 : R + 1]
            index, LeftP, RightP = L, 0, 0
            while LeftP < len(left) and RightP < len(right):
                if left[LeftP] < right[RightP]:
                    arr[index] = left[LeftP]
                    LeftP += 1
                else:
                    arr[index] = right[RightP]
                    RightP += 1
                index += 1
            while LeftP < len(left):
                arr[index] = left[LeftP]
                index += 1
                LeftP += 1
            
            while RightP < len(right):
                arr[index] = right[RightP]
                RightP += 1
                index += 1

        def mergeSort(arr, L, R):
            if L >= R:
                return
            M = (L + R) // 2
            mergeSort(arr, L, M)
            mergeSort(arr, M + 1, R)
            merge(arr, L, M, R)
        mergeSort(nums, 0, len(nums) - 1)
        return nums

