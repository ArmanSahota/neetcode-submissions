class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top = 0
        bottom = ROWS - 1

        while top <= bottom:
            M = (top + bottom) // 2

            if target > matrix[M][-1]:
                top =  M + 1
            elif target < matrix[M][0]:
                bottom = M - 1
            else:
                break
        if not (top <= bottom):
            return False
        L = 0
        R = COLS - 1
        while L <= R:
            mid = (L + R) // 2
            if matrix[M][mid] > target:
                R =  mid - 1
            elif matrix[M][mid] < target:
                L = mid + 1
            else:
                return True
        return False


        