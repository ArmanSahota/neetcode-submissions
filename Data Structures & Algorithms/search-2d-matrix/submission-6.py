class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        L, R = 0, ROWS * COLS - 1
        while L <= R:
            M = L + (R - L) // 2
            row, col = M // COLS, M % COLS
            if target > matrix[row][col]:
                L = M + 1
            elif target < matrix[row][col]:
                R = M - 1
            else:
                return True
        return False


        

        