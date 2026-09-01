class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            curMax = -1
            for j in range(i + 1, len(arr)):
                curMax = max(arr[j], curMax)
            arr[i] = curMax
        return arr
                
        